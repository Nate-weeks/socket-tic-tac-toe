from threading import Thread
import socket
from testchatgame import *

def initiateSocket():
    ''' function to initiate a socket and spawn a thread for each connection to run'''
    port = 12345
    server = socket.socket()
    server.bind(('', port))
    print "listening on port {}".format(port)
    while True:
        clients = []
        server.listen(2)
        (clientsocket, addr) = server.accept()
        clients.append(clientsocket)
        (clientsocket, addr) = server.accept()
        clients.append(clientsocket)
        thread1 = Thread(target=testchat, args=(clients,))
        thread1.start()

initiateSocket()
