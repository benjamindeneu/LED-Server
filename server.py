import socket
import pigpio
import subprocess
import os
import signal
from subprocess import call
from subprocess import Popen, PIPE
import shlex

pi = pigpio.pi()

bright = 255

RED_PIN   = 17
GREEN_PIN = 22
BLUE_PIN  = 24

iCurrentPid = 0

def startProcess(path):
        process = subprocess.Popen(shlex.split(path), shell=False)
        return process.pid

def killProcess(processId):
        if processId:
                try:
                        os.kill(processId, signal.SIGTERM)
                except OSError:
                        print("UNABLE TO KILL: " + str(processId))
                        return False
                else:
                        return True

#START SOCKET
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('192.168.0.234', 12345))
serversocket.listen(5) # become a server socket, maximum 5 connections

def setLights(pin, brightness):
        realBrightness = int(int(brightness) * (float(bright) / 255.0))
        pi.set_PWM_dutycycle(pin, realBrightness)

def setRGB(r,g,b):
        setLights(RED_PIN, r)
        setLights(GREEN_PIN, g)
        setLights(BLUE_PIN,b)

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if len(buf) > 0:

        #COPS EFFECT
        if buf == "COPS":
                killProcess(iCurrentPid)
                iCurrentPid = startProcess("python ./cops.py")

        aRGB = buf.split(',')
        if len(aRGB) == 3:
                killProcess(iCurrentPid)
                r = int(aRGB[0])
                g = int(aRGB[1])
                b = int(aRGB[2])
                setRGB(r,g,b)

