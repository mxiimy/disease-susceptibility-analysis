# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 19:13:39 2024

@author: Owner
"""
import pandas as pd

# Path to your CSV file
csv_file_path = 'D:/extracted_biosample_geoloc/biosample_geoloc.csv'

# Read the first 100 rows of the CSV file
first_1000_rows = pd.read_csv(csv_file_path, nrows=1000)

# Display the first 100 rows
print(first_1000_rows)
