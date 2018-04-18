# first of all import the socket library
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

# put the socket into listening mode
s.listen(5)
print "socket is listening"

(clientsocket, addr) = s.accept()

random_number = random.randint(0, 6)
print "the number is {}".format(random_number)

clientsocket.send("hello, lets play a guessing game, pick a number 1-6")
for i in range(1, 6): # max of 6 guesses
    data = clientsocket.recv(1024)  # what is this 10? bytes?
    if data == str(random_number):
        clientsocket.send("You guessed correct! the number was {}, closing connection".format(data))
        break
    clientsocket.send("Guess {}: {}\n".format(i, data))

clientsocket.close()
#
# a forever loop until we interrupt it or
# an error occurs
# while True:
#
#    # Establish connection with client.
#    c, addr = s.accept()
#    print 'Got connection from', addr
#    print c.recv(1024)
#    # send a thank you message to the client.
#    c.send('Thank you for connecting')
#
#    # Close the connection with the client
#    c.close()
