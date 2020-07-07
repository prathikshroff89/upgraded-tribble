import json
import csv

with open('/Users/pshroff/Downloads/sample-json-file.json') as json_file: 
    data = json.load(json_file) 
  
e_data = data['address']
  
data_file = open('/Users/pshroff/Downloads/data_file.csv', 'w') 
  
csv_writer = csv.writer(data_file) 

count = 0
  
for e in e_data: 
    if count == 0: 
  
        
        header = e.keys() 
        csv_writer.writerow(header) 
        count += 1
  
    
    csv_writer.writerow(e.values()) 
  
data_file.close() 