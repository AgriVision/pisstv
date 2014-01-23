pisstv is an attemp to use the Raspberry Pi as a slow scan television (SSTV) camera.
Its intended for use by ham radio amateurs.

It mainly consists of three commands.

raspistill: to grab the inage from the camera.
pisstv: to convert the image to a soundfile.
pifm_sstv: to transmit the soundfile over the air, e.g. on 144.5 MHz

pisstv is heavilly based on work from KI4MCW, which can be found here: https://sites.google.com/site/ki4mcw/Home/sstv-via-uc
I fixed some errors and made it a little bit more flexible.

pifm_sstv is based on the work of Oliver Mattos and Oskar Weigl  (http://www.icrobotics.co.uk/wiki/index.php/Turning_the_Raspberry_Pi_Into_an_FM_Transmitter).

The original program was intended for transmitting broadband stereo signals.
I adapted it a little bit so that the bandwidth can be set, which is very important for narrow-band ham radio transmissions. Also the timing can be tuned from the command-line, which is important for SSTV, where impropper timing results in slanted images.

