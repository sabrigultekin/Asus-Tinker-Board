import ASUS.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.ASUS)

relay = 161

GPIO.setup(relay,GPIO.OUT)
GPIO.output(relay,GPIO.LOW)

try:
	print "Welcome to my software"
	while True:
		data = input("Please enter data(1-2-3) ")
		if data == 1:
			print "open"
			GPIO.output(relay,GPIO.HIGH)
		elif data == 2:
			print "close"
			GPIO.output(relay,GPIO.LOW)
		elif data == 3:
			print "blink"
			for i in range(3):
				GPIO.output(relay,GPIO.HIGH)
				time.sleep(0.5)
				GPIO.output(relay,GPIO.LOW)
				time.sleep(0.5)
		else:
			print "wrong key, please enter -1-2-3-"
except KeyboardInterrupt:
	GPIO.cleanup()
	print "  Goodbye  "
