#!/bin/bash
. ./config
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
ffmpeg -y -i rtsp://$varip/live0 -vframes 1 $name.jpg
