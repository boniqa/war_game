# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)
import random
from random import shuffle


# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
# CARDS = []
# for x in SUITE:
#     for i in RANKS:
#         CARDS.append(x+i)


class Deck:
    def __init__(self):
        print('creating new ordered deck!')
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffleDeck(self):
        print ('shugffling deck...')
        shuffle(self.allcards)

    def splitInHalf(self):
        return(self.allcards[:26], self.allcards[26:])

    # """
    # This is the Deck Class. This object will create a deck of cards to initiate
    # play. You can then use this Deck list of cards to split in half and give to
    # the players. It will use SUITE and RANKS to create the deck. It should also
    # have a method for splitting/cutting the deck in half and Shuffling the deck.
    # """


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


    # '''
    # This is the Hand class. Each player has a Hand, and can add or remove
    # cards from that hand. There should be an add and remove card method here.
    # '''
    #


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {} ".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) <3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards

    def still_has_cards(self):
        return len(self.hand.cards) != 0


    # """
    # This is the Player class, which takes in a name and an instance of a Hand
    # class object. The Payer can then play cards and check if they still have cards.
    # """

#
#
# ######################
# #### GAME PLAY #######
# ######################
print("Welcome to War, let's begin...")

#creating new deck and split it in a half:
deck = Deck()
deck.shuffleDeck()
half1, half2 = deck.splitInHalf()

#creating both players:

pl1 = Player("computer", Hand(half1))

name = input("what is your name?")
pl2 = Player(name, Hand(half2))

# game:
totalRounds = 0
warCount = 0

while pl1.still_has_cards() and pl2.still_has_cards():
    totalRounds += 1
    print ("Time for a new round!")
    print ("Here are some current standings:")
    print(pl1.name + "has the count:" + str(len(pl1.hand.cards)))
    print(pl2.name + "has the count:" + str(len(pl2.hand.cards)))
    print("Play a card!")
    print ("\n")

table_cards = []

pl1_card = pl1.play_card()
pl2_card = pl2.play_card()

table_cards.append(pl1_card)
table_cards.append(pl2_card)

#comparing rankings -> tuples
if pl1_card[1] == pl2_card[1]:
    warCount += 1

    print("WAR!")

    table_cards.extend(pl1.remove_war_cards())
    table_cards.extend(pl2.remove_war_cards())

    if RANKS.index(pl1_card[1]) < RANKS.index(pl2_card[1]):
        pl2.hand.add(table_cards)
    else:
        pl1.hand.add(table_cards)

else:
    if RANKS.index(pl1_card[1]) < RANKS.index(pl2_card[1]):
        pl2.hand.add(table_cards)
    else:
        pl1.hand.add(table_cards)

print("Game over, number of rounds:" + str(totalRounds))
print("a war happened" + str(warCount) + "times")
