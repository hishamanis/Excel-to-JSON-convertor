import pandas as pd
# Load the Excel file
excel_data = pd.read_excel('Excel_Data.xlsx')
# Convert the Excel data to a JSON string
json_data = excel_data.to_json(orient='records')
# Save the JSON string to a file
with open('Excel_Data.json', 'w') as json_file:
   json_file.write(json_data)