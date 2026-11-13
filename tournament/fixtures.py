def generate_fixtures(teams):
    fixtures = {}

    if len(teams) < 4 or len(teams) > 8:
        raise ValueError("Tournament must have between 4 and 8 teams")

    counter = 1
    match_id = f"M{counter:03d}"

    teams_id = list(teams.keys())

    for index, team_id in enumerate(teams_id):
        for opponent_id in teams_id[index + 1:]:
            print(team_id, "vs", opponent_id)

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

    