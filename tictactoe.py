'''
Program to facilitate a game of TicTacToe over a client/socket connection
By Nate Weeks, April 2019
'''

import random

class TicTacToe(object):
    '''Object to play a game of TicTacToe, initializes the board and a list of legal computer moves'''
    def __init__(self, clientsocket):
        self.board = [["1","2","3"],["4","5","6"],["7","8","9"]]
        self.moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.clientsocket = clientsocket

    def printBoard(self):
        '''sends the board to client as a string'''
        board = ""
        for row in self.board:
            board += "\n"
            board += str(row)
        self.clientsocket.send(board)
        response = self.clientsocket.recv(1024)
        while response != "confirmed":
            self.clientsocket.send(board)
            response = self.clientsocket.recv(1024)

    def pickMove(self, move, type):
        '''picks a move and determines it's validity based on what's been picked
        already and what the user inputs - computer picks from only a list of valid
        moves - takes a move and a "type" - computer or player, removes the move
        from the list of valid moves'''
        if move in self.moves:
            self.moves.remove(move)
        if move == "1" and self.board[0][0] == "1":
            if type == "player":
                self.board[0][0] = "X"
            else:
                self.board[0][0] = "O"
            return True
        elif move == "2" and self.board[0][1] == "2":
            if type == "player":
                self.board[0][1] = "X"
            else:
                self.board[0][1] = "O"
            return True
        elif move == "3" and self.board[0][2] == "3":
            if type == "player":
                self.board[0][2] = "X"
            else:
                self.board[0][2] = "O"
            return True
        elif move == "4" and self.board[1][0] == "4":
            if type == "player":
                self.board[1][0] = "X"
            else:
                self.board[1][0] = "O"
            return True
        elif move == "5" and self.board[1][1] == "5":
            if type == "player":
                self.board[1][1] = "X"
            else:
                self.board[1][1] = "O"
            return True
        elif move == "6" and self.board[1][2] == "6":
            if type == "player":
                self.board[1][2] = "X"
            else:
                self.board[1][2] = "O"
            return True
        elif move == "7" and self.board[2][0] == "7":
            if type == "player":
                self.board[2][0] = "X"
            else:
                self.board[2][0] = "O"
            return True
        elif move == "8" and self.board[2][1] == "8":
            if type == "player":
                self.board[2][1] = "X"
            else:
                self.board[2][1] = "O"
            return True
        elif move == "9" and self.board[2][2] == "9":
            if type == "player":
                self.board[2][2] = "X"
            else:
                self.board[2][2] = "O"
            return True
        else:
            return False

    def pickComputerMove(self):
        '''randomly generates a computer move by picking one element from the
        array of valid moves'''
        move = random.choice(self.moves)
        return move

    def checkWinner(self):
        '''checks all the winning patterns to see if anybody has gotten 3 in a row
        returns a string that declares the winner'''
        winning_moves = [[(0,0), (0,1), (0,2)],[(1,0), (1,1), (1,2)],[(2,0), (2,1), (2,2)],[(0,0), (1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)], [(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]
        for set in winning_moves:
            playerWinCount = 0
            computerWinCount = 0
            for move in set:
                if self.board[move[0]][move[1]] == "X":
                    playerWinCount += 1
                if self.board[move[0]][move[1]] == "O":
                    computerWinCount += 1
            if playerWinCount == 3:
                return "player wins"
            if computerWinCount == 3:
                return "computer wins"
        return "tie"

    def getMove(self):
        '''gets an input from the user connected as a client to declare as their
        move, re-prompts the user if they select an invalid move'''
        self.clientsocket.send("pick a move 1-9, board is:")
        response = self.clientsocket.recv(1024)
        while response != "confirmed":
            self.clientsocket.send("pick a move 1-9, board is:")
        self.printBoard()
        move = self.clientsocket.recv(1024)
        while not self.pickMove(move, "player"):   #check if the move is valid
            self.clientsocket.send("invalid move\npick a move 1-9, board is:")
            response = self.clientsocket.recv(1024)
            while response != "confirmed":
                self.clientsocket.send("pick a move 1-9, board is:")
            self.printBoard()
            move = self.clientsocket.recv(1024)
        return move


    def playGame(self):
        '''calls functions to facilitate a game of TicTacToe'''
        while self.checkWinner() == "tie" and self.moves != []:
            self.getMove()
            if self.moves != [] and self.checkWinner() == "tie": # check if nobody has won and there are still open spaces
                computerMove = self.pickComputerMove()
                self.pickMove(computerMove, "computer")
            else:
                break

        self.clientsocket.send(self.checkWinner())
        response = self.clientsocket.recv(1024)
        while response != "confirmed":
            self.clientsocket.send(self.checkWinner())
        self.printBoard()

def initiateGame(clientsocket):
    '''takes a clientsocket connection and opens a game of TicTacToe - called from
    server_thread.py'''
    game = TicTacToe(clientsocket)
    game.playGame()

def main():
    initiateGame()

if __name__=='__main__':
    import doctest
    doctest.testmod()
    main()
