# By Hish Anis 2nd November 2025
# import_csv.py
# This script reads a CSV file and converts its contents to a JSON file.
# It uses the built-in csv and json libraries in Python.
# Make sure to have an input 'file_name.csv' file in the same directory as this script.
# The output will be saved as 'output.json'.

import csv
import json

# Open the CSV file
with open('food_data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Convert rows to a list of dictionaries
    data = [row for row in csv_reader]

# Write to a JSON file
with open('output.json', mode='w') as json_file:
    json.dump(data, json_file, indent=4)

print("CSV has been successfully converted to JSON!")

print("By Hish Anis 2nd November 2025")
