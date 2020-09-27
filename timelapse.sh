#!/bin/bash
. /lemontree/config
echo $varip
year=$(date +%Y)
echo $year
month=$(date +%m)
echo $month
day=$(date +%d)
echo $day
path=/lemontree/$year/$month/$day
name=danale-$year-$month-$day-$(date +%H-%M)
if [ ! -d $path ]; then
	mkdir -p $path
fi
cd $path
ffmpeg -y -rtsp_transport tcp -i rtsp://$varip -vframes 1 $name.jpg
python3 /lemontree/crop.py $name.jpg
