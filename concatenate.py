# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:16:06 2024

@author: Owner
"""
import pandas as pd

# List of file paths for the CSV files
files = ['rs3750861.csv', 'rs10508266.csv', 'rs10841302.csv']

# Initialize an empty list to store dataframes
dfs = []

# Loop through the list of files and load each into a DataFrame
for file in files:
    df = pd.read_csv(file)
    # Strip leading/trailing whitespace from column names
    df.columns = df.columns.str.strip()
    # Rename the columns if needed for clarity
    df.columns = ['Population', file.split('.')[0]]  # Name the second column based on the file name (you can customize)
    dfs.append(df)

# Merge all dataframes on the 'Population' column (country code)
merged_df = dfs[0]  # Start with the first dataframe
for df in dfs[1:]:
    merged_df = merged_df.merge(df, on='Population', how='outer')  # Use 'outer' to keep all countries

# Display the final merged dataframe
print(merged_df)

# Optionally, save the merged dataframe to a new CSV file
merged_df.to_csv('merged_countries_data.csv', index=False)

