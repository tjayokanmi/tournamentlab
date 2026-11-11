import unittest 
from tournament.teams import validate_team_name

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