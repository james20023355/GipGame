""" This File contains the unit tests for the gip game """
import unittest
from game import gip


class GipGameTests(unittest.TestCase):

    def test_diceRoll(self):

        # Arrange
        dice = gip.Dice()
        # Act
        result = gip.Dice.roll(dice)
        # Assert
        self.assertIsNotNone(result)

    def test_isWinner(self):
        # Arrange
        game = gip.GipGame()
        player = gip.Player("Joanna", False)
        player.score = 100

        self.assertTrue(game.isWinner(player))

    def test_updateScore(self):
        # Arrange
        game  = gip.GipGame
        player = gip.Player("Jorthan", False)
        expected = 5

        # Act
        player.updateScore(5)

        # Assert 
        self.assertEqual(player.score, expected)
