#!/bin/sh
#useage: sh ./cuttingMovie.sh hoge.avi
#Atsushi 2016
echo "cutting out images from the movie $1",
if [$# -ne 1]; then
	echo "invalid num of argument!"
	exit 1
fi

rm -R images
mkdir images
#get images from 0ms to the end of movie with 25 fps.
#image names will be start from 000001.png
ffmpeg -i $1 -ss 0 -r 25 -f image2 ./images/%06d.jpg
