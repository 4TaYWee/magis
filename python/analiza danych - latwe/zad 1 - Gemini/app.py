import pandas as pd

# Specify the path to your CSV file
file_path = "your_data.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Get basic statistics for all numerical columns
print(df.describe(include='all'))

# Get specific statistics for a particular column (e.g., mean, median, standard deviation)
column_name = "your_column_name"
print("Mean of", column_name, ":", df[column_name].mean())
print("Median of", column_name, ":", df[column_name].median())
print("Standard deviation of", column_name, ":", df[column_name].std())
