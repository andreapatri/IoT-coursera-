import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

pwm = GPIO.PWM(12, 50)
GPIO.output(12, False)
pwm.start(0)

for i in range(0, 50,2):
        print (i)
        pwm.ChangeDutyCycle(i)
        time.sleep(0.1)

print ("down")
for i in range(50, 0, -1):
        print (i)
        pwm.ChangeDutyCycle(i)
        time.sleep(0.1)















        
