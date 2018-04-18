# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('127.0.0.1', port))

print s.recv(1024)

response = ""
guess = ""
while response != "You guessed correct! the number was {}, closing connection".format(guess):

    guess = raw_input("type your guess: ")

    s.send(guess)

    # receive data from the server
    response = s.recv(1024)
    print response
# close the connection
s.close()
