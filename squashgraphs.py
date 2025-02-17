import json
import matplotlib.pyplot as plt
from datetime import datetime

# Use a raw string for the file path to avoid escape issues
with open(r"C:\Users\solon\OneDrive\Desktop\liveScoreDetails.json", "r") as f:
    data = json.load(f)

# Filter records for events where a point was scored.
point_records = [record for record in data if record.get("Decision") == "point"]

# Group records by (Game_Number, PointIndex) so that duplicate events for the same rally are merged.
# We choose the record with the latest EndDate as the final outcome for that rally.
points_by_rally = {}
for record in point_records:
    key = (record.get("Game_Number"), record.get("PointIndex"))
    # Convert EndDate to datetime for comparison.
    end_date = datetime.fromisoformat(record["EndDate"].replace("Z", "+00:00"))
    if key not in points_by_rally:
        points_by_rally[key] = record
    else:
        existing_end_date = datetime.fromisoformat(points_by_rally[key]["EndDate"].replace("Z", "+00:00"))
        if end_date > existing_end_date:
            points_by_rally[key] = record

unique_points = list(points_by_rally.values())

# Count points by serving side.
# We assume that if Serving_Side is "R", then that rally is won when serving on the right;
# likewise for "L".
counts = {"R": 0, "L": 0}
for record in unique_points:
    serving = record.get("Serving_Side", "").strip()
    if serving in counts:
        counts[serving] += 1

print("Points won when serving on the Right:", counts["R"])
print("Points won when serving on the Left:", counts["L"])

# Create a bar chart comparing the two counts.
sides = list(counts.keys())
points_won = [counts[side] for side in sides]

plt.figure(figsize=(8, 6))
plt.bar(sides, points_won, color=["blue", "green"])
plt.xlabel("Serving Side")
plt.ylabel("Points Won")
plt.title("Points Won by Serving Side")
for i, value in enumerate(points_won):
    plt.text(i, value, str(value), ha="center", va="bottom")
plt.tight_layout()
plt.show()