import requests

def test_api(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/58.0.3029.110 Safari/537.3"
        )
    }
    
    print(f"Testing API: {url}")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        print("Status Code:", response.status_code)
        if response.status_code == 200:
            try:
                data = response.json()
                print("JSON Response:")
                print(data)
            except Exception as json_error:
                print("Could not parse JSON:", json_error)
        else:
            print("API returned an error status.")
    except Exception as error:
        print("Error while testing API:", error)
    print("-" * 40)

def main():
    api_urls = [
        "https://api.ussquash.com/resources/teams/40867/info/",
        "https://api.ussquash.com/resources/teams/40867/players",
        "https://api.ussquash.com/resources/teams/40867/schedule"
    ]
    for url in api_urls:
        test_api(url)

if __name__ == "__main__":
    main()
