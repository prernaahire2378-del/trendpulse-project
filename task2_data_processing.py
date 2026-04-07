# Import required libraries
import pandas as pd
import json

# Step 1: Load the JSON file
# This file should be in the same folder as your script or Colab
with open("trends_20260406.json", "r") as file:
    data = json.load(file)

# Step 2: Convert JSON data into a DataFrame
df = pd.DataFrame(data)

# Print how many stories were loaded initially
print("Total stories loaded:", len(df))


# Step 3: Remove duplicate stories
# We use 'post_id' because it should be unique for each story
df = df.drop_duplicates(subset="post_id")


# Step 4: Remove rows with missing important values
# If any of these fields are missing, the row is not useful
df = df.dropna(subset=["post_id", "title", "score"])


# Step 5: Fix data types
# Convert score and number of comments into integers
df["score"] = df["score"].astype(int)

# Some stories may not have comments, so fill missing with 0
df["num_comments"] = df["num_comments"].fillna(0).astype(int)


# Step 6: Filter out low-quality stories
# Keep only stories with score >= 5
df = df[df["score"] >= 5]


# Step 7: Clean the title text
# Remove extra spaces from beginning and end
df["title"] = df["title"].str.strip()


# Step 8: Save cleaned data into a CSV file
output_file = "trends_clean.csv"
df.to_csv(output_file, index=False)


# Step 9: Print final results
print("Final cleaned stories:", len(df))
print("Clean file saved as:", output_file)


# Step 10: Show category-wise distribution
print("\nStories per category:")
print(df["category"].value_counts())

# -------- FINAL SUMMARY --------

print("\n----- FINAL SUMMARY -----")

# Total stories after cleaning
print("Total cleaned stories:", len(df))

# Category-wise count
print("\nStories per category:")
print(df["category"].value_counts())

# Average score per category
print("\nAverage score per category:")
print(df.groupby("category")["score"].mean())

# Top 3 highest scored stories
print("\nTop 3 highest scored stories:")
top3 = df.sort_values(by="score", ascending=False).head(3)
print(top3[["title", "score"]])


