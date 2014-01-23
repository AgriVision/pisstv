#!/bin/bash
# sstv camera, Gerrit Polder, PA3BYA
raspistill -t 1 --width 320 --height 256 -e png -o /tmp/image.png
# add callsign, something like
mogrify /tmp/image.png -pointsize 48 -draw "text 10,250 'call'"
./pisstv /tmp/image.png 22050
sudo ./pifm_sstv /tmp/image.png.wav
rm /tmp/image.png*