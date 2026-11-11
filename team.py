def validate_team_name(name: str) -> str:
    name = name.strip()
    if 2 <= len(name) <= 30:
        return name
    raise ValueError("Team name must be between 2 and 30 characters")    

