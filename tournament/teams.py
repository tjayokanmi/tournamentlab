def validate_team_name(name: str) -> str:
    name = name.strip()
    if 2 <= len(name) <= 30:
        return name
    raise ValueError("Team name must be between 2 and 30 characters")    

teams = {
    "TM001": {"id": "TM001", "name": "Red Comets"},
    "TM002": {"id": "TM002", "name": "Blue Hawks"}
}

def is_duplicate_team_name(name: str, teams: dict) -> bool:
    name = name.strip()
    for team in teams.values():
        if name.casefold() == team["name"].casefold():
            return True
    return False


def generate_team_id(teams):
    teams_store = []

    if len(teams) == 0:
        return "TM001"
    
    for team in teams:
        team_num = team[2:]
        
        teams_store.append(int(team_num))
    
    highest = max(teams_store) + 1
    return f"TM{highest:03d}"
