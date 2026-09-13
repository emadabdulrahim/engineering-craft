import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


PROJECT = Path(__file__).resolve().parents[1]
DESTINATIONS = (".claude/skills", ".agents/skills")


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="engineering-craft-")
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name).resolve()
        self.checkout = self.base / "checkout with spaces"
        self.checkout.mkdir()
        shutil.copy2(PROJECT / "install.sh", self.checkout / "install.sh")
        shutil.copytree(PROJECT / "skills", self.checkout / "skills")
        self.skills = sorted(
            file.parent.name for file in (self.checkout / "skills").glob("*/SKILL.md")
        )
        self.home = self.make_home("home with spaces")

    def make_home(self, name):
        home = self.base / name
        home.mkdir()
        return home

    def run_installer(self, *arguments, home=None, success=True, script=None):
        result = subprocess.run(
            [str(script or self.checkout / "install.sh"), *arguments],
            cwd=self.base,
            env={**os.environ, "HOME": str(self.home if home is None else home)},
            capture_output=True,
            text=True,
        )
        if success:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def assert_installed(self, home=None):
        home = home or self.home
        for destination in DESTINATIONS:
            folder = home / destination
            for name in self.skills:
                link = folder / name
                self.assertTrue(link.is_symlink(), link)
                self.assertEqual(link.readlink(), self.checkout / "skills" / name)
                self.assertEqual(
                    (link / "SKILL.md").read_bytes(),
                    (self.checkout / "skills" / name / "SKILL.md").read_bytes(),
                )

    def test_installs_from_another_directory_with_spaces_in_paths(self):
        self.run_installer()
        self.assert_installed()
        self.assertEqual(
            {entry.name for entry in self.home.iterdir()}, {".claude", ".agents"}
        )

    def test_repeated_install_leaves_correct_links_unchanged(self):
        self.run_installer()
        link = self.home / ".agents/skills/craft"
        before = link.lstat()
        self.run_installer()
        after = link.lstat()
        self.assertEqual(
            (before.st_ino, before.st_mtime_ns),
            (after.st_ino, after.st_mtime_ns),
        )
        self.assert_installed()

    def test_source_edits_are_visible_without_reinstalling(self):
        self.run_installer()
        source = self.checkout / "skills/craft/SKILL.md"
        updated = source.read_text() + "\nUpdated instructions.\n"
        source.write_text(updated)
        for destination in DESTINATIONS:
            self.assertEqual(
                (self.home / destination / "craft/SKILL.md").read_text(), updated
            )

    def test_reinstall_discovers_new_skills(self):
        self.run_installer()
        source = self.checkout / "skills/new-skill"
        source.mkdir()
        (source / "SKILL.md").write_text(
            "---\nname: new-skill\ndescription: Test fixture\n---\n"
        )
        self.run_installer()
        for destination in DESTINATIONS:
            self.assertEqual((self.home / destination / "new-skill").readlink(), source)

    def test_conflicts_fail_before_any_links_are_installed(self):
        for kind in ("file", "directory", "symlink", "broken-symlink"):
            with self.subTest(kind=kind):
                home = self.make_home(f"conflict-{kind}")
                conflict = home / ".agents/skills/unslop"
                conflict.parent.mkdir(parents=True)
                foreign = self.base / f"foreign-{kind}"
                if kind == "file":
                    conflict.write_text("keep this file")
                elif kind == "directory":
                    conflict.mkdir()
                    (conflict / "keep.txt").write_text("keep this directory")
                else:
                    if kind == "symlink":
                        foreign.mkdir()
                    conflict.symlink_to(foreign)
                result = self.run_installer(home=home, success=False)
                self.assertIn("Conflict:", result.stderr)
                self.assertIn("Nothing installed", result.stderr)
                self.assertFalse((home / ".claude").exists())
                self.assertEqual(list(conflict.parent.iterdir()), [conflict])
                if kind == "file":
                    self.assertEqual(conflict.read_text(), "keep this file")
                elif kind == "directory":
                    self.assertEqual(
                        (conflict / "keep.txt").read_text(), "keep this directory"
                    )
                else:
                    self.assertEqual(conflict.readlink(), foreign)

    def test_non_directory_destination_or_parent_fails_before_install(self):
        for path in (".agents", ".agents/skills"):
            with self.subTest(path=path):
                home = self.make_home("blocked-" + path.replace("/", "-"))
                blocker = home / path
                blocker.parent.mkdir(parents=True, exist_ok=True)
                blocker.write_text("preserve")
                self.run_installer(home=home, success=False)
                self.assertFalse((home / ".claude").exists())
                self.assertEqual(blocker.read_text(), "preserve")

    def test_broken_destination_symlink_fails_before_install(self):
        blocker = self.home / ".agents"
        blocker.symlink_to(self.base / "missing")
        self.run_installer(success=False)
        self.assertTrue(blocker.is_symlink())
        self.assertFalse((self.home / ".claude").exists())

    def test_agent_configuration_and_unrelated_skills_are_untouched(self):
        files = [
            self.home / ".claude/settings.json",
            self.home / ".codex/config.toml",
            self.home / ".config/opencode/opencode.jsonc",
            self.home / ".agents/skills/unrelated/SKILL.md",
        ]
        for file in files:
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_text("preserve exactly")
        self.run_installer()
        self.run_installer("--uninstall")
        for file in files:
            self.assertEqual(file.read_text(), "preserve exactly")

    def test_uninstall_preserves_source_files(self):
        before = {
            file.relative_to(self.checkout): file.read_bytes()
            for file in self.checkout.rglob("*")
            if file.is_file()
        }
        self.run_installer()
        self.run_installer("--uninstall")
        for destination in DESTINATIONS:
            self.assertEqual(list((self.home / destination).iterdir()), [])
        for path, content in before.items():
            self.assertEqual((self.checkout / path).read_bytes(), content)

    def test_uninstall_removes_owned_links_to_deleted_skills(self):
        self.run_installer()
        shutil.rmtree(self.checkout / "skills/craft")
        self.run_installer("--uninstall")
        for destination in DESTINATIONS:
            self.assertFalse((self.home / destination / "craft").is_symlink())

    def test_uninstall_preserves_a_link_replaced_by_another_installation(self):
        self.run_installer()
        link = self.home / ".agents/skills/craft"
        link.unlink()
        foreign = self.base / "other-checkout/skills/craft"
        link.symlink_to(foreign)
        self.run_installer("--uninstall")
        self.assertEqual(link.readlink(), foreign)

    def test_uninstall_is_repeatable_and_does_not_create_directories(self):
        self.run_installer("--uninstall")
        self.assertEqual(list(self.home.iterdir()), [])
        self.run_installer()
        self.run_installer("--uninstall")
        self.run_installer("--uninstall")

    def test_help_and_invalid_arguments_do_not_install(self):
        self.assertIn("Usage:", self.run_installer("--help").stdout)
        for arguments in (("--unknown",), ("--uninstall", "extra")):
            self.assertEqual(self.run_installer(*arguments, success=False).returncode, 2)
        self.assertEqual(list(self.home.iterdir()), [])

    def test_invalid_home_is_rejected(self):
        for home in ("", "relative-home", self.base / "missing-home"):
            with self.subTest(home=home):
                self.assertIn("HOME must", self.run_installer(home=home, success=False).stderr)

    def test_empty_collection_does_not_install(self):
        shutil.rmtree(self.checkout / "skills")
        self.assertIn("No skills found", self.run_installer(success=False).stderr)
        self.assertEqual(list(self.home.iterdir()), [])

    def test_checkout_directory_alias_uses_the_physical_source(self):
        alias = self.base / "checkout-alias"
        alias.symlink_to(self.checkout)
        self.run_installer(script=alias / "install.sh")
        self.assert_installed()


if __name__ == "__main__":
    unittest.main()
