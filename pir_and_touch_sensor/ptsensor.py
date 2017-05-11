import ASUS.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.ASUS)


RED    = 164
YELLOW = 166
GREEN  = 167

PirSensor   = 257
TouchSensor = 256


GPIO.setup(RED,GPIO.OUT)
GPIO.setup(YELLOW,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)

GPIO.setup(PirSensor,GPIO.IN)
GPIO.setup(TouchSensor,GPIO.IN)

try:
	while True:
		if(GPIO.input(PirSensor)):
			GPIO.output(RED,GPIO.HIGH)
                        GPIO.output(YELLOW,GPIO.HIGH)
                        GPIO.output(GREEN,GPIO.HIGH)
			print "***** pir sensor activated *****"
		if(GPIO.input(TouchSensor)):
                        GPIO.output(RED,GPIO.LOW)
                        GPIO.output(YELLOW,GPIO.LOW)
                        GPIO.output(GREEN,GPIO.LOW)
			print "+++++ touch sensor activated +++++"
		time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()

