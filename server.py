from config import *
from led_functions import *
from process_functions import *

#START SOCKET
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((SERVER_IP, SERVER_PORT))
#START LISTENING, MAX 5 CLIENTS
serversocket.listen(5)

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

