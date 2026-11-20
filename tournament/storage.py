import json 
from pathlib import Path


def save_tournament(teams, fixtures, filepath):

    filepath = Path(filepath)

    tournament_data = {
        "teams": teams,
        "fixtures": fixtures
    }

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(tournament_data, file, indent=4)
