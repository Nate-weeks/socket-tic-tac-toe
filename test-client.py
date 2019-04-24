'''
A program to spoof outputs from a client and test the TicTacToe server
Nate Weeks, April 2019
'''

# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('127.0.0.1', port))

greeting = s.recv(1024)

print greeting

while true:
    chat = raw_input("what would you like to say?")
    s.send(chat)
    response = s.recv(1024)
