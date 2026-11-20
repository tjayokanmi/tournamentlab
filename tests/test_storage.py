from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from  tournament.storage import save_tournament

class TestDataStorage(unittest.TestCase):
    def test_save_tournament(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            filepath = Path(tmp_dir)

        