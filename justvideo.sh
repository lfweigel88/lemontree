#!/bin/sh
year=$(date +%Y)
month=$(date +%m)
day=$(date +%d)
path=/lemontree/$year/$month/$day
name=$year-$month-$day-$(date +%H-%M)
cd $path
ffmpeg -framerate 1 -pattern_type glob -i "*.jpg" -c:v libx264 -pix_fmt yuv420p $name.mp4
