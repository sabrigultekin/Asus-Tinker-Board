import ASUS.GPIO as GPIO
import time

GPIO.setmode(GPIO.ASUS)
GPIO.setwarnings(False)

myservo = 238

GPIO.setup(myservo,GPIO.OUT)
pwm = GPIO.PWM(myservo,50) # 50hz yani 20mslik periyod
pwm.start(2.5) # 0 derece

try:
	while True:
		print "0 derece"
		pwm.ChangeDutyCycle(2.5) #0 derece
		time.sleep(1) # wait 1sec
		print "90 derece"
		pwm.ChangeDutyCycle(7.5) #90 derece
		time.sleep(1)
		print "180 derece"
		pwm.ChangeDutyCycle(12.5) #180 derece
		time.sleep(1)
		print "90 derece"
		pwm.ChangeDutyCycle(7.5)
		time.sleep(1)
except KeyboardInterrupt:
	print "Hoscakal canim"
	GPIO.cleanup()

