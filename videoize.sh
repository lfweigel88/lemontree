#!/bin/sh
year=$(date +%Y)
month=$(date +%m)
day=$(date +%d)
path=/lemontree/$year/$month/$day
name=$year-$month-$day-$(date +%H-%M)
cd $path
ffmpeg -framerate 1 -pattern_type glob -i "*.jpg" -c:v libx264 -pix_fmt yuv420p $name.mp4
cd /lemontree
python /lemontree/youtube.py --file=$path/$name.mp4 --title=$name --category="22" --privacyStatus="public" --noauth_local_webserver
rm $path/$name.mp4
