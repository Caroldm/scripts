library(SRAdb)
setwd('~/Desktop/SRA_demo')
## download the sqlite db of the metadata of SRA
sqlfile <- 'SRAmetadb.sqlite'
if (!sqlfile %in% list.files()){
	sqlfile <- getSRAdbFile()
}
## connect to SQLite db
sra_con <- dbConnect(SQLite(), sqlfile)
## search db using terms
#rs <- getSRA(search_terms = "breast cancer", out_types = c("run", "study"), sra_con = sra_con)
## get information of a specific SRA entity
#rs <- getSRAinfo(in_acc = c("SRP062188"), sra_con = sra_con)
## download the .sra files in the SRP
getSRAfile(in_acc = c("SRP070895"), sra_con = sra_con, destDir = getwd())
list.files()
