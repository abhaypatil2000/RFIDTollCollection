import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

try:
	i,txt =reader.read()
	print(i)
	print(txt)
finally:
	GPIO.cleanup()
