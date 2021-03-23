import RPi.GPIO as GPIO

#setup
GPIO.setmode(GPIO.BCM)

#pin_setup

GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.IN)


def left():
	GPIO.output(18,GPIO.HIGH)
	GPIO.output(17,GPIO.LOW)
	GPIO.output(27,GPIO.LOW)
	GPIO.output(22,GPIO.LOW)

def right():
	GPIO.output(17,GPIO.HIGH)
	GPIO.output(18,GPIO.LOW)
	GPIO.output(27,GPIO.LOW)
	GPIO.output(22,GPIO.LOW)

def forward():
	GPIO.output(18,GPIO.HIGH)
	GPIO.output(17,GPIO.HIGH)
	GPIO.output(27,GPIO.LOW)
	GPIO.output(22,GPIO.LOW)

def backward():
	GPIO.output(27,GPIO.HIGH)
	GPIO.output(22,GPIO.HIGH)
	
def stop():
	GPIO.output(18,GPIO.LOW)
	GPIO.output(17,GPIO.LOW)
	GPIO.output(27,GPIO.LOW)
	GPIO.output(22,GPIO.LOW)
	#GPIO.cleanup()
while True:

	data_r = GPIO.input(23)
	data_l = GPIO.input(24)

	if data_r == 1 and data_l != 1:
		left()
	elif data_l == 1 and data_r != 1:
		right()

	elif data_r == 0 and data_l == 0:
		forward()
		
	elif data_l == 1 and data_r == 1:
		stop()
				
GPIO.cleanup()
