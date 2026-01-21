import requests
import json
import time

def season_get_game_id(start_date, end_date):
    base_url ="https://api-web.nhle.com/v1/schedule/"
    current_date = start_date
    all_game_ids = []

    while current_date < end_date:
        url = f"{base_url}{current_date}"

        try:
            response = requests.get(url)
            data = response.json()
        except Exception as e:
            print("Error")
            break

        for day in data.get("gameWeek", []):
            for game in day.get("games", []):
                if game.get("gameType") == 2:
                    all_game_ids.append(game["id"])

        next_date = data.get("nextStartDate")

        if not next_date or current_date >= end_date:
            break

        current_date = next_date

        time.sleep(0.5)

    return all_game_ids



"""
url = "https://api-web.nhle.com/v1/schedule/2024-01-20"
url2 = "https://api-web.nhle.com/v1/gamecenter/2023020204/boxscore"

response = requests.get(url)
response2 = requests.get(url2)


data = response.json()["gameWeek"]


print(response2.json())
"""

season_start_22 = "2022-10-07"
season_end_22 = "2023-06-13"


season_start_23 = "2023-10-10"
season_end_23 = "2024-06-24"

season_start_24 = "2024-10-04"
season_end_24 = "2025-06-17"

game_ids_2022 = season_get_game_id(season_start_22, season_end_22)
game_ids_2023 = season_get_game_id(season_start_23, season_end_23)
game_ids_2024 = season_get_game_id(season_start_24, season_end_24)


with open("season_2022_ids.json", "w") as f:
    json.dump(game_ids_2022, f)

with open("season_2023_ids.json", "w") as f:
    json.dump(game_ids_2023, f)

with open("season_2024_ids.json", "w") as f:
    json.dump(game_ids_2024, f)

print(len(game_ids_2022))
print(len(game_ids_2023))
print(len(game_ids_2024))
