import unittest
from tournament.fixtures import generate_fixtures

class TestFixturesGeneration(unittest.TestCase):
    def setUp(self):

        self.teams_3 = {
        "TM001": {"id": "TM001", "name": "Red Comets"},
        "TM002": {"id": "TM002", "name": "Blue Hawks"},
        "TM003": {"id": "TM003", "name": "Golden Eagles"},
        }
        self.teams_4 = {
        "TM001": {"id": "TM001", "name": "Red Comets"},
        "TM002": {"id": "TM002", "name": "Blue Hawks"},
        "TM003": {"id": "TM003", "name": "Golden Eagles"},
        "TM004": {"id": "TM004", "name": "Black Panthers"}
        }
        self.teams_5 = {
        "TM001": {"id": "TM001", "name": "Red Comets"},
        "TM002": {"id": "TM002", "name": "Blue Hawks"},
        "TM003": {"id": "TM003", "name": "Golden Eagles"},
        "TM004": {"id": "TM004", "name": "Black Panthers"},
        "TM005": {"id": "TM005", "name": "Silver Wolves"}
        }

        self.teams_9 = {
        "TM001": {"id": "TM001", "name": "Red Comets"},
        "TM002": {"id": "TM002", "name": "Blue Hawks"},
        "TM003": {"id": "TM003", "name": "Golden Eagles"},
        "TM004": {"id": "TM004", "name": "Black Panthers"},
        "TM005": {"id": "TM005", "name": "Silver Wolves"},
        "TM006": {"id": "TM006", "name": "Red Devils"},
        "TM007": {"id": "TM007", "name": "Super Eagles"},
        "TM008": {"id": "TM008", "name": "Flying Eagles"},
        "TM009": {"id": "TM009", "name": "The Buffalos"}   
        }

    def test_fixtures_generation_4_teams(self):
        self.assertEqual(len(generate_fixtures(self.teams_4)), 6)
    
    def test_fixtures_generation_5_teams(self):
        self.assertEqual(len(generate_fixtures(self.teams_5)), 10)

    def test_fixtures_generation_invalid_3_teams(self):
        with self.assertRaises(ValueError):
            generate_fixtures(self.teams_3)

    def test_fixtures_generation_invalid_9_teams(self):
        with self.assertRaises(ValueError):
            generate_fixtures(self.teams_9)

