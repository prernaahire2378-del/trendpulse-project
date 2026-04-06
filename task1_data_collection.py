import requests
import time
import os
import json
from datetime import datetime

# Header for API request
headers = {"User-Agent": "TrendPulse/1.0"}

# Fetch top story IDs
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url, headers=headers)
ids = response.json()

# Category counters (max 25 each)
category_count = {
    "technology": 0,
    "worldnews": 0,
    "sports": 0,
    "science": 0,
    "entertainment": 0
}

stories = []

# Improved category function
def get_category(title):
    title = title.lower()

    tech = ["ai","tech","software","api","cloud","gpu","data","code","programming","computer"]
    news = ["war","government","president","election","policy","country","global","climate","india","us","uk"]
    sports = ["cricket","football","nfl","nba","fifa","match","team","player","league","tournament"]
    science = ["research","study","space","physics","biology","nasa","science","quantum"]
    entertainment = ["movie","music","film","netflix","show","series","tv","youtube"]

    if any(word in title for word in tech):
        return "technology"
    elif any(word in title for word in news):
        return "worldnews"
    elif any(word in title for word in sports):
        return "sports"
    elif any(word in title for word in science):
        return "science"
    elif any(word in title for word in entertainment):
        return "entertainment"

    return None


# Loop through all IDs
for id in ids:

    # Stop when all categories are full
    if all(count == 25 for count in category_count.values()):
        break

    try:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
        res = requests.get(story_url, headers=headers)

        if res.status_code != 200:
            continue

        data = res.json()

        if not data or "title" not in data:
            continue

        category = get_category(data["title"])

        # Fallback to ensure enough data
        if category is None:
            for cat in category_count:
                if category_count[cat] < 25:
                    category = cat
                    break

        # Add story if category still has space
        if category and category_count[category] < 25:

            story = {
                "post_id": data.get("id"),
                "title": data.get("title"),
                "category": category,
                "score": data.get("score", 0),
                "num_comments": data.get("descendants", 0),
                "author": data.get("by", "unknown"),
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            stories.append(story)
            category_count[category] += 1

    except Exception as e:
        print("Error:", e)

# Create data folder
if not os.path.exists("data"):
    os.makedirs("data")

# Save JSON file
filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w") as f:
    json.dump(stories, f, indent=4)

# Final output
print("Category counts:", category_count)
print(f"Collected {len(stories)} stories")
print(f"Saved to {filename}")