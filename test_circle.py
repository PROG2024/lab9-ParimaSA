"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import math
import unittest

from circle import Circle


class CircleTest(unittest.TestCase):
    def test_add_area_with_two_positive_circle(self):
        """
        The area of new circle should equal to the combined area of circle1 and circle2
        and the radius should equal to sqrt(r1^2 + r2^2) from the pythagorean laws(r1^2 + r2^2 = r3^2).
        """
        circle1 = Circle(5)
        circle2 = Circle(10)
        new_circle = circle1.add_area(circle2)
        radius = math.hypot(5, 10)
        area = circle1.get_area() + circle2.get_area()
        self.assertEqual(radius, new_circle.get_radius())
        self.assertEqual(area, new_circle.get_area())

    def test_add_area_with_one_zero_circle(self):
        """
        When one of the circle has radius 0, add area with non-zero circle,
        new circle should have the same radius and area with non-zero circle.
        """
        circle1 = Circle(5)
        circle2 = Circle(0)
        new_circle = circle1.add_area(circle2)
        area = circle1.get_area()
        self.assertEqual(5, new_circle.get_radius())
        self.assertEqual(area, new_circle.get_area())

    def test_circle_with_negative_radius(self):
        """Circle constructor should raises exception if the radius is negative."""
        with self.assertRaises(Exception):
            negative_circle = Circle(-5)
