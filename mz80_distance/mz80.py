import ASUS.GPIO as GPIO
from time import sleep

mz80 = 252
GPIO.setwarnings(False)
GPIO.setmode(GPIO.ASUS)
GPIO.setup(mz80,GPIO.IN)


try:
	while True:
		if not GPIO.input(mz80):
			print "*** distance in ***"
		else:
			print "distance out"
		sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()
	print "Good bye my love"
