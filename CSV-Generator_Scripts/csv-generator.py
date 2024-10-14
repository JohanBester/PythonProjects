from faker import Faker
import csv
import random
import string
import argparse
import json
import os
import zipfile

# CSV-Generator Usage Help:
# --------------------------
# usage: CSV Generator [-h] [-d DELIMITER] [-r ROWS] [-uh]
#                      [-o OUTPUT_DIR] [-i INPUT] [-id INPUT_DELIMITER]  
#                      [-s SEED]
#
# Given a JSON input file like { filename: delimited_columns, ... },     
# generate random CSV files with those columns
#
# options:
#   -h, --help            show this help message and exit
#   -d DELIMITER, --delimiter DELIMITER
#                         delimiter for the CSV default=","
#   -r ROWS, --rows ROWS  number of rows to generate default=20
#   -uh, --use_headers    use headers
#   -o OUTPUT_DIR, --output_dir OUTPUT_DIR
#                         output folder default="/code/output"
#   -i INPUT, --input INPUT
#                         source file with header names default="input.json"
#   -id INPUT_DELIMITER, --input_delimiter INPUT_DELIMITER
#                         delimiter for the source file default=","
#   -s SEED, --seed SEED  seeding the generator default=None
# 
# Documentation can be found at ...
#   https://faker.readthedocs.io/en/master/


# CSV-Generator Usage command Example:
# --------------------------------------
#   python csv-generator.py -d "," -r 30 -uh -i "./input.json"


parser = argparse.ArgumentParser(
    prog='CSV Generator',
    description='Given a JSON input file like { filename: delimited_columns, ... }, generate random CSV files with those columns')

parser.add_argument('-d', '--delimiter', type=str, default=',',
                    help='delimiter for the CSV default=","')

parser.add_argument('-r', '--rows', type=int, default=20,
                    help='number of rows to generate default=20')

parser.add_argument('-uh', '--use_headers', action='store_true',
                    help='use headers default ="store_true"')

parser.add_argument('-o', '--output_dir', type=str, default='D:/Code_(D)/output',
                    help='output folder default="/code/output"')

parser.add_argument('-i', '--input', default='input.json',
                    help='source file with header names default="input.json"')

parser.add_argument('-id', '--input_delimiter', type=str, default=',',
                    help='delimiter for the source file  default=","')

parser.add_argument('-s', '--seed', type=int, default=None,
                    help='seeding the generator default=None')


args = parser.parse_args()
if args.seed != None:
    Faker.seed(args.seed)
    random.seed(args.seed)
fake = Faker('en_US')

with open('csv-generator-config.json', 'r') as file:
    config = json.loads(file.read())


def trim(s, l):
    if len(s) > l:
        return s[:l]
    return s


def address():
    return fake.street_address()


def url():
    return fake.url()


def city():
    return fake.city()


def state():
    return fake.state()


def country():
    return fake.country()


def postalcode():
    return fake.postalcode()


def company():
    return fake.company() + ' ' + fake.company_suffix()

    
def rstring():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(config['rstring']['len']))


def phone():
    return fake.phone_number()


def number():
    return ''.join(random.choice(string.digits) for _ in range(config['number']['len']))


def integer():
    return ''.join(random.choice(string.digits) for _ in range(config['integer']['len']))


def money():
    return ''.join(random.choice(string.digits) for _ in range(config['money']['len'])) + '.00'


def text():
    return trim(fake.text(), config['text']['len'])


def name():
    return fake.name()


def yes_no():
    return random.choice(["Y", "N"])


def date():
    return str(fake.date_between(start_date=config['date']['state_date'], end_date=config['date']['end_date'])) + ' 00:00:00'


def password():
    return fake.password(length=18, special_chars=True, upper_case=False)


def value(header):
    header = header.lower()
    for group in config:
        for keyword in config[group]['contains']:
            if keyword in header:
                return str(eval(group)()).replace(args.delimiter, '').replace('\"', '').replace('\'', '').replace('\n', '')
    return number()


with open(args.input, 'r') as file:
    input = json.loads(file.read())

for csv_name in input:
    new_file = os.path.join(args.output_dir, csv_name)
    os.makedirs(os.path.dirname(new_file), exist_ok=True)
    with open(new_file, 'w', newline='') as csv_file:
        spamwriter = csv.writer(
            csv_file, delimiter=args.delimiter, quoting=csv.QUOTE_ALL)
        headers = input[csv_name].split(args.input_delimiter)
        if (args.use_headers):
            spamwriter.writerow(headers)
        for _ in range(args.rows):
            rs = [value(header) for header in headers]
            spamwriter.writerow(rs)
    print('Saved at \"' + new_file + '\"')


# ZIP THE CSV FILES AFTER CREATION
def zip_csv_files(folder_path):
    csv_files = [file for file in os.listdir(
        folder_path) if file.endswith('.csv')]

    if csv_files:
        for csv_file in csv_files:
            zip_file_path = os.path.join(
                folder_path, f"{os.path.splitext(csv_file)[0]}.zip")
            with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
                file_path = os.path.join(folder_path, csv_file)
                zip_file.write(file_path, os.path.basename(file_path))
            print(
                f"CSV file '{csv_file}' zipped successfully to '{zip_file_path}'.")
    else:
        print("No .csv files found in Output folder.")
        return


if __name__ == "__main__":
    folder_path = args.output_dir
    zip_csv_files(folder_path)
