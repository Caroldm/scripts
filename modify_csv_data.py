#import csv

out = open ('/Users/carol/Desktop/chea_test.csv','rt', encoding='utf8') ## keept getting error iterator, should return strings, not bytes
data =  csv.reader(out)
data = [row for row in data]
out.close()
#print (data)


new_data = [[row[0],row[1]+row[2]] for row in data] 
#print (new_data)


#Open and save
out = open('new_data.csv','wt') # o 'wb' e escrever, write
output = csv.writer(out) 


for row in new_data:
   output.writerow(row)    
out.close() 

