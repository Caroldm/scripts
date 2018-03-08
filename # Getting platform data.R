# Getting platform data

#source("https://bioconductor.org/biocLite.R")
#biocLite("SRAdb")

setwd('/Users/Carol/Desktop/')

library(GEOquery) 

# Read in the data
#x <- scan("/Users/Carol/Desktop/LadoE/gsm_11.txt", what="", sep="\n")
#gsm_list <- strsplit(x, "[[:space:]]+")  # Separate elements by one or more whitepace
#for (i in gsm_list){
#  gsm <- getGEO(i, destdir='/Users/Carol/Desktop/gsm_falta/')
#}


gpl10558 <- getGEO('gpl10558')
Meta(gpl10558)$title

head(Meta(gpl10558)$series_id)

length(Meta(gpl10558)$series_id)

head(Meta(gpl10558)$sample_id)

length(Meta(gpl10558)$sample_id)

# Download all the samples

gsmids <- Meta(gpl10558)$sample_id
gsmlist <- sapply(gsmids,getGEO)
data <- names(gsmlist)
for (i in gsm_list){
  gsm <- getGEO(i, destdir='/Users/Carol/Platforms/')
}