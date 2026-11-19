from tournament.standings import calculate_standings
import unittest  

class TestCalculateStandings(unittest.TestCase):
    def setUp(self):
        self.teams = {
            "TM001" : {"id": "TM001", "name" : "Red Comets"},
            "TM002" : {"id": "TM002", "name" : "Blue Hawks"},
            "TM003" : {"id": "TM003", "name" : "Golden Eagles"},
            "TM004" : {"id": "TM004", "name" : "Black Panthers"}
        }

        self.fixtures = {}

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
            


