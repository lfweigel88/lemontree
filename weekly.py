#!/usr/bin/python3
import os
import glob
import datetime
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("start", type=int, help="Number of days ago to start")
parser.add_argument("times", type=str, help="Times to grab")
args = parser.parse_args()
startinput = args.start
timesinput = args.times
os.system('rm -rf tmp')
today = datetime.datetime.now()
year = today.year
month = today.month
day = today.day
#startinput = input("Enter number of days ago to start: ")
#timesinput = input("Enter times to grab: ")
timesinput = timesinput.split(',')
times = []
for i in timesinput:
	times.append(i)
start = int(day) - int(startinput)
print(start)
print(times)
os.system("mkdir /lemontree/tmp")
while start <= day:
	if start < 10:
	        startstr = ("0"+str(start))
	else:
        	startstr=str(start)
	for i in times:
		os.system('cp ./2020/08/'+startstr+'/*-'+i+'-00.jpg tmp/')
	start = start + 1
name = "weekly-" + str(year) + "-" + str(month) + "-" + str(day) + "-" + str(today.hour) + "-" + str(today.minute)
print(name)
os.system('ffmpeg -framerate 1 -pattern_type glob -i "tmp/*.jpg" -c:v libx264 -pix_fmt yuv420p '+ name + '.mp4')
#os.system('python /lemontree/youtube.py --file=/lemontree/'+name+'.mp4 --title='+name+' --category="22" --privacyStatus="public" --noauth_local_webserver')
#os.system('rm -rf '+name+'.mp4')
