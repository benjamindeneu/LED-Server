import select
import socket
import pigpio

#NETWORK SETTINGS
SERVER_IP = ""
SERVER_PORT = 12345

#IO-PIN SETUP
RED_PIN   = 17
GREEN_PIN = 22
BLUE_PIN  = 24

#PIGPIO OBJECT TO SWITCH/DIM LED CHANNELS
pi = pigpio.pi()

#MAXIMUM OF BRIGHTNESS
MAX_BRIGHTNESS = 255

led_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
led_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
led_socket.bind((SERVER_IP, SERVER_PORT))
led_socket.listen(5)

print "LED SERVER STARTED AT " + SERVER_IP + " ON PORT: " + str(SERVER_PORT)

def setLights(pin, brightness):
        realBrightness = int(int(brightness) * (float(MAX_BRIGHTNESS) / 255.0))
        pi.set_PWM_dutycycle(pin, realBrightness)

def setRGB(r,g,b):
        setLights(RED_PIN, r)
        setLights(GREEN_PIN, g)
        setLights(BLUE_PIN,b)


def setRGB(r,g,b):
        setLights(RED_PIN, r)
        setLights(GREEN_PIN, g)
        setLights(BLUE_PIN,b)

read_list = [led_socket]
while True:
    readable, writable, errored = select.select(read_list, [], [])
    for s in readable:
        if s is led_socket:
            client_socket, address = led_socket.accept()
            read_list.append(client_socket)
            #print "Connection from", address
        else:
            data = s.recv(64)
            if data:
                aRGB = data.split(',')
                if len(aRGB) == 3:
                        r = int(aRGB[0])
                        g = int(aRGB[1])
                        b = int(aRGB[2])
                        setRGB(r,g,b)
            else:
                s.close()
                read_list.remove(s)

