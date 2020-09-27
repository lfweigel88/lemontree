#!/usr/bin/python3
import os
import glob
import datetime
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("start", type=int, help="Number of days ago to start")
parser.add_argument("times", type=str, help="Times to grab")
parser.add_argument("--upload", help="Upload flag", action="store_true")
args = parser.parse_args()
print(args.upload)
startinput = args.start
timesinput = args.times
os.system('rm -rf /lemontree/tmp')
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
#start = int(day) - int(startinput)
#start = datetime.datetime.now() - datetime.timedelta(days=startinput)
#print(dir(start))
os.system("mkdir /lemontree/tmp")
i = int(startinput)
while i >= 0:
	start = datetime.datetime.now() - datetime.timedelta(days=i)
	if start.month < 10:
        	startmostr = ("0"+str(start.month))
	else:
        	startmostr = str(start.month)
	if start.day < 10:
		print(str(start.day) + " was less than 10")
		startdastr = ("0"+str(start.day))
	else:
        	startdastr=str(start.day)
	for t in times:
		print('/lemontree/2020/'+str(startmostr)+'/'+startdastr+'/*-'+t+'-00.jpg /lemontree/tmp/')
		os.system('cp /lemontree/2020/'+str(startmostr)+'/'+str(startdastr)+'/*-'+str(t)+'-00.jpg /lemontree/tmp/')
	i = int(i) - 1
name = "weekly-" + str(year) + "-" + str(month) + "-" + str(day) + "-" + str(today.hour) + "-" + str(today.minute)
print(name)
os.system('ffmpeg -framerate 1 -pattern_type glob -i "/lemontree/tmp/*.jpg" -c:v libx264 -pix_fmt yuv420p /lemontree/'+ name + '.mp4')
if args.upload:
	os.system('cd /lemontree; python /lemontree/youtube.py --file=/lemontree/'+name+'.mp4 --title='+name+' --category="22" --privacyStatus="public" --noauth_local_webserver')
	os.system('rm -rf /lemontree/'+name+'.mp4')
