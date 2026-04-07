# Import libraries
import pandas as pd
import numpy as np
import os

# Load CSV file (make sure file is uploaded in Colab)
df = pd.read_csv("trends_clean.csv")

# Check data
print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# Calculate averages
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print("\nAverage score:", int(avg_score))
print("Average comments:", int(avg_comments))

# NumPy calculations
scores = df["score"].values

print("\n--- Stats ---")
print("Mean:", int(np.mean(scores)))
print("Median:", int(np.median(scores)))
print("Std:", int(np.std(scores)))
print("Max:", int(np.max(scores)))
print("Min:", int(np.min(scores)))

# Category with most stories
top_cat = df["category"].value_counts().idxmax()
count = df["category"].value_counts().max()

print("\nMost stories in:", top_cat, "(", count, ")")

# Most commented story
row = df.loc[df["num_comments"].idxmax()]
print("\nMost commented story:")
print(row["title"], "-", row["num_comments"], "comments")

# Add new columns
df["engagement"] = df["num_comments"] / (df["score"] + 1)
df["is_popular"] = df["score"] > avg_score

# Create folder and save file
os.makedirs("data", exist_ok=True)

output_path = "data/trends_analysed.csv"
df.to_csv(output_path, index=False)

print("\nFile saved successfully at:", output_path)