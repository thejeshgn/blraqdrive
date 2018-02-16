# coding=utf-8
import sys
import os
import sqlite3 as lite
import csv
import dataset
import json
import string

root_raw_data_folder = '/home/thej/Documents/code/blraqdrive/data/aq'
db = dataset.connect('sqlite:////home/thej/Documents/code/blraqdrive/data/db/data.sqlite3')		



def step1_match_minute():

	matched_minute = db['matched_minute']
	minute_query = """
	select distinct substr(locations.ist_time, 0, 17) time, CAST(aq.pm25 AS FLOAT) as pm25, CAST(aq.pm10 AS FLOAT) as pm10, 
		locations.latitude as latitude, locations.longitude as longitude, locations.track as track 
	from locations, aq  
	where substr(locations.ist_time, 0, 17) = substr(aq.CreatedDate,0,17)
	"""

	db.begin()
	matched_minute.delete()
	db.commit()


	results =  db.query(minute_query)
	matched_minute.insert_many(results)
	db.commit()												



def step2_match_seconds():

	matched_seconds = db['matched_seconds']
	second_query = """
	select distinct locations.ist_time as time, CAST(aq.pm25 AS FLOAT) as pm25, CAST(aq.pm10 AS FLOAT) as pm10, 
		locations.latitude as latitude , locations.longitude as longitude, locations.track as track 
	from locations, aq  
	where locations.ist_time = aq.CreatedDate;
	"""

	db.begin()
	matched_seconds.delete()
	db.commit()


	results =  db.query(second_query)
	matched_seconds.insert_many(results)
	db.commit()												


def main():
	step1_match_minute()
	step2_match_seconds()

if __name__ == "__main__":
	main()
