def calculate_standings(teams, fixtures):
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

        home_id = fixture["home_id"]
        away_id = fixture["away_id"]
        home_score = fixture["home_score"]
        away_score = fixture["away_score"]
        
        
        standing[home_id]['MP'] += 1
        standing[away_id]['MP'] += 1
        standing[home_id]['GF'] += home_score
        standing[home_id]['GA'] += away_score
        standing[away_id]['GF'] += away_score
        standing[away_id]['GA'] += home_score
        

        if home_score > away_score:
            standing[home_id]['Pts'] += 3
           
            standing[home_id]['W'] += 1
            standing[away_id]['L'] += 1



        elif home_score == away_score:
            standing[home_id]['Pts'] += 1
            standing[away_id]['Pts'] += 1
            standing[home_id]['D'] += 1
            standing[away_id]['D'] += 1
                    
        else:
            standing[away_id]['Pts'] += 3
            standing[home_id]['L'] += 1
            standing[away_id]['W'] += 1
        
    for team_id, team in standing.items():
        team['GD'] = team['GF'] - team['GA']

    ranked_standings = sorted(
            standing.values(),
            key=lambda team: (
                -team["Pts"],
                -team["GD"],
                -team["GF"],
                team["name"].casefold()
            )
        )
            
    return ranked_standings