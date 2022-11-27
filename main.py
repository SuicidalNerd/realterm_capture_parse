#with open('capture_demo.txt','r') as f:
    #line_list=[]
    #recnik = {}
    #for line in f:
        #strip_lines=line.strip()
        #listli=str(strip_lines.split())
        #m=line_list.append(listli)
        #print(listli)
        
###==^^==OLD IDEA==^^==###

import csv
from csv import reader, DictReader
from datetime import datetime

with open('capture_demo.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('log.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('time', 'current'))
        writer.writerows(lines)

with open('log.csv','r') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    header = next(csv_dict_reader)
    if header != None:
        for row in csv_dict_reader:
            print(datetime.utcfromtimestamp(int(row['time'])).strftime('%Y-%m-%d %H:%M:%S'), format(int(row['current'],'f')))