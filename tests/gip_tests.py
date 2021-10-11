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

