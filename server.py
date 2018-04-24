'''
server.py
A program to facilitate a guessing game between a client and server using sockets
Nate Weeks, April 2018
'''

# first of all import the socket library and random library
import socket
import random

# next create a socket object
s = socket.socket()
print "Socket successfully created"

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print "socket binded to %s" %(port)

# put the socket into listening mode, accept 5 connections
s.listen(5)
print "socket is listening"

# method accept a connection from a clientsocket at a given address
(clientsocket, addr) = s.accept()

# create a random number for the guessing game
random_number = random.randint(0, 6)
print "the number is {}".format(random_number)

clientsocket.send("hello, lets play a guessing game, pick a number 1-6")
for i in range(1, 7): # max of 6 guesses
    data = clientsocket.recv(1024)  # 1024 bytes
    if data == str(random_number):  # break and close connection upon successful guess
        clientsocket.send("You guessed correct! the number was {}, closing connection".format(data))
        break
    clientsocket.send("Guess {}: {} Not correct!\n".format(i, data))

clientsocket.close()
