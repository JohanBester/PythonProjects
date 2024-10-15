input_file_path = 'tenantJson.json'
output_file_path = 'output.txt'

# Read data from the input file
with open(input_file_path, 'r') as file:
    data = file.read()

# Strip out '\n' and replace '\"'
cleaned_data = data.replace('\\n', '\n').replace('\\"', '"')

# Write the cleaned data to the output file
with open(output_file_path, 'w') as file:
    file.write(cleaned_data)

print("Data has been cleaned and written to", output_file_path)
