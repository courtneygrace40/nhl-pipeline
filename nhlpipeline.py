import requests

url = "https://api-web.nhle.com/v1/schedule/2024-01-20"
url2 = "https://api-web.nhle.com/v1/game/2023020706/boxscore"

response = requests.get(url)
response2 = requests.get(url2)


data = response.json()["gameWeek"]


print(response2.json())





