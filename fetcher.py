import json 
import pprint
import requests
import time

with open('season_2022_ids.json') as f:
    season_2022_ids = json.load(f)

with open('season_2023_ids.json') as f:
    season_2023_ids = json.load(f)

with open('season_2024_ids.json') as f:
    season_2024_ids = json.load(f)
    

def get_game_info(season_ids, year):
    base_url = f"https://api-web.nhle.com/v1/gamecenter/"

    with open(f"all_games{year}.jsonl", "a") as f:
        for gameID in season_ids:
            url = f"{base_url}{gameID}/landing"
            try:
                response = requests.get(url)
                data = response.json()
                f.write(json.dumps(data) + "\n")
            except Exception as e:
                print("Error")
                break
            time.sleep(0.5)
        

get_game_info(season_2022_ids, "2022")

    

      
