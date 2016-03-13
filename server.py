import socket
import pigpio

pi = pigpio.pi()

bright = 255

RED_PIN   = 17
GREEN_PIN = 22
BLUE_PIN  = 24

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
        aRGB = buf.split(',')
        if len(aRGB) == 3:
                r = int(aRGB[0])
                g = int(aRGB[1])
                b = int(aRGB[2])
                setRGB(r,g,b)

