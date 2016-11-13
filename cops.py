import RPi.GPIO as GPIO
import time
import pigpio
from thread import start_new_thread

RED_PIGPIO = 17
GREEN_PIGPIO = 22
BLUE_PIGPIO = 24

pi = pigpio.pi()

def setRGB(r,g,b):
        pi.set_PWM_dutycycle(RED_PIGPIO, r)
        pi.set_PWM_dutycycle(GREEN_PIGPIO, g)
        pi.set_PWM_dutycycle(BLUE_PIGPIO, b)
        return

def cops(sleepTime):
        setRGB(255,0,0)
        time.sleep(sleepTime)
        setRGB(0,0,255)
        time.sleep(sleepTime)
        return

while 1:
        cops(0.5)
