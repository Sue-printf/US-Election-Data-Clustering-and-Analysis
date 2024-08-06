# Import necessary libraries
import requests
import io
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Provided code for data collection - No changes needed here
URL = "https://en.wikipedia.org/wiki/List_of_United_States_presidential_election_results_by_state"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("table", {"class": "wikitable"})
df = pd.read_html(io.StringIO(str(results)))
df = pd.DataFrame(df[0])
df.columns = df.iloc[0, :].values
df.index = df.iloc[:, 0].values
election_df = df.iloc[1:53, 52:66].drop("State").dropna(axis=1)

# Part 1: Data Cleaning and Preparation
# Convert "D" and "R" to 0 and 1, respectively. Verify the data has been properly cleaned by printing the first five rows.
# Hint: Use the DataFrame.replace() method to replace "D" with 0 and "R" with 1. The inplace parameter might be useful here.
# Your code here:

# Part 2: Identifying Specific Subsets of States
# Find states that voted exclusively for one party across the given time period. Then, identify states with voting patterns identical to Illinois.
# Hint: For finding exclusive voting patterns, check for rows that contain all 1s or all 0s using the DataFrame.all() method along an axis.
# Hint: To compare states to Illinois, first get Illinois's voting pattern. Then use DataFrame.eq() to find matches.
# Your code here:

# Part 3: K-means Clustering Analysis with sklearn
# The objective here is to find an optimal number of clusters K using the elbow method, then apply K-means clustering.
# Step 1: Prepare your data for clustering, if not already in the correct format.
# Hint: KMeans needs numerical data. Ensure your DataFrame is ready for clustering.

# Step 2: Use the elbow method to find the optimal K.
# Hint 1: Initialize KMeans with varying values of K within a loop. Use n_clusters=k where k is the loop variable.
# Hint 2: Fit KMeans on your data (election_df) and calculate inertia (model.inertia_) for each K.
# Hint 3: Plot the inertia values against K to find the elbow point. This is your optimal K.

# Your code here for the elbow method:

# Step 3: Run K-means clustering with the optimal K found from the elbow method.
# Hint: With your chosen K, initialize KMeans and fit it on your data again. Use the labels_ attribute to assign cluster labels to your DataFrame.
# Your code here for K-means clustering:

# Part 4: Interpretation of Clusters
# Analyze the clusters to understand the political landscape they represent.
# Hint: Group your DataFrame by the new cluster labels and calculate means or counts to see the voting patterns within each cluster. What do these patterns suggest about each cluster's political preferences?
# Your code here:

