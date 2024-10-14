import csv

# This code reads the input CSV file, reads each row, wraps each field in double quotes,
# and then writes the modified rows to the output CSV file.
# Line 16 below wraps each field in the double quotes


input_file = 'D:/OneDrive - DataServ/Downloads/APVendorMaster1.CSV'
output_file = 'D:/OneDrive - DataServ/Downloads/APVendorMaster.CSV'

with open(input_file, 'r', newline='') as csv_in, open(output_file, 'w', newline='') as csv_out:
    reader = csv.reader(csv_in)
    writer = csv.writer(csv_out, quoting=csv.QUOTE_ALL)

    for row in reader:
        wrapped_row = ['"{}"'.format(field) for field in row]
        writer.writerow(row)
