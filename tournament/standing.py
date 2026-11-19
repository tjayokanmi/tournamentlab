def calculate_standings(teams, fixtures):
    teams = {
    "TM001": {"id": "TM001", "name": "Red Comets"},
    "TM002": {"id": "TM002", "name": "Blue Hawks"}
}

    fixtures = {
    "M001": {
        "id": "M001",
        "home_id": "TM001",
        "away_id": "TM002",
        "status": "pending",
        "home_score": None,
        "away_score": None
    }
}
        
    standing = {}
    for team_id, team  in teams.items():
        standing[team_id] = {
            "id": team["id"],
            "name": team["name"],
            "MP": 0,
            "W": 0,
            "D": 0,
            "L": 0,
            "GF": 0,
            "GA": 0,
            "GD": 0,
            "Pts": 0
        }

    for fixture_id, fixture in fixtures.items():
        if fixture["status"] != "played":
            continue

    return standing