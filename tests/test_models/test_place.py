import unittest
import pathlib as pl
from os import getcwd

class TestFileExistance(unittest.TestCase):
    """
    Base test case to check if file is present

    ...

    Methods
    -------
    assertIsFile(path)
        Checks if a path exists, else raises an error

    test()
        Main test method that checks for intended file
    """
    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

    def test(self):
        path = pl.Path(f"{getcwd()}/models/place.py")
        self.assertIsFile(path)

