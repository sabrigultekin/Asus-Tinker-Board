import ASUS.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.ASUS)


RED    = 164
YELLOW = 166
GREEN  = 167

GPIO.setup(RED,GPIO.OUT)
GPIO.setup(YELLOW,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)

try:
	while True:
		#open led
		print "open led"
		GPIO.output(RED,GPIO.HIGH)
                GPIO.output(YELLOW,GPIO.HIGH)
                GPIO.output(GREEN,GPIO.HIGH)
		time.sleep(0.5) #500ms
		#close led
		print "close led"
		GPIO.output(RED,GPIO.LOW)
                GPIO.output(YELLOW,GPIO.LOW)
                GPIO.output(GREEN,GPIO.LOW)
                time.sleep(0.5) #500ms
except KeyboardInterrupt:
	GPIO.cleanup()
