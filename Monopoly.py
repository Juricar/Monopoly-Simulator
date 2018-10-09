# This is a program inspired by a video on Youtube by standupmaths, that creates a virtual game of Monopoly, and is
# then used to simulate many rounds of Monopoly, and find, without putting your trust in someone else, the math behind
# the random chance in Monopoly

"""Code written by myself; Antonio Juric"""

import random as rng


def main():
    turns = 100000
    spaces_landed = the_game(turns)
    the_results(spaces_landed, turns)


class Player(object):
    # creates a class "Player" that will be used to simulate the game, recording the dice throws it gets, and where it
    # lands, to create a data set of randomly generated data that we can then study.

    def __init__(self):
        self.space = 0  # what space the Player is on
        self.roll_history = []  # What his rolls have been (for checking)
        self.space_history = []  # What spaces he has landed on (for final results)
        self.jail = 0  # If the Player is in Jail or not
        self.jail_counter = 0  # How many times the Player has failed to roll out of jail

    def take_turn(self):
        # This is a method to make a given player take a turn, making the player roll 2 dice, recording the total, and
        # then changing their space to be appropriate space after they would move that many spaces, resenting them if
        # they pass space 39, as then they would be back at go, and also checking if they are in jail, and making them
        # stop/not move as appropriate
        roll = 0
        roll_results = []
        for x in range(2):
            roll_results = roll_results + [rng.randint(1, 6)]
            roll = roll + roll_results[x]
        self.roll_history = self.roll_history + [roll]
        if self.jail == 1:
            if roll_results[0] == roll_results[1]:
                self.jail = 0
                self.jail_counter = 0
            else:
                if self.jail_counter < 2:
                    self.jail_counter = self.jail_counter + 1
                else:
                    self.jail = 0
                    self.jail_counter = 0
        if self.jail != 1:
            for k in range(roll):
                if self.space == 39:
                    self.space = 0
                else:
                    self.space = self.space + 1
        self.space_history = self.space_history + [self.space]
        if self.space == 30:
            self.space = 10
            self.jail = 1
        # if roll_results[0] == roll_results[1]:


def the_game(n):
    # Simply creates a player, and makes them play a very long game of Monopoly, with a huge amount of turns n
    alpha = Player()
    for k in range(n):
        alpha.take_turn()
    return alpha.space_history


def the_results(results, turns):
    # Displays the number of times a spot was landed on throughout the game, as well as the percentage of the time it
    # was landed on
    percents = []
    for k in range(40):
        percents = percents + [100 * (times_landed(results, k) / turns)]
    print('Times landed on GO! = ', times_landed(results, 0), '                       ', percents[0])
    print('Times landed on Mediterranean Ave.! = ', times_landed(results, 1), '       ', percents[1])
    print('Times landed on Community Chest #1! = ', times_landed(results, 2), '       ', percents[2])
    print('Times landed on Baltic Ave.! = ', times_landed(results, 3), '              ', percents[3])
    print('Times landed on Income Tax! = ', times_landed(results, 4), '               ', percents[4])
    print('Times landed on Reading Railroad! = ', times_landed(results, 5), '         ', percents[5])
    print('Times landed on Oriental Ave.! = ', times_landed(results, 6), '            ', percents[6])
    print('Times landed on Chance #1! = ', times_landed(results, 7), '                ', percents[7])
    print('Times landed on Vermont Ave.! = ', times_landed(results, 8), '             ', percents[8])
    print('Times landed on Connecticut Ave.! = ', times_landed(results, 9), '         ', percents[9])
    print('Times landed on Visiting/In Jail! = ', times_landed(results, 10), '         ', percents[10])
    print('Times landed on St. Charles Place! = ', times_landed(results, 11), '        ', percents[11])
    print('Times landed on Electric! = ', times_landed(results, 12), '                 ', percents[12])
    print('Times landed on States Ave.! = ', times_landed(results, 13), '              ', percents[13])
    print('Times landed on Virginia Ave.! = ', times_landed(results, 14), '            ', percents[14])
    print('Times landed on Pennsylvania Railroad! = ', times_landed(results, 15), '    ', percents[15])
    print('Times landed on St. James Place! = ', times_landed(results, 16), '          ', percents[16])
    print('Times landed on Community Chest #2! = ', times_landed(results, 17), '       ', percents[17])
    print('Times landed on Tennessee Ave.! = ', times_landed(results, 18), '           ', percents[18])
    print('Times landed on New York Ave.! = ', times_landed(results, 19), '            ', percents[19])
    print('Times landed on Free Parking! = ', times_landed(results, 20), '             ', percents[20])
    print('Times landed on Kentucky Ave.! = ', times_landed(results, 21), '            ', percents[21])
    print('Times landed on Chance #2! = ', times_landed(results, 22), '                ', percents[22])
    print('Times landed on Indiana Ave.! = ', times_landed(results, 23), '             ', percents[23])
    print('Times landed on Illinois Ave.! = ', times_landed(results, 24), '            ', percents[24])
    print('Times landed on B & O Railroad! = ', times_landed(results, 25), '           ', percents[25])
    print('Times landed on Atlantic Ave.! = ', times_landed(results, 26), '            ', percents[26])
    print('Times landed on Ventnor Ave.! = ', times_landed(results, 27), '             ', percents[27])
    print('Times landed on Water Works! = ', times_landed(results, 28), '              ', percents[28])
    print('Times landed on Marvin Gardens! = ', times_landed(results, 29), '           ', percents[29])
    print('Times landed on Go to Jail! = ', times_landed(results, 30), '               ', percents[30])
    print('Times landed on Pacific Ave.! = ', times_landed(results, 31), '             ', percents[31])
    print('Times landed on North Carolina Ave.! = ', times_landed(results, 32), '      ', percents[32])
    print('Times landed on Community Chest #3! = ', times_landed(results, 33), '       ', percents[33])
    print('Times landed on Pennsylvania Ave.! = ', times_landed(results, 34), '        ', percents[34])
    print('Times landed on Short Line! = ', times_landed(results, 35), '               ', percents[35])
    print('Times landed on Chance #3! = ', times_landed(results, 36), '                ', percents[36])
    print('Times landed on Park Place! = ', times_landed(results, 37), '               ', percents[37])
    print('Times landed on Luxury Tax! = ', times_landed(results, 38), '               ', percents[38])
    print('Times landed on Boardwalk! = ', times_landed(results, 39), '                ', percents[39])


def times_landed(results, n):
    # counts the number of times a certain number/space appears in the results
    count = 0
    for k in range(len(results)):
        if results[k] == n:
            count = count + 1
    return count


main()
