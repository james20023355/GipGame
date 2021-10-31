"""
This File Contains the code for the Git Game
Author: James Penales
"""
import time

class Player:
    """ This class is to represent a real world player"""
    def __init__(self, name, turn):
        self.name = name  # Represents Player Name
        self.turn = turn  # Represents whether or not it is a player's turn
        self.score = 0  # Represents a player's overall score

    def updateScore(self, score):
        """ This method updates a player's score"""
        self.score += score


class GipGame:
    """ This Class is in charge of the logic of the GitGame"""
    def __init__(self):
        self.currentlyPlaying = False
        self.turnScore = 0

    def switchTurns(self, player, player2, n):
        """ This method is used to switch the players' turns """
        if not n:
            rollAgain = input(f"> [GipGame](Turn Score: {self.turnScore}) Would you like to roll again?[Y/N]: ").upper()

            if rollAgain == 'Y':
                result = self.rollDice()

                if result != False:
                    print("> [GipGame] You rolled a: ", result,"\n")
                else:
                    self.switchTurns(player, player2,  True)

            elif rollAgain == 'N' and player.turn:
                player.turn = False
                player2.turn = True
                print(f"\n> [{player.name}] Congrats you earned: {self.turnScore} Points")
                player.updateScore(self.turnScore)
                print(f"> [{player.name}] Your Current Score is: {player.score}\n")
                self.turnScore = 0
                if self.isWinner(player):
                    player.turn = False
                    player2.turn = False
                    self.currentlyPlaying = False

            elif rollAgain == 'N' and player2.turn:
                player.turn = True
                player2.turn = False
                print(f"\n> [{player2.name}]  Congrats you earned: {self.turnScore} Points")
                player2.updateScore(self.turnScore)
                print(f"> [{player2.name}]  Your Current Score is: {player2.score}\n")
                self.turnScore = 0
                if self.isWinner(player2):
                    player.turn = False
                    player2.turn = False
                    self.currentlyPlaying = False

            else:
                print("Error: Wrong Input!")
                self.switchTurns(player, player2, False)

        else:

            if player.turn:
                print(f"> [{player.name}] Sorry {player.name}, you rolled a 1. You lost all your points for this turn\n")
                player.turn = False
                player2.turn = True
                time.sleep(0.5)

            elif player2.turn:
                print(f"> [{player2.name}] Sorry {player2.name}, you rolled a 1. You lost all your points for this turn\n")
                player.turn = True
                player2.turn = False
                time.sleep(0.5)
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

    def introMessage(self):
        """ This method is in charge of the introduction to the game"""
        playIntro = input("> [GipGame] Would you like to know the rules of GipGame? [Y/N]: ").upper()

        if playIntro == 'Y':
            print("> [GipGame] The Rules of the game are simple .. ")
            time.sleep(2)
            print("> [GipGame] Each player gets a turn to roll a die, if the player rolls a number between 2 and 6.")
            time.sleep(5)
            print("> [GipGame] That number is added to the overall score for that turn.")
            time.sleep(4)
            print("> [GipGame] The player will have the option to keep re-rolling.")
            time.sleep(4)
            print("> [GipGame] But if they roll a 1, the amount of points built up in that turn is lost.")
            time.sleep(5)
            print("> [GipGame] And the other player gets a turn")
            time.sleep(4)
            print("> [GipGame] First Person to 100 wins.")
            time.sleep(2)
            print("> [GipGame] Good Luck.\n")
            time.sleep(3)
        elif playIntro == 'N':
            print("> [GipGame] Alright. Player 1 will now roll\n")
            time.sleep(1.5)
        else:
            print("[GipGame] Wrong input, try again")
            self.introMessage()

    def play(self):
        """ This method is to handle the game process"""
        self.currentlyPlaying = True

        print("> [GipGame] Hello and Welcome to Gip Game.")
        time.sleep(1)
        p1Name = input("> [GipGame] Player 1, Please Enter your Name: ")
        time.sleep(0.5)
        p2Name = input("> [GipGame] Player 2, Please Enter your Name: ")
        time.sleep(1)
        player1 = Player(p1Name, True)
        player2 = Player(p2Name, False)
        print(f"\n> [GipGame] Welcome to the game {p1Name} and {p2Name} \n")
        time.sleep(1)

        self.introMessage()


        while self.currentlyPlaying:
            if player1.turn:
                if self.turnScore == 0:

                    firstRoll = self.rollDice()

                    if firstRoll:

                        print(f"> [{p1Name}](Points: {player1.score}): Your first roll for this round is: ", firstRoll,"\n")
                    else:
                        self.switchTurns(player1, player2, True)
                else:
                    self.switchTurns(player1, player2, False)

            time.sleep(1)
            if player2.turn:
                if self.turnScore == 0:
                    firstRoll = self.rollDice()

                    if firstRoll:
                        print(f"> [{p2Name}](Points: {player2.score}): Your first roll for this round is: ", firstRoll,"\n")
                    else:
                        self.switchTurns(player1, player2, True)
                else:
                    self.switchTurns(player1, player2, False)

    def isWinner(self, player):
        """ This Method returns a boolean value based on whether or not a player has reached 100 points"""
        if player.score >= 100:
            print(f"{player.name} Wins")
            return True
        else:
            return False


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
