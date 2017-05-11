import ASUS.GPIO as GPIO
import spidev
from time import sleep

#spi
spi = spidev.SpiDev()
spi.open(2,0)
spi.max_speed_hz = 1000000 #1Mhz
CS = 17

#gpio
GPIO.setwarnings(False)
GPIO.setmode(GPIO.ASUS)
GPIO.setup(CS,GPIO.OUT)
GPIO.output(CS,GPIO.LOW)

#adc read value function
#read value length 12bit
def GetCH0():
	GPIO.output(CS,GPIO.LOW) #start
	spi.writebytes([0x06])
	temp = spi.readbytes(0x00)[0] & 0x0F # 0000 1111
	temp = temp << 8 # yyyy 0000 0000
	temp = temp | spi.readbytes(0)[0]
	sleep(0.0001)
	GPIO.output(CS,GPIO.HIGH) #stop
	return temp

try:
	print 'Welcome, reading CH0 port'
	while True:
		adc_value = GetCH0() # 0-4095
		print "adc value => ",adc_value
		#adc to volt value
		volt_value = adc_value*5/4095.0
		print "volt value => ",format(volt_value,'.1f'),"V"
		sleep(0.5) # 500ms wait
except KeyboardInterrupt:
	GPIO.cleanup()
	spi.close()
	print "Good by my hooney"
