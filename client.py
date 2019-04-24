'''
client.py
A program to facilitate a game of TicTacToe between a client and server using sockets
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

# get the initial ask for move 1-9
askForMove = s.recv(1024)
# loop making moves until the output declares a winner or tie
while askForMove != "tie" and askForMove != "computer wins" and askForMove != "player wins":
    if not askForMove:
        print "server not responsive, closing connection"
        s.close()
    while askForMove != "pick a move 1-9, board is:":
        s.send("uncomfirmed")
        askForMove = s.recv(1024)
    s.send("confirmed")
    print askForMove

    ## receive and print the board
    board = s.recv(1024)
    while board[0] != "\n":
        s.send("uncomfirmed")
        board = s.recv(1024)
    print board
    s.send("confirmed")

    #select a move
    move = raw_input()
    s.send(move)
    askForMove = s.recv(1024)
    ## handle for invalid move
    if askForMove == "invalid move\npick a move 1-9, board is:":
        while askForMove == "invalid move\npick a move 1-9, board is:":
            print askForMove
            s.send("confirmed")
            ## print board
            board = s.recv(1024)
            while board[0] != "\n":
                s.send("uncomfirmed")
                board = s.recv(1024)
            print board
            s.send("confirmed")
            ## send a new move
            move = raw_input()
            s.send(move)
            askForMove = s.recv(1024)

    # print the winner of the game
print askForMove
s.send("confirmed")
board = s.recv(1024)
while board[0] != "\n":
    s.send("uncomfirmed")
    board = s.recv(1024)
print board
s.send("confirmed")

s.close()
