import json


def format_json(input_file, output_file=None):
    # Read the JSON data from the input file
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Format the JSON data
    formatted_json = json.dumps(data, indent=4)

    # If an output file is provided, save the formatted JSON to that file
    if output_file:
        with open(output_file, 'w') as f:
            f.write(formatted_json)


def clean_json(input_file_path, output_file_path):
    # Read data from the input file
    with open(input_file_path, 'r') as file:
        data = file.read()

    # Strip out '\n' and replace '\"'
    cleaned_data = data.replace('\\n', '\n').replace('\\"', '"')

    # Write the cleaned data to the output file
    with open(output_file_path, 'w') as file:
        file.write(cleaned_data)


# Example usage
if __name__ == "__main__":
    
    input_file_path = 'tenantJson.json'
    output_file_path = 'cleaned_data.txt'
    
    clean_json(input_file_path, output_file_path)
    
    formatted_json = 'formatted_json.json'  # Optional: Replace with your desired output file path
    
    format_json(output_file_path, formatted_json)

    print("Data has been cleaned and written to", formatted_json)
