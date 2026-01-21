import json
import pprint

# Load just the first line of your 2022 file
with open('all_games2022.jsonl', 'r') as f:
    first_line = f.readline()
    data = json.loads(first_line)

print("--- TOP LEVEL KEYS ---")
print(data.keys())



print("\n--- HOME TEAM KEYS (Example) ---")
# I'm guessing 'homeTeam' exists. If this errors, we'll know!
if 'summary' in data:
    pprint.pprint(data['summary'])
else:
    print("Could not find 'homeTeam'. keys are:", data.keys())