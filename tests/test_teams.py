import unittest
from tournament.teams import validate_team_name, is_duplicate_team_name, generate_team_id, register_team



class TestValidateTeamName(unittest.TestCase):

    def test_valid_team_name(self):
        self.assertEqual(
            validate_team_name("Red Comets"),
            "Red Comets"
        )

    def test_whitespace_team_name(self):
        self.assertEqual(
            validate_team_name("   Red Comets       "),
            "Red Comets"
        )

    def test_exactly_maximum_character_team_name(self):
        self.assertEqual(
            validate_team_name("Manchester Manchester Uniteded"),
            "Manchester Manchester Uniteded"
        )
    def test_invalid_one_character_team_name(self):
        with self.assertRaises(ValueError):
            validate_team_name("R")

    def test_whitespace_only_team_name(self):
        with self.assertRaises(ValueError):
            validate_team_name("   ")
    
    def test_team_name_exceeds_maximum_length(self):
        with self.assertRaises(ValueError):
            validate_team_name("Manchester United Juventus Bayern Munchen")

class TestIsDuplicateTeamName(unittest.TestCase):
        
    def setUp(self):
        self.teams = {
            "TM001": {"id": "TM001", "name": "Red Comets"},
            "TM002": {"id": "TM002", "name": "Blue Hawks"}
        }
    
    def test_existing_team_name_is_duplicate(self):
        self.assertTrue(is_duplicate_team_name("Red Comets", self.teams)
        )

    def test_existing_team_name_is_duplicate_lowercase(self):
        self.assertTrue(is_duplicate_team_name("red comets", self.teams))

    def test_existing_team_name_is_duplicate_uppercase(self):
        self.assertTrue(is_duplicate_team_name("RED COMETS", self.teams))

    
    def test_existing_team_name_is_duplicate_whitespace(self):
        self.assertTrue(is_duplicate_team_name("  Red Comets   ", self.teams)
        )

    def test_existing_team_name_is_duplicate_unique_name(self):
        self.assertFalse(is_duplicate_team_name("Yellow Lions", self.teams))

class TestGenerateNewID(unittest.TestCase):
    def setUp(self):
        self.teams = {
            "TM001": {"id": "TM001", "name": "Red Comets"},
            "TM002": {"id": "TM002", "name": "Blue Hawks"}
        }
        self.empty = {}

        self.teams1 = {
            "TM003": {"id": "TM003", "name": "Red Comets"},
            "TM009": {"id": "TM009", "name": "Blue Hawks"},
            "TM012": {"id": "TM012", "name": "Green Giants"}
        }

    def test_generate_new_id_empty(self):
        self.assertEqual(generate_team_id(self.empty), "TM001")

    def test_generate_team_id_existing_id(self):
        self.assertEqual(generate_team_id(self.teams), "TM003")
    
    def test_generate_team_id_uses_highest_existing_id(self):
        self.assertEqual(generate_team_id(self.teams1), "TM013")



class TestRegisterTeam(unittest.TestCase):
    def setUp(self):
        self.teams = {
            "TM001": {"id": "TM001", "name": "Red Comets"},
            "TM002": {"id": "TM002", "name": "Blue Hawks"}
        }

        self.empty = {}

    def test_register_new_team(self):
        self.assertEqual(register_team("Yellow Lions", self.teams), {"id" : "TM003", "name" : "Yellow Lions"})
        self.assertIn("TM003", self.teams)
    
    def test_register_new_team_empty_dic(self):
        self.assertEqual(register_team("Yellow Lions", self.empty), {"id" : "TM001", "name" : "Yellow Lions"})
        self.assertIn("TM001", self.empty)

    def test_duplicate_register_team(self):
        original_teams = self.teams.copy()
        with self.assertRaises(ValueError):
            register_team("Red Comets", self.teams)
        
        self.assertEqual(self.teams, original_teams)


    def test_register_invalid_team(self):
        original_teams = self.teams.copy()
        with self.assertRaises(ValueError):
            register_team("R", self.teams)
        
        self.assertEqual(self.teams, original_teams)
