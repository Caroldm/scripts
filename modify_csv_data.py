
################################
##### Modify data ##############
################################

import csv
out = open ('/Users/carol/Desktop/chea_test.csv','rt', encoding='utf8') ## keept getting error iterator, should return strings, not bytes
data =  csv.reader(out)
data = [row for row in data]
out.close()
#print (data)

new_data = [[row[0],row[1]+row[2]] for row in data] 
#print (new_data)


#Save
out = open('new_data.csv','wt') # o 'wb' e escrever, write
output = csv.writer(out) 


for row in new_data:
   output.writerow(row)    
out.close() 




################################
################################
##### Alternative - Test1 ######
#####     Using a DICT    ######
################################
################################

import csv
out = open ('/Users/carol/Desktop/cheabackground1.csv','rt', encoding='UTF-8')  
data =  csv.reader(out)


new_data = [[row[1]+ '-' + row[4]+'-'+row[5]+'-'+row[6] +'-'+ row[7], row[3]] for row in data] 
#new_data = [[row[2]+'-'+row[5]+'-'+row[6] +'-'+ row[7], row[3]] for row in data] 


#Dict
my_dict = {}
for row in new_data:
   if row[0] in my_dict:
      my_dict[row[0]] += " " + row[1]
   else:
      my_dict[row[0]] = row[1]

new_data = [[my_key,my_dict[my_key]] for my_key in my_dict]
#print (new_data)


#Output
out = open('/Users/carol/new_dataf.csv','wt') 
output = csv.writer(out)  

for row in new_data:
   output.writerow(row)    
out.close()



################################
################################
##### Alternative - Test2 ######
#####  string encode issue #####
################################
################################

import csv
out = open ('/Users/carol/Desktop/cheabackground1.csv','rt', decode='UTF-8')  # open the input file rename it out
data =  csv.reader(out) # read inputed file

new_keys = [row[1]+ '-' + row[4]+'-'+row[5]+'-'+row[6] +'-'+ row[7] for row in data] 
new_values = [row[3] for row in data]


aggregate_values = {} # An empty dictionary

# Iterate across the paired lists together

for key, value in zip(new_keys, new_values): 
    if key not in aggregate_values:
        aggregate_values[key] = [value]
    else: 
        aggregate_values[key].append(value)

out = open('/Users/carol/newdata10.csv','wt') 
output = csv.writer(out)  

# printed output
for key in aggregate_values:
    print (key + ' ' + ' '.join(aggregate_values[key])
    

out.close()

           

# TEST3

import csv

out = open ('/Users/carol/Desktop/cheabackground1.csv','rt', encoding = 'UTF-8', errors = 'ignore')  
data =  csv.reader(out)

new_data = [[row[1]+ '-' + row[4]+'-'+row[5]+'-'+row[6] +'-'+ row[7], row[3]] for row in data] 

my_dict = {}
for row in new_data:
   if row[0] in my_dict:
      my_dict[row[0]] += ' ' + row[1]
   else:
      my_dict[row[0]] = row[1]

new_data = [[my_key,my_dict[my_key]] for my_key in my_dict]

print (new_data)

out = open('/Users/carol/new_dataf1.csv','wt') 
output = csv.writer(out)  


out.close()

