Socket-Tic-Tac-Toe
===========

running this software
=========

* Clone the repo from [https://github.com/Nate-weeks/socket-tic-tac-toe](https://github.com/Nate-weeks/socket-tic-tac-toe)
* run the server in one tab: python server_thread.py
* run the client in another tab: python client.py

Specifications
===========

* Run in python 2.7
* I mostly used the defaults from the python 2.7 socket library [https://docs.python.org/2/library/socket.html](https://docs.python.org/2/library/socket.html)
* I used the Thread object from the python 2 threading library [https://docs.python.org/2/library/threading.html](https://docs.python.org/2/library/threading.html)

Sources
=========

A general outline of my code came from work I did on a socket black-jack game last year.  I didn't actually look up any sources for this project.

General Architecture
==========

Server_thread.py listens on port 12345 for an incoming connection.  When it receives a connection, it creates a new thread to handle the incoming connection, and initiates an instance of a TicTacToe game through the initiateGame() method.  When a client from client.py connects to the server, it just receives some text asking to choose a move and an image of the board.  Moves are chosen with an integer 1-9 and represented as 3 nested arrays.  After each transmission the tictactoe game waits for a "confirmed" message from the client before moving on to the next transmission.  It also validates each move and asks for a different move if the move is already taken or anything other than 1-9.  Right now I just have the player going first every time and the computer choosing random moves.  It wouldn't be hard to decide randomly who goes first but it would take a bit of overhauling the order of communication between client and server.  Time permitting I would also like to have a smarter computer algorithm.

Testing
========

I used the test-server and test-client that loop through client-server interactions allowing me to type each message by hand.  I checked what would happen with unexpected responses to the client or to the server and handled for most cases.  Right now I have it set that each time the client receives incorrect data it will send "unconfirmed" and wait for the proper response.  This works well for bad inputs but I realize this is flawed, if either side sends nothing the program will just hang.  If I had more time I would re-factor the client to wait for a response on a set timer, then send an unconfirmed message after a few seconds, and try that a few times before eventually closing the connection.

Example output
=========

* run the server in one window with python server_thread.py
* run the client in another window:

```
python client.py
pick a move 1-9, board is:

['1', '2', '3']
['4', '5', '6']
['7', '8', '9']
1
pick a move 1-9, board is:

['X', '2', '3']
['4', 'O', '6']
['7', '8', '9']
4
pick a move 1-9, board is:

['X', '2', '3']
['X', 'O', '6']
['O', '8', '9']
0
invalid move
pick a move 1-9, board is:

['X', '2', '3']
['X', 'O', '6']
['O', '8', '9']
2
pick a move 1-9, board is:

['X', 'X', '3']
['X', 'O', 'O']
['O', '8', '9']
3
player wins

['X', 'X', 'X']
['X', 'O', 'O']
['O', '8', '9']
```
