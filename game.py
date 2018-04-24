'''
game.py
A program to play and keep track of a game of blackjack
Nate Weeks, April 2018
'''
from hand import *

class Game(object):
    '''Object to play a game of blackjack, initializes the
    player_hand, computer_hand and deck of cards'''
    def __init__(self, clientsocket):
        self.deck = Deck()
        self.player_hand = Hand(self.deck.deal(), self.deck.deal())
        self.computer_hand = Hand(self.deck.deal(), self.deck.deal())
        self.clientsocket = clientsocket

    def getPlayerHand(self):
        '''returns the player_hand'''
        return self.player_hand

    def getComputerHand(self):
        '''returns the computer_hand'''
        return self.computer_hand

    def dealPlayer(self):
        '''deals the player and plays out the hand, asking to hit or stand
        and printing out the score and cards contained in the players hand'''
        self.clientsocket.send("hello, let's play a game of blackjack, you were dealt the {}, your score is {}".format(self.getPlayerHand().getString(), self.getPlayerHand().score()))
        self.hitOrStand()

    def hitOrStand(self):
        '''asks the player to hit or stand, adds a card to their hand if hit is chosen,
        handles for improper inputs and ends the loop if stand is chosen.
        '''
        VALID_RESPONSE = ["h", "s"]
        self.clientsocket.send("would you like to hit or stand? (h or s)")
        response = self.clientsocket.recv(1024)
        while response not in VALID_RESPONSE:
            self.clientsocket.send("please print a valid input, (h or s)")
            response = self.clientsocket.recv(1024)
        while response == "h":
            new_card = self.deck.deal()
            self.player_hand.addCard(new_card)
            self.clientsocket.send("you were dealt the {}, your score is {}, would you like to hit or stand?".format(new_card, self.player_hand.score()))
            response = self.clientsocket.recv(1024)
            while response not in VALID_RESPONSE:
                self.clientsocket.send("please print a valid input, (h or s)")
                response = self.clientsocket.recv(1024)

    def playComputerHand(self):
        '''plays out the dealers hand'''
        while self.computer_hand.score() <= 17:
            self.computer_hand.addCard(self.deck.deal())

    def calculateWinner(self):
        '''calculates the winner of a given game of blackjack, whoever gets over 21
        busts, whoever has the higher score wins'''
        player_score = self.player_hand.score()
        computer_score = self.computer_hand.score()
        if computer_score > 21:
            self.clientsocket.send("computer busted, player wins")
        elif player_score > 21:
            self.clientsocket.send("player busted, computer wins")
        elif player_score > computer_score:
            self.clientsocket.send("player score {}, computer score {}, player wins".format(player_score, computer_score))
        elif computer_score > player_score:
            self.clientsocket.send("player score {}, computer score {}, computer wins".format(player_score, computer_score))
        elif player_score == computer_score:
            self.clientsocket.send("player score {}, computer score {}, its a push".format(player_score, computer_score))

    def playGame(self, game):
        '''plays out a game of blackjack, single player against computer dealer'''
        game.dealPlayer()
        game.playComputerHand()
        game.calculateWinner()

def initiateGame(clientsocket):
    '''initiates the game of blackjack with a clientsocket'''
    game = Game(clientsocket)
    game.playGame(game)

def main():
    initiateGame()

if __name__=='__main__':
    import doctest
    doctest.testmod()
    main()
