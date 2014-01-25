#!/usr/bin/env python
# Gerrit Polder, PA3BYA, Januari 2014
# Endless loop, wait for Image change, then transmits image data
# on 144.5 MHz using SSTV

import time
import subprocess
import StringIO
from PIL import Image, ImageFont, ImageDraw

mycallsign = "MYCALL" # ham radio callsign
threshold = 10
sensitivity = 400
DEBUG = True

font = ImageFont.load_default()
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf", 24)

# Capture an image
def captureImage():
	command = "raspistill -w %s -h %s -t 1 -e png -o -" % (320, 256)
	imageData = StringIO.StringIO()
	imageData.write(subprocess.check_output(command, shell=True))
	imageData.seek(0)
	image = Image.open(imageData)
	buffer = image.load()
	imageData.close()
	return image, buffer

# transmit image in sstv
def transmitImage(im):
	draw = ImageDraw.Draw(im)
	localtime = time.strftime("%b %d %Y %H:%M:%S", time.localtime(time.time()) )
	draw.text((10, 10), mycallsign , (0,0,0), font=font)
	draw.text((10, 220), localtime, (0,0,0), font=font)
	im.save("/tmp/image.png")
	command = "./pisstv /tmp/image.png 22050"
	subprocess.call(command, shell=True)
	command = "sudo ./pifm_sstv /tmp/image.png.wav"
	subprocess.call(command, shell=True)
	command = "rm /tmp/image.png*"
	subprocess.call(command, shell=True)

# grab initial image
img, buf = captureImage()

# loop forever
while (True):
	if (DEBUG):
		print(time.strftime("%b %d %Y %H:%M:%S", time.localtime(time.time()) ))
	# grab comparison image
	imgnew, bufnew = captureImage()

	# Count changed pixels
	changedPixels = 0
	for x in xrange(0, 320):
		for y in xrange(0, 256):
			# Just check red channel as it's dominant for PiCam NoIR
			pixdiff = abs(buf[x,y][0] - bufnew[x,y][0])
			if pixdiff > threshold:
				changedPixels += 1
	if (DEBUG):
		print(changedPixels)
		
	# Transmit an image if pixels changed
	if changedPixels > sensitivity:
		# Swap comparison buffers
		img = imgnew
		buf = bufnew
		transmitImage(img.copy())

