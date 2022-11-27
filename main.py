import csv
from csv import reader, DictReader
from datetime import datetime
import decimal

def text_to_csv():
    with open('capture_demo.txt', 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(",") for line in stripped if line)
        with open('log.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('time', 'current'))
            writer.writerows(lines)

def parse_test():
    with open('log.csv','r') as read_obj:
     csv_dict_reader = DictReader(read_obj)
     header = next(csv_dict_reader)
     if header != None:
           for row in csv_dict_reader:
              print(datetime.utcfromtimestamp(int(row['time'])).strftime('%H:%M:%S'), decimal.Decimal(row['current']))

parse_test()