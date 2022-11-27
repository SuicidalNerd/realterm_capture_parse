import csv
from csv import reader, DictReader
from datetime import datetime
import decimal

time_temp = ""
current_temp = 0


with open('capture_demo.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    
    with open('capture.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('time', 'current'))
        writer.writerows(lines)
        
with open('capture.csv','r') as read_obj:
 csv_dict_reader = DictReader(read_obj)
 header = next(csv_dict_reader)
 if header != None:
     with open('results.csv', 'w') as results:
       for row in csv_dict_reader:
           #final_line = datetime.utcfromtimestamp(int(row['time'])).strftime('%H:%M:%S'), decimal.Decimal(row['current'])
           time_temp = datetime.utcfromtimestamp(int(row['time'])).strftime('%H:%M:%S')
           current_temp = decimal.Decimal(row['current'])
           #print(final_line)
           print(time_temp + "," + str(current_temp))
           writer = csv.writer(results)
           writer.writerow((time_temp, current_temp))