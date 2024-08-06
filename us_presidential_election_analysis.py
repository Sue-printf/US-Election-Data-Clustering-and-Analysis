# Import necessary libraries
import requests
import io
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


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

election_df.replace({"D": 0, "R": 1}, inplace=True)
print("Cleaned Dataset:")
print(election_df.head())

# Part 2: Identifying Specific Subsets of States
# Find states that voted exclusively Republican, exclusively Democratic, and those that voted exactly the same as Illinois.

# Find states that voted exclusively Republican
republican_states = election_df[election_df.all(axis=1)]
print("\nStates that voted exclusively Republican:")
print(republican_states)

# Find states that voted exclusively Democratic
democratic_states = election_df[(election_df == 0).all(axis=1)]
print("\nStates that voted exclusively Democratic:")
print(democratic_states)

# Find states that voted exactly the same as Illinois
illinois_pattern = election_df.loc["Illinois"]
same_as_illinois = election_df[election_df.eq(illinois_pattern).all(axis=1)]
print("\nStates that voted exactly the same as Illinois:")
print(same_as_illinois)

# Part 3: K-means Clustering Analysis with sklearn

# Initialize lists to store inertia values and K values
inertia_values = []
k_values = []

# Try multiple values of K
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, n_init=10, random_state=0)
    kmeans.fit(election_df)
    inertia_values.append(kmeans.inertia_)
    k_values.append(k)

# Plot the inertia values against K to find the elbow point
plt.plot(k_values, inertia_values, marker='o')
plt.xlabel('Number of clusters (K)')
plt.ylabel('Total within-cluster variance')
plt.title('Elbow Method for Optimal K')
plt.show()

# Run K-means clustering with the optimal K
optimal_k = 3  # Assume the optimal K is 3 based on the elbow method

kmeans = KMeans(n_clusters=optimal_k, n_init=10, random_state=0)


# Fit KMeans on your data again
kmeans.fit(election_df)

# Assign cluster labels to your DataFrame
election_df['Cluster'] = kmeans.labels_
print("\nClustering results:")
print(election_df)

# Part 4: Interpretation of Clusters

# Analyze the clusters to understand the political landscape they represent.
# Group your DataFrame by the new cluster labels and calculate means or counts to see the voting patterns within each cluster.

cluster_analysis = election_df.groupby('Cluster').mean()
print("\nCluster analysis:")
print(cluster_analysis)