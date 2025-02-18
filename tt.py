import json
import matplotlib.pyplot as plt
from datetime import datetime

# -- LOAD DATA --
with open(r"C:\Users\solon\Downloads\test2.json", "r") as f:
    data = json.load(f)

# -- FILTER ONLY SCORING EVENTS FOR GAME 1 --
points_game1 = [
    event for event in data
    if event.get("Decision") == "point" and event.get("Game_Number") == 1
]

if not points_game1:
    print("No 'point' events found for Game 1.")
    exit()

# -- SORT BY StartDate --
points_game1.sort(
    key=lambda e: datetime.fromisoformat(e["StartDate"].replace("Z", "+00:00"))
)

# -- PREPARE DATA --
x = [evt["Points_left"] + evt["Points_right"] for evt in points_game1]
p1_scores = [evt["Points_left"]  for evt in points_game1]
p2_scores = [evt["Points_right"] for evt in points_game1]

player1_name = "Harrison Yang"
player2_name = "Alejandro Moncada Gonzalez"

# -- CREATE FIGURE --
fig, ax = plt.subplots(figsize=(8, 6))

# -- PLOT LINES & MARKERS --
ax.plot(x, p1_scores, marker="o", color="red",  label=player1_name)
ax.plot(x, p2_scores, marker="o", color="blue", label=player2_name)

# -- TITLE & LABELS --
ax.set_title("Match Insights", fontsize=14, pad=12)
ax.set_xlabel("Points Played")
ax.set_ylabel("Score")

# -- AXIS LIMITS --
max_x = max(x) if x else 0  # handle empty case gracefully
max_score = max(max(p1_scores), max(p2_scores)) if p1_scores else 0
ax.set_xlim(left=0, right=max_x + 1)
ax.set_ylim(bottom=0, top=max_score + 1)

# -- MAKE X-AXIS TICKS COUNT BY 2 --
ax.set_xticks(range(0, max_x + 2, 2))  # step of 2

# -- GRID & SPINES --
ax.grid(True, which="major", axis="both", color="0.8", alpha=0.5)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# -- LEGEND & LAYOUT --
ax.legend(loc="upper left")
plt.tight_layout()
plt.show()
