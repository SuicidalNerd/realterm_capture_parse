import csv
from csv import reader, DictReader
from datetime import datetime
import decimal

time = ""
current = 0

average_current = 0
current_pom = 0
measurement_counter = 0

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
           time = datetime.utcfromtimestamp(int(row['time'])).strftime('%H:%M:%S')
           current = decimal.Decimal(row['current'])
           #print(final_line)
           measurement_counter = measurement_counter + 1
           current_pom = current_pom + current
           print(time + "," + str(current))
           writer = csv.writer(results)
           writer.writerow((time, current))
           
average_current = current_pom / measurement_counter
average_current_ma = average_current/1000
print("Average current:" + str(average_current) + " A - " +"(" + str(round(average_current_ma, 4)) +") mA")