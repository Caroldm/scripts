# Delete duplicates

# Holds lines already seen
lines_seen = set()  
outfile = open('/Users/Carol/Documents/SRA_RNA-seq_GEO/search_geo_pl_py/gse_category_classifier_text_mining_out.csv','w')


for line in open('/Users/Carol/Documents/SRA_RNA-seq_GEO/search_geo_pl_py/gse_category_classifier_text_mining_out.csv','rU'):
    if line not in lines_seen: 
        outfile.write(line)
        lines_seen.add(line)
        
outfile.close()
