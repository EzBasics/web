import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Use a nicer style (ggplot is available by default)
plt.style.use("ggplot")

# URL for the user's rating history
url = "https://api.ussquash.com/resources/res/user/170053/ratings_history"

# Fetch the JSON data from the API
response = requests.get(url)
data = response.json()

# Parse dates and ratings from the JSON data
dates = []
ratings = []
for entry in data:
    # Convert the ISO date string to a datetime object
    dt = datetime.fromisoformat(entry["RankingPeriod"])
    dates.append(dt)
    ratings.append(entry["NewRating"])

# Ensure data is sorted chronologically
dates, ratings = zip(*sorted(zip(dates, ratings)))

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(dates, ratings, marker='o', linestyle='-', color='darkblue', markersize=8, linewidth=2)

# Set titles and labels with increased font sizes for clarity
ax.set_title("User Ratings History", fontsize=20, fontweight='bold', pad=20)
ax.set_xlabel("Date", fontsize=14)
ax.set_ylabel("Rating", fontsize=14)

# Improve the x-axis date formatting
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45)

# Customize grid appearance
ax.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
