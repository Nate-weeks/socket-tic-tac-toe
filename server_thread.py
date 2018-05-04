'''
server_thread.py
A program to set up a socket server to play blackjack with a client in a
multi-threaded environment
Nate Weeks, April 2018
'''

from threading import Thread
from game import *
import socket
import random

def initiateSocket():
    ''' function to initiate a socket and spawn a thread for each connection to run'''
    port = 12345
    server = socket.socket()
    server.bind(('', port))
    print "listening on port {}".format(port)
    while True:
        server.listen(1)
        (clientsocket, addr) = server.accept()
        thread1 = Thread(target=initiateGame, args=(clientsocket, ))
        thread1.start()

def main():
    initiateSocket()

if __name__=='__main__':
    import doctest
    doctest.testmod()
    main()
