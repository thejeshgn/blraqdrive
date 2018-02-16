	# coding=utf-8
import sys
import os
import sqlite3 as lite
import csv
import dataset
import json
import string
import gpxpy 
import gpxpy.gpx 
import arrow
import pytz
from pytz import timezone

root_raw_data_folder = '/home/thej/Documents/code/blraqdrive/data/gpx'


def step1_import_gpx():
	db = dataset.connect('sqlite:////home/thej/Documents/code/blraqdrive/data/db/data.sqlite3')	
	locations = db['locations']	
	#IST format 2018-02-05 00:01:00


	for path, subdirs, files in os.walk(root_raw_data_folder):
		for name in files:
			gpx_file_path = os.path.join(path, name)
			gpx_file = open(gpx_file_path, 'r') 			
			alredy_exists  = locations.find_one(track=name)
			if alredy_exists:
				continue

			if gpx_file_path[-4:] == ".gpx":
				gpx = gpxpy.parse(gpx_file) 
				gpx_locations = []
				for track in gpx.tracks: 
					for segment in track.segments: 
						for point in segment.points: 
							row = {}							
							row["latitude"] = point.latitude
							row["longitude"] = point.longitude
							row["elevation"] = point.elevation
							row["time"] = point.time

							utc_time = pytz.utc.localize(point.time) 							
							IST = timezone('Asia/Calcutta')
							ist_time = utc_time.astimezone(IST)
							#IST format 2018-02-05 00:01:00
							format_db_ist="%Y-%m-%d %H:%M:%S"
							print "-------------"
							utc_time = utc_time.strftime(format_db_ist)
							ist_time = ist_time.strftime(format_db_ist)
							row["utc_time"] = utc_time
							row["ist_time"] = ist_time
							row["track"] = name
							gpx_locations.append(row)
							print str(row)
				db.begin()
				locations.insert_many(gpx_locations)							
				db.commit()
			else:
				print "Not a gpx file"



def main():
	step1_import_gpx()

if __name__ == "__main__":
	main()
