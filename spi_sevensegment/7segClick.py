import ASUS.GPIO as GPIO
import spidev #spi library
from time import sleep
from array import *


SegmentTable=[
	0x7E, #0
	0x0A, #1
	0xB6, #2
	0x9E, #3
	0xCA, #4
	0xDC, #5
	0xFC, #6
	0x0E, #7
	0xFE, #8
	0xDE, #9
]

GPIO.setwarnings(False)

speed = 1000000 #1Mhz
CS    = 0

## spi settings
spi = spidev.SpiDev()
spi.open(2,CS)
spi.max_speed_hz=speed
spi.mode = 0b00

##setup gpio
PWM = 252
RST = 253

GPIO.setmode(GPIO.ASUS)
GPIO.setup(PWM,GPIO.OUT)
GPIO.output(PWM,GPIO.HIGH)
GPIO.setup(RST,GPIO.OUT)

##send data
def sendData(val1,val2):
	spi.xfer2([val1])
	spi.xfer2([val2])
	print 'data send successfuly'

##NumberTo7segValue
def NumTo7segValue(Digit):
	if (Digit >= 0) and (Digit <= 9):
		return SegmentTable[Digit]
	else:
		print 'Please Enter Digit'
		return 0

try:
	print 'Welcome'
	GPIO.output(RST,GPIO.LOW)
	sleep(1)
	GPIO.output(RST,GPIO.HIGH)
	GPIO.output(PWM,GPIO.HIGH)
	while True:
		number = input('Please Enter Number(0-99): ')
		if(number>99 or number < 0):
			print 'Please dont wrong'
		else:
			birler = NumTo7segValue(number%10)
			onlar  = NumTo7segValue(number/10)
			print 'Birler Basamagi ',birler
			print 'Onlar Basamagi ',onlar
			sendData(birler,onlar)
		sleep(1)
except (KeyboardInterrupt, Exception) as e :
	print e
	GPIO.output(RST,GPIO.LOW)
	GPIO.output(PWM,GPIO.LOW)
	print 'Good bye my friend'
	spi.close()
