#!/usr/bin/python3
# Gerrit Polder, PA3BYA, Oktober 2014
# point and shoot sstv camera, transmits image data
# on 144.5 MHz using SSTV

import time
import subprocess
import sys
from time import sleep
from random import randint
import pifacecad
import pifacecad.tools
from pifacecad.lcd import LCD_WIDTH


class SSTVCam(object):
	def __init__(self, mycall):
		self.listener = pifacecad.SwitchEventListener()
		self.listener.register(0, pifacecad.IODIR_ON, self.grab_and_transmit)
		self.listener.activate()  
		
		self.cad = pifacecad.PiFaceCAD()
		self.mycall = mycall
		self.active = False
		self.cad.lcd.clear()
		self.theircall = "PA0NUL"
		self.cad.lcd.write("SSTVCam " + self.mycall)
		self.cad.lcd.backlight_on()
		self.cad.lcd.cursor_off()
		self.cad.lcd.blink_off()

		
	def start(self):
		while True:
			self.get_calls()
			self.update_display()
			sleep(5)

	def update_display(self):
		self.cad.lcd.set_cursor(0, 0)
		self.cad.lcd.write("SSTVCam " + self.mycall)
		if not self.active:
			self.cad.lcd.set_cursor(0, 1)
			self.cad.lcd.write("to: " + self.theircall + "   ")

	def get_calls(self):
		file = open('/home/pi/pisstv/mycall', 'r')
		self.mycall = file.read().split()[0]
		file.close()
		file = open('/home/pi/pisstv/call', 'r')
		self.theircall = file.read().split()[0]
		file.close()
								
				
	def grab_and_transmit(self, event):
		self.active = True
		self.cad.lcd.set_cursor(0, 1)
		self.cad.lcd.write("grab image .....")
		command = "raspistill -t 1 --width 320 --height 256 -e png -o /tmp/image.png"
		subprocess.call(command, shell=True)
		command = "mogrify -fill yellow -stroke black -strokewidth 1 -pointsize 30 -draw \"text 10,40 '" + self.mycall + " to " + self.theircall + "'\" /tmp/image.png"
		subprocess.call(command, shell=True)
		localtime = time.strftime("%b %d %Y %H:%M:%S", time.localtime(time.time()) )
		command = "mogrify -fill cyan -stroke black -strokewidth 1 -pointsize 20 -draw \"text 10,240 '" + localtime + "'\" /tmp/image.png"
		subprocess.call(command, shell=True)

		self.cad.lcd.set_cursor(0, 1)
		self.cad.lcd.write("encode image ...")
		command = "/home/pi/pisstv/pisstv /tmp/image.png 22050"
		subprocess.call(command, shell=True)
		self.cad.lcd.set_cursor(0, 1)
		self.cad.lcd.write("transmit image .")
		command = "sudo /home/pi/pisstv/pifm_sstv /tmp/image.png.wav"
		subprocess.call(command, shell=True)
		command = "rm /tmp/image.png*"
		subprocess.call(command, shell=True)
		self.active = False
		self.cad.lcd.clear()



if __name__ == "__main__":
	sstvcam = SSTVCam("PA3BYA")
	sstvcam.start()