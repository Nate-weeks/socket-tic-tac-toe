'''
client.py
A program to facilitate a game of blackjack between a client and server using sockets
Nate Weeks, April 2018
'''

# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('127.0.0.1', port))

# print received data until client response is s for stand
response = "h"
# print hello welcome to a game of blackjack
print s.recv(1024)
# loop to hit or stand based on blackjack score
while response != "s":
    print s.recv(1024)
    response = raw_input()
    s.send(response)
# print the winner of the game
print s.recv(1024)
s.close()
