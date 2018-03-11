import os
import pandas as pd 
import numpy as np
import csv
import re

path = '/Users/Carol/Desktop/Work/hg_ag/hg_ag_sigs_full/'

# Create folder for saving signatures
folders = os.listdir('./')
savefolder = 'hg_ag_sigs_full_no_headers'
if savefolder not in folders:
    os.mkdir(savefolder)



#path = '/Users/Carol/Desktop/Work/hg_ag/hg_ag_sigs_full/'


for filename in os.listdir(path):
	if filename.endswith('.txt'):
		#print filename
		fname = filename.strip('.txt') 
		lines = []
		file = (path + filename)
		df = pd.read_csv(file, sep='\t', comment='!', index_col=0) 
		#print data
		#lines = data.readlines()
		savefile = savefolder + '/' +  fname + '.txt'
		df.to_csv(savefile)
		



        
