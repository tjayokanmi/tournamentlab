from tournament.standings import calculate_standings
import unittest  
from copy import deepcopy

class TestCalculateStandings(unittest.TestCase):
    def setUp(self):
        self.teams = {
            "TM001" : {"id": "TM001", "name" : "Red Comets"},
            "TM002" : {"id": "TM002", "name" : "Blue Hawks"},
            "TM003" : {"id": "TM003", "name" : "Golden Eagles"},
            "TM004" : {"id": "TM004", "name" : "Black Panthers"}
        }

        self.fixtures = {}
        self.fixtures1 = {
            "M001": {
                "id": "M001",
                "home_id": "TM001",
                "away_id": "TM002",
                "status": "played",
                "home_score": 3,
                "away_score": 1
            },
            "M002": {
                "id": "M002",
                "home_id": "TM001",
                "away_id": "TM003",
                "status": "played",
                "home_score": 2,
                "away_score": 2
            },
            "M003": {
                "id": "M003",
                "home_id": "TM002",
                "away_id": "TM003",
                "status": "played",
                "home_score": 0,
                "away_score": 2
            }
        }

    def test_calculate_standings(self):
        results = calculate_standings(self.teams, self.fixtures)
        expected_stats = {
            "MP": 0,
            "W": 0,
            "D": 0,
            "L": 0,
            "GF": 0,
            "GA": 0,
            "GD": 0,
            "Pts": 0
        }        
        self.assertEqual(len(results), 4)
        
        for team in results:
            for stat, expected_value in expected_stats.items():
                self.assertEqual(team[stat], expected_value)

    def test_calculate_standings_with_results(self):
        results = calculate_standings(self.teams, self.fixtures1)

        expected = {
            "TM001": {
                "MP": 2, "W": 1, "D": 1, "L": 0,
                "GF": 5, "GA": 3, "GD": 2, "Pts": 4
            },
            "TM002": {
                "MP": 2, "W": 0, "D": 0, "L": 2,
                "GF": 1, "GA": 5, "GD": -4, "Pts": 0
            },
            "TM003": {
                "MP": 2, "W": 1, "D": 1, "L": 0,
                "GF": 4, "GA": 2, "GD": 2, "Pts": 4
            },
            "TM004": {
                "MP": 0, "W": 0, "D": 0, "L": 0,
                "GF": 0, "GA": 0, "GD": 0, "Pts": 0
            }
        }

        results_by_id = {team["id"]: team for team in results}

        for team_id, stats in expected.items():
            for stat, expected_value in stats.items():
                self.assertEqual(results_by_id[team_id][stat], expected_value)

    def test_standings_ranking(self):
        fixtures = {
            "M001": {
                "id": "M001",
                "home_id": "TM001",
                "away_id": "TM002",
                "status": "played",
                "home_score": 3,
                "away_score": 1
            },
            "M002": {
                "id": "M002",
                "home_id": "TM003",
                "away_id": "TM004",
                "status": "played",
                "home_score": 2,
                "away_score": 0
            },
            "M003": {
                "id": "M003",
                "home_id": "TM001",
                "away_id": "TM003",
                "status": "played",
                "home_score": 1,
                "away_score": 0
            },
            "M004": {
                "id": "M004",
                "home_id": "TM002",
                "away_id": "TM004",
                "status": "played",
                "home_score": 2,
                "away_score": 0
            }
        }

        results = calculate_standings(self.teams, fixtures)

        actual_order = [team["id"] for team in results]

        expected_order = ["TM001", "TM003", "TM002", "TM004"]

        self.assertEqual(actual_order, expected_order)

    def test_standings_alphabetical_tiebreaker(self):
        fixtures = {
            "M001": {
                "id": "M001",
                "home_id": "TM001",
                "away_id": "TM002",
                "status": "played",
                "home_score": 0,
                "away_score": 0
            },
            "M002": {
                "id": "M002",
                "home_id": "TM003",
                "away_id": "TM004",
                "status": "played",
                "home_score": 0,
                "away_score": 0
            }
        }

        results = calculate_standings(self.teams, fixtures)

        actual_order = [team["name"] for team in results]

        expected_order = [
            "Black Panthers",
            "Blue Hawks",
            "Golden Eagles",
            "Red Comets"
        ]

        self.assertEqual(actual_order, expected_order)

    def test_pending_fixtures_are_ignored(self):
        pending_fixtures = {
            "M001": {
                "id": "M001",
                "home_id": "TM001",
                "away_id": "TM002",
                "status": "pending",
                "home_score": None,
                "away_score": None
            }
        }

        results = calculate_standings(self.teams, pending_fixtures)

        expected_stats = {
            "MP": 0,
            "W": 0,
            "D": 0,
            "L": 0,
            "GF": 0,
            "GA": 0,
            "GD": 0,
            "Pts": 0
        }

        for team in results:
            for stat, expected_value in expected_stats.items():
                self.assertEqual(team[stat], expected_value)

    def test_calculate_standings_does_not_modify_inputs(self):
        original_teams = deepcopy(self.teams)
        original_fixtures = deepcopy(self.fixtures1)

        calculate_standings(self.teams, self.fixtures1)

        self.assertEqual(self.teams, original_teams)
        self.assertEqual(self.fixtures1, original_fixtures)