"""
This File Contains the code for the Git Game
Author: James Penales
"""
import time

class Player:
    """ This class is to represent a real world player"""
    def __init__(self, name,turn):
        self.name = name
        self.turn = turn
        self.score = 0

    def updateScore(self, score):
        self.score += score



class GipGame:
    """ This Class is in charge of the logic of the GitGame"""
    def __init__(self):
        self.currentlyPlaying = False
        self.turnScore = 0


    def switchTurns(self, player, player2, n):
        """ This method is used to switch the players' turns """
        if not n:
            rollAgain = input(f"> [GipGame]({self.turnScore}) Would you like to roll again?[Y/N]: ").upper()
            if rollAgain == 'Y':
                result = self.rollDice()

                if result != False:
                    print("> [GipGame] You rolled a: ", result,"\n")
                else:
                    self.switchTurns(player, player2,  True)

            elif rollAgain == 'N' and player2.turn:
                    player.turn = True
                    player2.turn = False
                    print(f"\n> [{player2.name}]  Congrats you earned: {self.turnScore} Points")
                    player2.updateScore(self.turnScore)
                    print(f"> [{player2.name}]  Your Current Score is: {player2.score}\n")
                    self.turnScore = 0

            elif rollAgain == 'N' and player.turn:
                player.turn = False
                player2.turn = True
                print(f"\n> [{player.name}] Congrats you earned: {self.turnScore} Points")
                player.updateScore(self.turnScore)
                print(f"> [{player.name}] Your Current Score is: {player.score}\n")
                self.turnScore = 0
            else:
                print("Error: Wrong Input!")
                self.switchTurns(player, player2, False)

        else:

            if player.turn:
                print(f"Sorry {player.name}, you rolled a 1. You lost all your points for this turn :(\n")
                player.turn = False
                player2.turn = True

            elif player2.turn:
                print(f"Sorry {player2.name}, you rolled a 1. You lost all your points for this turn :(\n")
                player.turn = True
                player2.turn = False
            self.turnScore = 0




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
        self.currentlyPlaying = True;
        print("> [GipGame] Hello and Welcome to Gip Game.")
        time.sleep(2)

        p1Name = input("> [GipGame] Player 1, Please Enter your Name: ")
        time.sleep(0.5)
        p2Name = input("> [GipGame] Player 2, Please Enter your Name: ")

        time.sleep(2)
        player1 = Player(p1Name, True)
        player2 = Player(p2Name, False)
        print(f"> [GipGame] Welcome to the game {p1Name} and {p2Name} \n")
        time.sleep(2)
        while self.currentlyPlaying:
                if player1.turn:
                    if self.turnScore == 0:
                        firstRoll = self.rollDice()

                        if firstRoll !=  False:
                            print(f"> [{p1Name}]: Your first roll for this round is: ", firstRoll,"\n")
                        else:
                            self.switchTurns(player1, player2, True)
                    else:
                        self.switchTurns(player1, player2, False)

                time.sleep(1)
                if player2.turn:
                    if self.turnScore == 0:
                        firstRoll = self.rollDice()

                        if firstRoll != False:
                            print(f"> [{p2Name}]: Your first roll for this round is: ", firstRoll,"\n")
                        else:
                            self.switchTurns(player1, player2, True)
                    else:
                        self.switchTurns(player1, player2, False)




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
