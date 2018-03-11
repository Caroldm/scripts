import os
import re

path = '/Users/Carol/Desktop/GS/'

# Print os.listdir(path)
for filename in os.listdir(path):
	with open(path + filename,'rU') as data:
		data=data.readlines()
		words = ['SRA:']
		keep = re.compile(r"|".join(words))
		#print(filename)
    	for line in data:
         # if line contains match from words
        	if keep.search(line):
        		l = line.replace('!Sample_relation =','')
        		name = filename.strip('.soft')
        		print(name + l)



# #source("https://bioconductor.org/biocLite.R")
# #biocLite("SRAdb")

# setwd('/Users/Carol/Desktop/GSMmetadata/')
# library(GEOquery) 
# library(SRAdb) 


# #gds <- getGEO("GSM1847166") 
# #Meta(gds)


# mylist=("GSM1686397", "GSM1686398", "GSM1686399", "GSM1686400")


# for (i in mylist){
#   gds <- getGEO(i)
#   Meta(gds)
# }
# write(gds, file='/Users/Carol/Desktop/GSMmetadata/)
