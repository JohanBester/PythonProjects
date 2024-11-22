import pandas as pd

# Load the Excel file
df = pd.read_csv('D:/OneDrive - DataServ/Downloads/IPM_Labor_Distribution_Copy.csv')

# Save the DataFrame to CSV with UTF-8 encoding and wrap all values in double quotes
df.to_csv('D:/OneDrive - DataServ/Downloads/IPM_Labor_Distribution_Copy_output.csv', index=False, quoting=1, encoding='utf-8')
