#!/usr/bin/python

import MySQLdb

db=MySQLdb.connect(user="root",passwd="",db="GEOsra",
	unix_socket="/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock")


def query_1():
	sql = """
SELECT *
FROM `gsm`
WHERE `accession` = 'GSE43717'
"""
print query_1



# (sample, description, sample_type, Label)