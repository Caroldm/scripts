import csv

 with open ('/Users/data.csv','rU') as f1, open ('out.csv','w') as out:
  	data=csv.reader(f1)
  	# next(data, None) 
  	string=('GSM')
  	for line in data:
  		for line[0] in line:
  			if any(s in line[0] for s in string):
  				print(line)
  				out.write(str(line))



