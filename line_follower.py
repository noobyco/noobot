import RPi.GPIO as GPIO

#setmode
GPIO.setmode(GPIO.BCM)

#pin_setup for motors.

GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)

pwm_right = GPIO.PWM(25,100)
pwm_left = GPIO.PWM(8,100)
pwm_right.start(0)
pwm_left.start(0)



#Pin setup for IR sensor.

GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.IN)


def left():
	GPIO.output(18,GPIO.HIGH)
	GPIO.output(17,GPIO.LOW)
	GPIO.output(27,GPIO.LOW)
	GPIO.output(22,GPIO.LOW)
	pwm_left.ChangeDutyCycle(50)
	pwm_right.ChangeDutyCycle(50)

def right():
	GPIO.output(17,GPIO.HIGH)
	GPIO.output(18,GPIO.LOW)
	GPIO.output(27,GPIO.LOW)
	GPIO.output(22,GPIO.LOW)
	pwm_right.ChangeDutyCycle(50)
	pwm_left.ChangeDutyCycle(50)

def forward():
	GPIO.output(18,GPIO.HIGH)
	GPIO.output(17,GPIO.HIGH)
	GPIO.output(27,GPIO.LOW)
	GPIO.output(22,GPIO.LOW)
	pwm_left.ChangeDutyCycle(50)
	pwm_right.ChangeDutyCycle(50)

def backward():
	#Not Currently used.
	GPIO.output(27,GPIO.HIGH)
	GPIO.output(22,GPIO.HIGH)
	pwm_left.ChangeDutyCycle(50)
	pwm_right.ChangeDutyCycle(50)
		
def stop():
	GPIO.output(18,GPIO.LOW)
	GPIO.output(17,GPIO.LOW)
	GPIO.output(27,GPIO.LOW)
	GPIO.output(22,GPIO.LOW)
	
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
