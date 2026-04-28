import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv")

print("First 5 rows:")
print(df.head())

print("\nBasic Info:")
print(df.info())

# Data Cleaning
df.dropna(inplace=True)

# Example Analysis
print("\nTop Countries:")
print(df['country'].value_counts().head())

# Visualization
df['release_year'].value_counts().sort_index().plot(kind='line')
plt.title("Content Release Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()
