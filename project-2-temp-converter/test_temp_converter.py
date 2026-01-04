"""
Unit Tests for Temperature Converter
-------------------------------------
File Name: test_temp_converter.py
Teacher: David Steedman
Class: Software Engineering

Run these tests with: python -m unittest test_temp_converter
Or: python test_temp_converter.py
"""

import unittest


# =============================================================================
# STUDENT IMPLEMENTATION SECTION
# =============================================================================
# 
# TODO: Copy your conversion functions from temp-converter.py here,
# or import them if your file is structured as a module.
# 
# Your functions should look something like:
# 
# def celsius_to_fahrenheit(celsius):
#     """Convert Celsius to Fahrenheit."""
#     return (celsius * 9/5) + 32
# 
# def fahrenheit_to_celsius(fahrenheit):
#     """Convert Fahrenheit to Celsius."""
#     return (fahrenheit - 32) * 5/9
# 
# Uncomment the import below if you've structured your code as functions:
# from temp_converter import celsius_to_fahrenheit, fahrenheit_to_celsius
# =============================================================================


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit. Replace with your implementation."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius. Replace with your implementation."""
    return (fahrenheit - 32) * 5/9


# =============================================================================
# TEST CASES
# =============================================================================

class TestCelsiusToFahrenheit(unittest.TestCase):
    """Tests for Celsius to Fahrenheit conversion."""
    
    def test_freezing_point(self):
        """0°C should equal 32°F (freezing point of water)."""
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32, places=1)
    
    def test_boiling_point(self):
        """100°C should equal 212°F (boiling point of water)."""
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212, places=1)
    
    def test_negative_temperature(self):
        """-40°C should equal -40°F (they're the same at this point!)."""
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40, places=1)
    
    def test_body_temperature(self):
        """37°C should equal approximately 98.6°F (body temperature)."""
        self.assertAlmostEqual(celsius_to_fahrenheit(37), 98.6, places=1)
    
    def test_room_temperature(self):
        """20°C should equal 68°F (comfortable room temperature)."""
        self.assertAlmostEqual(celsius_to_fahrenheit(20), 68, places=1)


class TestFahrenheitToCelsius(unittest.TestCase):
    """Tests for Fahrenheit to Celsius conversion."""
    
    def test_freezing_point(self):
        """32°F should equal 0°C (freezing point of water)."""
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0, places=1)
    
    def test_boiling_point(self):
        """212°F should equal 100°C (boiling point of water)."""
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100, places=1)
    
    def test_negative_temperature(self):
        """-40°F should equal -40°C (they're the same at this point!)."""
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40, places=1)
    
    def test_body_temperature(self):
        """98.6°F should equal approximately 37°C (body temperature)."""
        self.assertAlmostEqual(fahrenheit_to_celsius(98.6), 37, places=1)
    
    def test_room_temperature(self):
        """68°F should equal 20°C (comfortable room temperature)."""
        self.assertAlmostEqual(fahrenheit_to_celsius(68), 20, places=1)


if __name__ == '__main__':
    print("Running Temperature Converter Tests...")
    print("=" * 50)
    unittest.main(verbosity=2)
