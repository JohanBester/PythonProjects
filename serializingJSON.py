import json
import re

def serialize_json_with_encoded_line_breaks(input_file, output_file):
    # Read the JSON data from the input file
    with open(input_file, 'r') as infile:
        data = json.load(infile)
    
    # Serialize the data to a JSON string
    json_string = json.dumps(data, indent=2)
    
    # Encode line breaks
    encoded_json_string = json_string.replace('\n', '\\n').replace('\r', '\\r')
    
    # Escape double quotes - replace '\"'
    cleaned_data = encoded_json_string.replace('\"', '\\"')
    
    # Remove excessive space characters
    encoded_json_string = re.sub(r'\s{2,}', ' ', cleaned_data)
        
    # Write the encoded JSON string to the output file
    with open(output_file, 'w') as outfile:
        outfile.write(encoded_json_string)

# Example usage
# Specify your input file here
input_filename = 'formatted_json.json'
# Specify your output file here
output_filename = 'output.json'

serialize_json_with_encoded_line_breaks(input_filename, output_filename)
print(f"Encoded JSON has been written to {output_filename}")
