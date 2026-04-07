# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 1: Load data

# Load analysed CSV from Task 3
df = pd.read_csv("data/trends_analysed.csv")

print("Data loaded:", df.shape)

# Create outputs folder if not exists
os.makedirs("outputs", exist_ok=True)

# Step 2: Chart 1 - Top 10 stories by score

# Sort data by score and take top 10
top10 = df.sort_values(by="score", ascending=False).head(10)

# Shorten long titles (max 50 characters)
top10["short_title"] = top10["title"].apply(lambda x: x[:50])

plt.figure()
plt.barh(top10["short_title"], top10["score"])
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")

# Save chart
plt.savefig("outputs/chart1_top_stories.png")
plt.show()

# Step 3: Chart 2 - Stories per category

category_counts = df["category"].value_counts()

plt.figure()
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

# Save chart
plt.savefig("outputs/chart2_categories.png")
plt.show()

# Step 4: Chart 3 - Scatter plot

# Separate popular and non-popular stories
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.figure()

# Plot both groups
plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()

# Save chart
plt.savefig("outputs/chart3_scatter.png")
plt.show()

# Bonus: Dashboard (all charts together)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Chart 1 in dashboard
axes[0].barh(top10["short_title"], top10["score"])
axes[0].set_title("Top Stories")

# Chart 2 in dashboard
axes[1].bar(category_counts.index, category_counts.values)
axes[1].set_title("Categories")

# Chart 3 in dashboard
axes[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axes[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axes[2].set_title("Score vs Comments")
axes[2].legend()

# Overall title
plt.suptitle("TrendPulse Dashboard")

# Save dashboard
plt.savefig("outputs/dashboard.png")
plt.show()

print("\nAll charts saved in outputs folder")