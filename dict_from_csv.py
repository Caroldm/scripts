import csv
f = open ('/Users/carol/Desktop/chea_test.csv','rt', encoding='utf8') 
csv_f =  csv.DictReader(f) 


tf = 
current_line = [row[1]]
genes = [row[3]]
prev_line = [current_line:-1]

for line in f:
 if current_line == prev_line
 print (genes)
    
 else 
 print (current_line)
 print (genes)
        
   
########################
######## Test ##########
########################

with open('/Users/carol/Desktop/chea_test.csv','rt', encoding='utf8') as f:
    reader = csv.DictReader(f) # read rows into a dict 
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append value to list
                                 # based on column name k


print(columns['name'])
print(columns['phone'])
print(columns['street'])
        
