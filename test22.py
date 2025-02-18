import requests

# URL for the match
match_id = "3499012"
url = f"https://api.ussquash.com/resources/res/matches/{match_id}/liveScoreDetails"

# Cookies from your browser
cookies = {
    "USSQ-API-SESSION": "s%3A2KCwXNuxA-R2GwhridQ7iVahv1J5aKQk.5hb8uDyRv6%2FvkSl2bKgkMsayoLZNX4Knp3SlOeYuG0E"
}

# Headers (to mimic a real browser)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Referer": "https://www.ussquash.com/"  # Adjust if needed
}

# Make the request
response = requests.get(url, headers=headers, cookies=cookies)

# Print the response
if response.status_code == 200:
    print(response.json())  # Successfully retrieved data
else:
    print(f"Error {response.status_code}: {response.text}")
