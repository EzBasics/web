import requests

url = "https://api.ussquash.com/resources/teams/40867/players"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                  'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                  'Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    players = response.json()
    
    # Sort players by "TeamPosition" (convert the string to int)
    sorted_players = sorted(players, key=lambda p: int(p["TeamPosition"]))
    
    for player in sorted_players:
        # Use .strip() to remove any trailing whitespace from the name
        print(f"Position: {player['TeamPosition']}, "
              f"Name: {player['player'].strip()}, "
              f"Rating: {player['Rating']}, "
              f"Wins: {player['wins']}, "
              f"Losses: {player['losses']}")
else:
    print("Failed to fetch players data")
