#!/bin/bash
year=$(date +%Y)
echo $year
month=$(date +%m)
echo $month
day=$(date +%d)
echo $day
path=/lemontree/$year/$month/$day
name=eufy-$year-$month-$day-$(date +%H-%M)
if [ ! -d $path ]; then
	mkdir -p $path
fi
cd $path
ffmpeg -y -i rtsp://192.168.43.116/live0 -vframes 1 $name.jpg
