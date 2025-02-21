from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# Default match id if none is provided
DEFAULT_MATCH_ID = "3499012"

# Session cookie (used to bypass CORS via server-side fetch)
COOKIES = {
    "USSQ-API-SESSION": "s%3AnP8iOvjFv4N5MtnTsq2NikJ0DhzWUQAK.nDc6GCWcX6fO3ek%2FnAlrRf9WXQNfWbWivmwg9bAymqA"
}

@app.route("/")
def schedule():
    return render_template("test.html")

@app.route("/proxy/liveScoreDetails")
def proxy_live_score_details():
    # Get the match_id from the query parameter (or use default)
    match_id = request.args.get("match_id", DEFAULT_MATCH_ID)
    # Build the API URL dynamically based on match_id
    api_url = f"https://api.ussquash.com/resources/res/matches/{match_id}/liveScoreDetails"
    response = requests.get(api_url, cookies=COOKIES)
    if response.status_code != 200:
        return jsonify({"error": "Failed to retrieve data from API"}), response.status_code
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True, port=3000)
