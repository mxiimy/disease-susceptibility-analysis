# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:48:26 2024

@author: Owner
"""
import pandas as pd
import os

# Set the default directory
os.chdir(r'C:\Users\Owner\Documents\GitHub\disease-susceptibility-analysis')

# Load your data
# Assuming your data is in a CSV file with no header. If it has a header, set 'header=0'
df = pd.read_csv('data1.csv', header=None)

# Select only the first and third columns
df = df[[0, 2]]

# Rename columns for clarity
df.columns = ['Column1', 'Column2']

# Function to extract country code from the first column
def extract_country_code(col):
    return col.split(';')[0]

# Function to extract the T number from the second column
def extract_t_number(col):
    parts = col.split('T:')
    if len(parts) > 1:
        t_part = parts[1].split()[0]  # Extract the number after 'T:'
        return t_part
    return None

# Apply the functions to the respective columns
df['Country_Code'] = df['Column1'].apply(extract_country_code)
df['Allele Frequency'] = df['Column2'].apply(extract_t_number)

# Select only the necessary columns
output_df = df[['Country_Code', 'Allele Frequency']]

# Save the result to a new CSV
output_df.to_csv('rs10508266.csv', index=False)

# Print the first few rows to verify
print(output_df.head())
