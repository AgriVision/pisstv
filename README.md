# PiSSTV

Gerrit Polder, PA3BYA.

pisstv is an attemp to use the Raspberry Pi as a slow scan television (SSTV) camera.
Its intended for use by ham radio amateurs.

It mainly consists of three commands.

raspistill: to grab the image from the camera.
pisstv: to convert the image to a soundfile.
pifm_sstv: to transmit the soundfile over the air, e.g. on 144.5 MHz

pisstv is heavilly based on work from KI4MCW, which can be found here: https://sites.google.com/site/ki4mcw/Home/sstv-via-uc
I fixed some errors and made it a little bit more flexible.

pifm_sstv is based on the work of Oliver Mattos and Oskar Weigl  (http://www.icrobotics.co.uk/wiki/index.php/Turning_the_Raspberry_Pi_Into_an_FM_Transmitter).

The original program was intended for transmitting broadband stereo signals.
I adapted it a little bit so that the bandwidth can be set, which is very important for narrow-band ham radio transmissions. Also the timing can be tuned from the command-line, which is important for SSTV, where impropper timing results in slanted images.

sstvcatch is kind of a sstv security camera. A python script runs an endless loop, waits for image change, then transmits image data on 144.5 MHz using SSTV.

sstvcam.py is a point and shoot sstv camera. It uses the piface control and display (http://www.piface.org.uk/products/piface_control_and_display/) as user interface.

Put:
 * python3 /home/pi/pifacecad/startup.py
 * python3 /home/pi/pisstv/sstvcam.py &

At the end of your /etc/rc.local to start this software automatically at power up.

## License
All of the code contained here is licensed by the GNU General Public License v3.

## Credits
Credits to KI4MCW (sstv), Oliver Mattos and Oskar Weigl (pifm).
