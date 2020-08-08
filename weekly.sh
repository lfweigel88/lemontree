#!/bin/bash
year=$(date +%Y)
month=$(date +%m)
day=$(date +%d)
startday=$(date --date="1 week ago" +%d)
startmonth=$(date --date="1 week ago" +%m)
startyear=$(date --date="1 week ago" +%Y)
mkdir /lemontree/tmp
cp /lemontree/[$startyear-$year]*/[$startmonth-$month]*/[$startday-$day]*/*-{00,06,12,18}-00.jpg /lemontree/tmp
#for i in `ls /lemontree/[2020-2020]*/[08-08]*/[01-08]*/*-{00,06,12,18}-00.jpg`; do cp $i /lemontree/tmp; done
#ls /lemontree/tmp/
name=weekly-$year-$month-$day-$(date +%H-%M)
#cd $path
cd /lemontree/$year/$month/
ffmpeg -framerate 1 -pattern_type glob -i "/lemontree/tmp/*.jpg" -c:v libx264 -pix_fmt yuv420p $name.mp4
rm -rf /lemontree/tmp
#cd /lemontree
