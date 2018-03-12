import numpy as np
from chdir import chdir

with open('/Users/Carol/Desktop/RNAseqbrain-out.txt','r') as nf:
    next(nf)
    genes = []
    ctrls = []
    expms = []
    for line in nf:
        words = line.split('\t')
        genes.append(words[0])
        ctrls.append([float(x) for x in words[1:8]])
        expms.append([float(x) for x in words[8:16]])
        
b = chdir(ctrls,expms)
b = np.squeeze(b)
annot_b = list(zip(genes,b.tolist()))
res = sorted(annot_b,key=lambda x:x[1]*x[1],reverse=True)
#assert(res[0][0]=='MCL1')
#assert(res[1][0]=='LIMD2')
#assert((res[1][1]-0.379125)<0.0001)

print(res)

new_file = '/Users/Carol/Desktop/gtex_analysis/brain-2050-chdir.txt'
f = open(new_file, 'w')
#f.write(res)
f.write(str(res))



