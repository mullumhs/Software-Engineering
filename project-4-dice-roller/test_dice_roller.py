"""
Unit Tests for Dice Roller
--------------------------
File Name: test_dice_roller.py
Teacher: David Steedman
Class: Software Engineering

Run these tests with: python -m unittest test_dice_roller
Or: python test_dice_roller.py
"""

import unittest


# =============================================================================
# STUDENT IMPLEMENTATION SECTION
# =============================================================================
# 
# TODO: Copy your dice rolling functions from dice-roller.py here,
# or import them if your file is structured as a module.
# 
# Your functions should look something like:
# 
# def roll_die(sides):
#     """Roll a single die with the given number of sides."""
#     import random
#     return random.randint(1, sides)
# 
# def roll_dice(num_dice, sides):
#     """Roll multiple dice and return a list of results."""
#     return [roll_die(sides) for _ in range(num_dice)]
# 
# Uncomment the import below if you've structured your code as functions:
# from dice_roller import roll_die, roll_dice
# =============================================================================


import random

def roll_die(sides):
    """Roll a single die with the given number of sides. Replace with your implementation."""
    return random.randint(1, sides)


def roll_dice(num_dice, sides):
    """Roll multiple dice and return a list of results. Replace with your implementation."""
    return [roll_die(sides) for _ in range(num_dice)]


# =============================================================================
# TEST CASES
# =============================================================================

class TestRollDie(unittest.TestCase):
    """Tests for single die rolling."""
    
    def test_d6_in_range(self):
        """A d6 roll should always be between 1 and 6."""
        for _ in range(100):  # Roll 100 times to test randomness
            result = roll_die(6)
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, 6)
    
    def test_d20_in_range(self):
        """A d20 roll should always be between 1 and 20."""
        for _ in range(100):
            result = roll_die(20)
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, 20)
    
    def test_d4_in_range(self):
        """A d4 roll should always be between 1 and 4."""
        for _ in range(100):
            result = roll_die(4)
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, 4)
    
    def test_returns_integer(self):
        """Die roll should return an integer."""
        result = roll_die(6)
        self.assertIsInstance(result, int)


class TestRollDice(unittest.TestCase):
    """Tests for rolling multiple dice."""
    
    def test_correct_number_of_dice(self):
        """Rolling 3 dice should return 3 results."""
        results = roll_dice(3, 6)
        self.assertEqual(len(results), 3)
    
    def test_single_die(self):
        """Rolling 1 die should return 1 result."""
        results = roll_dice(1, 6)
        self.assertEqual(len(results), 1)
    
    def test_all_results_in_range(self):
        """All results from 4d6 should be between 1 and 6."""
        results = roll_dice(4, 6)
        for result in results:
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, 6)
    
    def test_returns_list(self):
        """roll_dice should return a list."""
        results = roll_dice(2, 6)
        self.assertIsInstance(results, list)
    
    def test_d20_multiple(self):
        """Rolling 5d20 should return 5 values all between 1 and 20."""
        results = roll_dice(5, 20)
        self.assertEqual(len(results), 5)
        for result in results:
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, 20)


class TestStatisticalProperties(unittest.TestCase):
    """Tests for statistical properties of dice rolls."""
    
    def test_d6_produces_all_values(self):
        """Over many rolls, a d6 should produce all values 1-6."""
        results = set()
        for _ in range(1000):
            results.add(roll_die(6))
        self.assertEqual(results, {1, 2, 3, 4, 5, 6})
    
    def test_reasonable_average(self):
        """The average of many d6 rolls should be close to 3.5."""
        rolls = [roll_die(6) for _ in range(10000)]
        average = sum(rolls) / len(rolls)
        self.assertAlmostEqual(average, 3.5, places=1)


if __name__ == '__main__':
    print("Running Dice Roller Tests...")
    print("=" * 50)
    unittest.main(verbosity=2)
