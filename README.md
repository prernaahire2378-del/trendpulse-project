# TrendPulse Project

## About the Project
This project is about working with real-world data step by step.  
I collected trending stories, cleaned the data, analyzed it, and then created charts to understand the trends.

---

## Task 1: Data Collection
In this step, I collected data from the Hacker News API.

- Fetched top stories
- Divided them into categories like:
  - Technology
  - World News
  - Sports
  - Science
  - Entertainment
- Tried to collect around 100+ stories

Then I saved the data in a JSON file.

Output file:
- trends_YYYYMMDD.json

---

## Task 2: Data Cleaning
Here I cleaned the raw data so it can be used properly.

- Loaded JSON into pandas DataFrame
- Removed duplicate stories
- Removed rows with missing values
- Converted score and comments into numbers
- Filtered out low quality stories (score < 5)
- Cleaned titles (removed extra spaces)

Output file:
- data/trends_clean.csv

---

## Task 3: Data Analysis
In this step, I analyzed the cleaned data.

- Calculated average score and comments
- Used NumPy to find:
  - mean
  - median
  - standard deviation
- Found:
  - which category has most stories
  - which story has most comments
- Added new columns:
  - engagement (based on score and comments)
  - is_popular (True/False)

Output file:
- data/trends_analysed.csv

---

## Task 4: Data Visualization
In the final step, I created charts using matplotlib.

Charts created:
1. Top 10 stories by score (horizontal bar chart)
2. Stories per category (bar chart)
3. Score vs comments (scatter plot)

Also created a dashboard combining all charts.

Output files:
- outputs/chart1_top_stories.png
- outputs/chart2_categories.png
- outputs/chart3_scatter.png
- outputs/dashboard.png

---

## Tools Used
- Python
- Pandas
- NumPy
- Matplotlib

---

## Project Structure

trendpulse-project/

task1_data_collection.py  
task2_data_processing.py  
task3_analysis.py  
task4_visualization.py  

data/  
  trends_clean.csv  
  trends_analysed.csv  

outputs/  
  chart1_top_stories.png  
  chart2_categories.png  
  chart3_scatter.png  
  dashboard.png  

README.md  

---

## Final Thoughts
This project helped me understand the full data pipeline:
collecting data → cleaning → analyzing → visualizing.

It also helped me understand how different types of stories perform based on score and comments.
