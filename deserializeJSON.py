import json


def deserialize_specific_key(input_file, key):
    # Read the JSON data from the input file
    with open(input_file, 'r') as infile:
        json_string = infile.read()
    
    # Deserialize the JSON string into a Python dictionary
    data = json.loads(json_string)
    
    # Check if the data is a list
    if isinstance(data, list):
        # Iterate over each item in the list and apply replacements
        for item in data:
            if isinstance(item, dict) and key in item:
                item[key] = item[key].replace('\\n', '\n').replace('\"', '"')
                print(item[key])

    return data  # Return the modified list


def format_json(result_data, output_file=None):
    # Format the JSON data
    formatted_json = json.dumps(result_data, indent=4)

    # If an output file is provided, save the formatted JSON to that file
    if output_file:
        with open(output_file, 'w') as f:
            f.write(formatted_json)
            
    return formatted_json


# Example usage
if __name__ == "__main__":
    
    cleaned_file_path = 'cleaned_data.txt'
    formatted_json_output = 'formatted_json.json'
    
    # Specify your input file here
    input_file_path = 'tenantJson.json'
    # Specify the key you want to extract
    key_to_extract = 'json'
    
    data = deserialize_specific_key(input_file_path, key_to_extract)

    if data:
        print(f"The value of the key '{key_to_extract}' was found.")
        # print(data)
        
        formatted_json = format_json(data, formatted_json_output)
        
        if formatted_json:
            print("Data has been formatted and written to", formatted_json_output)
        else:
            print("There was an error formatting the data")

    else:
        print(f"The key '{key_to_extract}' was not found in the JSON.")
