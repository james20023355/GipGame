"""
This File Contains the code for the Git Game
Author: James Penales
"""


class Player:
    """ This class is to represent a real world player"""
    def __init__(self, name,turn):
        self.name = name
        self.turn = turn
        self.score = 0

    def updateScore(self, score):

        self.turn += score



class GipGame:
    """ This Class is in charge of the logic of the GitGame"""
    def __init__(self):
        self.currentlyPlaying = False
        self.turnScore = 0


    def switchTurns(self, player, n):
        """ This method is used to switch the players' turns """
        if not n:
            rollAgain = input("Would you like to roll again?[Y/N]: ").upper()
            if rollAgain == 'Y':
                result =  self.rollDice()
                print(result)
                if result != False:
                    print("Your Rolled A: ", result)
                else:
                    self.switchTurns(player, True)
            elif rollAgain == 'N':
                player.turn = False
            else:
                print("Error: Wrong Input!")
                self.switchTurns(player, False)

        else:
            print(f"Sorry  Player: {player.name}, you rolled a 1. You lost all your points for this turn :(")
            self.turnScore = 0
            player.turn = False



    def rollDice(self):
        """ this method handles the logic for a dice roll"""
        die = Dice()
        result = die.roll()
        if result != 1:
            self.turnScore += result
            return result
        else:
            return False



    def play(self):
        print("> Hello Welcome to Git Game:")
        p1Name = input("> Hello Player 1, Please Enter your Name: ")
        p2Name = input("> Hello Player 2, Please Enter your Name: ")
        player1 = Player(p1Name, True)
        player2 = Player(p2Name, False)
        print(f"Welcome to the game {p1Name} and {p2Name}")

        while player1.turn:
            if self.turnScore == 0:
                firstRoll = self.rollDice()

                if firstRoll !=  False:
                    print("Hello Player 1 your first roll is: ", )
                    print(self.turnScore)
                else:
                    print(f"Sorry  Player: {p1Name}, you rolled a 1. Your turn ends")
                    self.switchTurns(player1, True)
            else:
                self.switchTurns(player1, False)
                print(self.turnScore)



    def isWinner(self, winner):
        return winner


class Dice:
    """ This class is to represent a real world dice """
    def __init__(self):
        self.sides = [1, 2, 3, 4, 5, 6]

    def roll(self):
        """ Rolls a number from the sides of the die"""
        from random import choice as roll
        return roll(self.sides)


def main():
    game = GipGame()

    game.play()


if __name__ == '__main__':
    main()
