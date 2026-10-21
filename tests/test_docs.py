import tempfile
import unittest
from pathlib import Path

from scripts.check_docs import validate


class DocumentationChecks(unittest.TestCase):
    def test_valid_local_link(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'README.md').write_text('[Guide](guide.md)')
            (root / 'guide.md').write_text('# Guide')
            self.assertEqual(validate(root), [])

    def test_missing_link_fails(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'README.md').write_text('[Guide](missing.md)')
            self.assertTrue(validate(root))

    def test_private_artifacts_fail(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'credentials.json').write_text('{}')
            self.assertTrue(validate(root))

    def test_external_https_link_is_not_fetched(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'README.md').write_text('[Reference](https://example.invalid/)')
            self.assertEqual(validate(root), [])

    def test_absolute_file_link_fails(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'README.md').write_text('[Private](/private/file.md)')
            self.assertTrue(validate(root))

    def test_parent_escape_fails(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'README.md').write_text('[Private](../private.md)')
            self.assertTrue(validate(root))
