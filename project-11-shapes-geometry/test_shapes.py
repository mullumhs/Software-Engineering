"""
Unit Tests for Shapes and Geometry
-----------------------------------
File Name: test_shapes.py
Teacher: David Steedman
Class: Software Engineering

Run these tests with: python -m unittest test_shapes
Or: python test_shapes.py
"""

import unittest
import math


# =============================================================================
# STUDENT IMPLEMENTATION SECTION
# =============================================================================
# 
# TODO: Import your shape classes from shapes.py
# 
# Your classes should look something like:
# 
# class Shape:
#     def area(self):
#         raise NotImplementedError
#     
#     def perimeter(self):
#         raise NotImplementedError
# 
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     
#     def area(self):
#         return math.pi * self.radius ** 2
#     
#     def perimeter(self):
#         return 2 * math.pi * self.radius
#
# Uncomment the import below when you've completed shapes.py:
# from shapes import Shape, Circle, Rectangle, Triangle
# =============================================================================


class Shape:
    """Base Shape class. Replace with your implementation."""
    
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")
    
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter()")


class Circle(Shape):
    """Circle class. Replace with your implementation."""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class. Replace with your implementation."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    """Triangle class. Replace with your implementation."""
    
    def __init__(self, base, height, side_a=None, side_b=None, side_c=None):
        self.base = base
        self.height = height
        # For perimeter, use provided sides or default to equilateral
        self.side_a = side_a if side_a else base
        self.side_b = side_b if side_b else base
        self.side_c = side_c if side_c else base
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


# =============================================================================
# TEST CASES
# =============================================================================

class TestCircle(unittest.TestCase):
    """Tests for the Circle class."""
    
    def test_circle_area_unit(self):
        """Circle with radius 1 should have area pi."""
        circle = Circle(1)
        self.assertAlmostEqual(circle.area(), math.pi, places=5)
    
    def test_circle_area_radius_5(self):
        """Circle with radius 5 should have area 25*pi (≈78.54)."""
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.54, places=2)
    
    def test_circle_perimeter_unit(self):
        """Circle with radius 1 should have perimeter 2*pi."""
        circle = Circle(1)
        self.assertAlmostEqual(circle.perimeter(), 2 * math.pi, places=5)
    
    def test_circle_perimeter_radius_10(self):
        """Circle with radius 10 should have perimeter 20*pi (≈62.83)."""
        circle = Circle(10)
        self.assertAlmostEqual(circle.perimeter(), 62.83, places=2)


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""
    
    def test_rectangle_area_square(self):
        """Square 5x5 should have area 25."""
        rect = Rectangle(5, 5)
        self.assertEqual(rect.area(), 25)
    
    def test_rectangle_area_different_sides(self):
        """Rectangle 4x6 should have area 24."""
        rect = Rectangle(4, 6)
        self.assertEqual(rect.area(), 24)
    
    def test_rectangle_perimeter_square(self):
        """Square 5x5 should have perimeter 20."""
        rect = Rectangle(5, 5)
        self.assertEqual(rect.perimeter(), 20)
    
    def test_rectangle_perimeter_different_sides(self):
        """Rectangle 4x6 should have perimeter 20."""
        rect = Rectangle(4, 6)
        self.assertEqual(rect.perimeter(), 20)
    
    def test_rectangle_with_float_dimensions(self):
        """Rectangle should work with float dimensions."""
        rect = Rectangle(3.5, 2.5)
        self.assertAlmostEqual(rect.area(), 8.75, places=2)


class TestTriangle(unittest.TestCase):
    """Tests for the Triangle class."""
    
    def test_triangle_area(self):
        """Triangle with base 10 and height 5 should have area 25."""
        tri = Triangle(10, 5)
        self.assertEqual(tri.area(), 25)
    
    def test_triangle_area_different_values(self):
        """Triangle with base 8 and height 6 should have area 24."""
        tri = Triangle(8, 6)
        self.assertEqual(tri.area(), 24)
    
    def test_triangle_perimeter_equilateral(self):
        """Equilateral triangle with side 5 should have perimeter 15."""
        tri = Triangle(5, 4.33, 5, 5, 5)
        self.assertEqual(tri.perimeter(), 15)
    
    def test_triangle_perimeter_scalene(self):
        """Triangle with sides 3, 4, 5 should have perimeter 12."""
        tri = Triangle(3, 4, 3, 4, 5)
        self.assertEqual(tri.perimeter(), 12)


class TestPolymorphism(unittest.TestCase):
    """Tests for polymorphic behavior."""
    
    def test_all_shapes_have_area(self):
        """All shapes should implement area method."""
        shapes = [Circle(5), Rectangle(4, 6), Triangle(10, 5)]
        for shape in shapes:
            self.assertIsNotNone(shape.area())
            self.assertGreater(shape.area(), 0)
    
    def test_all_shapes_have_perimeter(self):
        """All shapes should implement perimeter method."""
        shapes = [Circle(5), Rectangle(4, 6), Triangle(10, 5, 10, 10, 10)]
        for shape in shapes:
            self.assertIsNotNone(shape.perimeter())
            self.assertGreater(shape.perimeter(), 0)
    
    def test_shapes_are_shape_instances(self):
        """All shapes should be instances of Shape."""
        shapes = [Circle(5), Rectangle(4, 6), Triangle(10, 5)]
        for shape in shapes:
            self.assertIsInstance(shape, Shape)


if __name__ == '__main__':
    print("Running Shapes and Geometry Tests...")
    print("=" * 50)
    unittest.main(verbosity=2)
