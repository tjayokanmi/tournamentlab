import unittest
from tournament.fixtures import generate_fixtures, record_result
from copy import deepcopy


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

    def test_no_duplicate_pairings(self):
        fixtures = generate_fixtures(self.teams_4)
        seen_pairs = set()

        for fixture in fixtures.values():
            home_id = fixture["home_id"]
            away_id = fixture["away_id"]

            self.assertNotEqual(home_id, away_id)

            pair = tuple(sorted((home_id, away_id)))

            self.assertNotIn(pair, seen_pairs)

            seen_pairs.add(pair)

    def test_fixtures_generation_dictionary(self):
        copied = self.teams_4.copy()

        generate_fixtures(self.teams_4)

        self.assertEqual(self.teams_4, copied)

class TestRecordResult(unittest.TestCase):
    def setUp(self):
        self.fixtures = {
    "M001": {
        "id": "M001",
        "home_id": "TM001",
        "away_id": "TM002",
        "status": "pending",
        "home_score": None,
        "away_score": None
    },
    "M002": {
        "id": "M002",
        "home_id": "TM001",
        "away_id": "TM003",
        "status": "cancelled",
        "home_score": None,
        "away_score": None
    },
    "M003": {
        "id": "M003",
        "home_id": "TM002",
        "away_id": "TM003",
        "status": "played",
        "home_score": 2,
        "away_score": 1
    }
}

    def test_record_result_already_played(self):
        copied = deepcopy(self.fixtures)

        with self.assertRaises(ValueError):
            record_result(self.fixtures, "M003", 2, 1)

        self.assertEqual(self.fixtures, copied)


    def test_record_result_negative_home_score(self):
        with self.assertRaises(ValueError):
            record_result(self.fixtures,"M001",-1, 2)

    def test_record_result_negative_away_score(self):
        with self.assertRaises(ValueError):
            record_result(self.fixtures, "M001", 2,-1)
    
    def test_record_result_float_score(self):
        with self.assertRaises(ValueError):
            record_result(self.fixtures, "M001", 2.5, 1)

    def test_record_result_string_score(self):
        with self.assertRaises(ValueError):
            record_result(self.fixtures,"M001", "2", 1)

    def test_record_result_boolean_score(self):
        with self.assertRaises(ValueError):
            record_result(self.fixtures, "M001", True, 1)

    def test_record_result_nonexistent_fixture(self):
        with self.assertRaises(ValueError):
            record_result(self.fixtures, "M999", 2, 1)
    
    def test_record_result_invalid_result(self):
        copied = deepcopy(self.fixtures)
        with self.assertRaises(ValueError):
            record_result(self.fixtures, "M001", 3, -1)

        self.assertEqual(self.fixtures,copied)

    def test_record_result_cancelled_match(self):
        with self.assertRaises(ValueError):
            record_result(self.fixtures, "M002", 2, 1)