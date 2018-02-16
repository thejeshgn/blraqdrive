# coding=utf-8
import sys
import os
import sqlite3 as lite
import csv
import dataset
import json
import string

root_raw_data_folder = '/home/thej/Documents/code/blraqdrive/data/aq'


def step1_import_aq():
	db = dataset.connect('sqlite:////home/thej/Documents/code/blraqdrive/data/db/data.sqlite3')	
	aq = db['aq']	
	#IST format 2018-02-05 00:01:00

	db.begin()
	aq.delete()
	db.commit()

	for path, subdirs, files in os.walk(root_raw_data_folder):
		for name in files:
			csv_file_path = os.path.join(path, name)					

			if csv_file_path[-4:] == ".csv":
				print csv_file_path
				with open(csv_file_path,'rb') as csvfile:
					reader = csv.DictReader(csvfile)
					aq.insert_many(reader)
					db.commit()												
			else:
				print "Not a csv file"


def main():
	step1_import_aq()

if __name__ == "__main__":
	main()
