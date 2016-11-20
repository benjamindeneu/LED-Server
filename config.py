#IMPORT REQUIRED LIBS
import pigpio
import socket
import subprocess
import os
import signal
from subprocess import call
from subprocess import Popen, PIPE
import shlex

#NETWORK SETTINGS
SERVER_IP = "192.168.0.234"
SERVER_PORT = 12345

#MAXIMUM OF BRIGHTNESS
MAX_BRIGHTNESS = 255

#IO-PIN SETUP
RED_PIN   = 17
GREEN_PIN = 22
BLUE_PIN  = 24

#PORCESS ID OF SUBPROCESSES, USED FOR EFFECTS
iCurrentPid = 0

#PIGPIO OBJECT TO SWITCH/DIM LED CHANNELS
pi = pigpio.pi()
