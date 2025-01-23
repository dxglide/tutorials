import csv
import os

# https://www.pythontutorial.net/python-basics/python-read-csv-file/
# The csv module provides a reader object to read a CSV file.

def file_path(file, file_dir):
    return os.path.join(os.getcwd(), file_dir, file)

file =  file_path('country.csv', 'I_O_files')

with open(file, encoding="utf8") as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        print(line)

with open(file, encoding="utf8") as f:
    csv_reader = csv.reader(f)
    for line_no, line in enumerate(csv_reader, 1):
        if line_no == 1:
            print('Header:')
            print(line)  # header
            print('Data:')
        else:
            print(line)  # data