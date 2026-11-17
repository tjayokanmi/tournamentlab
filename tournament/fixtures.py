def generate_fixtures(teams):
    fixtures = {}

    if len(teams) < 4 or len(teams) > 8:
        raise ValueError("Tournament must have between 4 and 8 teams")

    counter = 1
    

    teams_id = list(teams.keys())

    for index, team_id in enumerate(teams_id):
        for opponent_id in teams_id[index + 1:]:
            match_id = f"M{counter:03d}"

            fixture = {
                "id" : match_id,
                "home_id" : team_id,
                "away_id" : opponent_id,
                "status" : "pending",
                "home_score" : None,
                "away_score" : None
            }
            fixtures[match_id] = fixture
            counter += 1
    return fixtures

    
def record_result(fixtures, fixture_id, home_score, away_score):
    if fixture_id not in fixtures: 
        raise ValueError("Fixture does not exist")
    if fixtures[fixture_id]["status"] == "played":
        raise ValueError("Fixture has already been played")    

    if not (
        type(home_score) is int and 
        type(away_score) is int and 
        home_score >= 0 and 
        away_score >= 0
    ):              
        raise ValueError("Enter a valid number for the scores")
        
    fixtures[fixture_id]["home_score"] = home_score
    fixtures[fixture_id]["away_score"] = away_score
    fixtures[fixture_id]["status"] = "played"