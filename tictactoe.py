import random

class TicTacToe(object):
    def __init__(self):
        self.board = [["1","2","3"],["4","5","6"],["7","8","9"]]
        self.moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def printBoard(self):
        for row in self.board:
            print(row)

    def getBoard(self):
        return self.board

    def pickMove(self, move, type):
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
        move = random.choice(self.moves)
        return move

    def checkWinner(self):
        winning_moves = [[(0,0), (0,1), (0,2)],[(1,0), (1,1), (1,2)],[(2,0), (2,1), (2,2)],[(0,0), (1,0), (2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)], [(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]
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

    def playGame(self):
        while self.checkWinner() == "tie" and self.moves != []:
            print("pick a move 1-9")
            self.printBoard()
            move = input()
            while not self.pickMove(move, "player"):
                print("invalid move")
                print("pick a move 1-9")
                self.printBoard()
                move = input()
            if self.moves != [] and self.checkWinner() == "tie":
                computerMove = self.pickComputerMove()
                self.pickMove(computerMove, "computer")
            else:
                break

        print(self.checkWinner())
        self.printBoard()

game = TicTacToe()
game.playGame()
