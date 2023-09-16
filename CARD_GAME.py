#card game

import random

class Card():
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, c):
        if self.value < c.value:
            return True
        elif self.value == c.value:
            if self.suit < c.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c):
        if self.value > c.value:
            return True
        elif self.value == c.value:
            if self.suit > c.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        x = self.values[self.value] + " of " + self.suits[self.suit]
        return x

class Deck():
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(0, 4):
                self.cards.append(Card(i, j))
        random.shuffle(self.cards)

    def pick_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop() 
    
class Player():
    def __init__(self, name, card, wins):
        self.name = name
        self.card = card
        self.wins = wins

class Game():
    def __init__(self):
        name1 = input("Enter the first player: ")
        name2 = input("Enter the second player: ")
        self.deck = Deck()
        self.player1 = Player(name1, None, 0)
        self.player2 = Player(name2, None, 0)

    def play(self):
        cards = self.deck.cards
        while len(cards) >= 2:
            tmp = input("Enter any symbol")
            player1_card = self.deck.pick_card()
            player2_card = self.deck.pick_card()
            player1_name = self.player1.name
            player2_name = self.player2.name
            self.print(player1_card, player1_name, player2_card, player2_name)
        if player1_card > player2_card:
            self.player1.wins += 1
        else:
            self.player2.wins += 1
        winner = self.winner(self.player1, self.player2)
        print("Game is over. {} won!", format(winner))

    def print(self, player1_card, player1_name, player2_card, player2_name):
        s = "Player {} picks {}, when player {} picks {} \n"
        s = s.format(player1_name, player1_card, player2_name, player2_card)
        print(s)

    def winner(self, player1, player2):
        if player1.wins > player2.wins:
            print("First player won\n")
            return
        if player2.wins > player1.wins:
            print("Second player won\n")
            return
        else:
            print("Draw\n")
            return

game = Game()
game.play()