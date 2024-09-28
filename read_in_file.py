# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:48:26 2024

@author: Owner
"""
import pandas as pd
import os

# Set the default directory
os.chdir(r'C:\Users\Owner\Documents\GitHub\disease-susceptibility-analysis')

# Original CSV file name
original_file = '1000genomesprojectphase3-PopulationGenotypes-Homo_sapiens_Variation_Population_rs10841302.csv'

# Function to extract rs_number from the filename
def extract_rs_number(filename):
    start = filename.find('rs')
    if start != -1:
        end = filename.find('.', start)  # Locate the end of the rs_number before the file extension
        if end != -1:
            return filename[start:end]  # Extract 'rs' and the following digits
    return None

# Extract rs_number from the file name
rs_number = extract_rs_number(original_file)

# Load your data (assuming the data is in a CSV format with no header. Adjust 'header=0' if there's a header)
df = pd.read_csv(original_file, header=None)

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
df['T_Number'] = df['Column2'].apply(extract_t_number)

# Select only the necessary columns
output_df = df[['Country_Code', 'T_Number']]

# Generate the output CSV filename based on the rs_number
if rs_number:
    output_filename = f'{rs_number}.csv'
    # Save the result to a new CSV
    output_df.to_csv(output_filename, index=False)
    print(f"Saved to {output_filename}")
else:
    print("rs_number not found in the file name")

# Print the first few rows to verify
print(output_df.head())
