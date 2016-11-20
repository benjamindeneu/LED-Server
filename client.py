import config
from config import *

import socket

while True:
        try:
                mode = raw_input('Enter RGB (0 - 255) R;G;B:')
        except ValueError:
                print "Not a number"

        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect(('localhost', 12345))
        clientsocket.send(str(mode))
        clientsocket.close()




