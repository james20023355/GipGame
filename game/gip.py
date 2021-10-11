"""
This File Contains the code for the Git Game
Author: James Penales
"""


class Player:
    """ This class is to represent a real world player"""
    def __init__(self, name, turn, score):
        self.name = name
        self.turn = turn
        self.score = score

    def updateScore(self):
        print("")


    def rollDice(self):
        """ Player should be able to roll the dice"""
        die = Dice()
        return die.roll()


class GipGame:
    """ This Class is in charge of the logic of the GitGame"""
    def __init__(self):
        self.currentlyPlaying = False
        self.turnScore = 0


    def switchTurns(self):
        print("")


    def switchTurns(self):
        print("")


class Dice:
    """ This class is to represent a real world dice """
    def __init__(self):
        self.sides = [1, 2, 3, 4, 5, 6]

    def roll(self):
        """ Rolls a number from the sides of the die"""
        from random import choice as roll
        return roll(self.sides)


def main():
    print("Hello World")


if __name__ == '__main__':
    main()