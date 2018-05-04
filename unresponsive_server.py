'''
test_server.py
A server to test various incorrect responses
Nate Weeks, April 2018
'''

import socket

# next create a socket object
s = socket.socket()
print "Socket successfully created"

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345

# Next bind to the port
s.bind(('', port))
print "socket binded to %s" %(port)

# put the socket into listening mode, accept 5 connections
s.listen(5)
print "socket is listening"

# method accept a connection from a clientsocket at a given address
(clientsocket, addr) = s.accept()
