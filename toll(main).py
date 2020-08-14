import RPi.GPIO as GPIO
import SimpleMFRC522
from datetime import datetime
import time

def Read(reader, dict, id2, pwm):
	id, name = reader.read()
	if((id2)!=(id)):
		print('id: '+ str(id))
		if id not in dict.keys():
			dict[id] = 500
		else:
			if dict[id]>=50:
				amnt = dict[id]
				amnt -= 50
				dict[id] = amnt
				pwm.start(5.0)
				time.sleep(1)
				barrierUp(pwm)
				time.sleep(1)
			else:
				amnt = dict[id]
				print('Not Enough Balance, Please Recharge!')
				dict[id] = 300

		print('name: ' + str(name))	
		print('avlBal: ' + str(dict[id]))
		print(datetime.now().time())
		print('')
                time.sleep(1)
		pwm.start(2.0)
                barrierDown(pwm)
		time.sleep(1)
		return int(id)

def barrierUp(pwm):
	duty1 = 3.5
	duty2 = 18.5
	pwm.ChangeDutyCycle(duty1)
	time.sleep(0.8)

def barrierDown(pwm):
	duty1 = 3.5
	duty2 =18.5
	pwm.ChangeDutyCycle(duty2)
	time.sleep(0.8)

def main():
	dict={}
	reader = SimpleMFRC522.SimpleMFRC522()

	servoPin = 33
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(servoPin, GPIO.OUT)
	pwm = GPIO.PWM(servoPin,100)
	#pwm.start(5.0)
	id2=0
	try:
		while True:
			id1 = Read(reader, dict ,id2, pwm)
			id2 = id1
	except KeyboardInterrupt:
		GPIO.cleanup()

if __name__ == '__main__':
	main()
