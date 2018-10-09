# This is a program inspired by a video on Youtube by standupmaths, that creates a virtual game of Monopoly, and is
# then used to simulate many rounds of Monopoly, and find, without putting your trust in someone else, the math behind
# the random chance in Monopoly
"Code written by myself; Antonio Juric"

import random as rng

def main():
    the_game()


class Player(object):
    # creates a class "Player" that will be used to simulate the game, recording the dice throws it gets, and where it
    # lands, to create a data set of randomly generated data that we can then study.

    def __init__(self):
        self.space = 0
        self.roll_history = []
        self.space_history = []

    def take_turn(self):
        # This is a method to make a given player take a turn, making the player roll 2 dice, recordning the total, and
        # then changing their space to be appropriate space after they would move that many spaces, reseting them if
        # they pass space 39, as then they would be back at go
        roll = 0
        for x in range(2):
            roll = roll + rng.randint(1,6)
        self.roll_history = self.roll_history + [roll]
        for k in range(roll):
            if self.space == 39:
                self.space = 0
            else:
                self.space = self.space + 1
        self.space_history = self.space_history + [self.space]

def the_game():
    alpha = Player()
    for k in range(10):
        alpha.take_turn()

main()