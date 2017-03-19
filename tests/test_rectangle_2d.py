"""
   =======
   License
   =======
   Copyright (c) 2017 Thomas Lehmann

   Permission is hereby granted, free of charge, to any person obtaining a copy of this
   software and associated documentation files (the "Software"), to deal in the Software
   without restriction, including without limitation the rights to use, copy, modify, merge,
   publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons
   to whom the Software is furnished to do so, subject to the following conditions:

   The above copyright notice and this permission notice shall be included in all copies
   or substantial portions of the Software.

   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
   INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
   IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
   DAMAGES OR OTHER LIABILITY,
   WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
# pylint: disable=R0201
import math
import unittest
from hamcrest import assert_that, equal_to, is_not
from concept.math.rectangle import Rectangle2d
from concept.math.vector import Vector2d
from concept.math.point import Point2d


class TestRectangle2d(unittest.TestCase):
    """ Testing math 2d rectangle. """

    def test_init(self):
        """Testing construction."""
        rectangle = Rectangle2d(Point2d(1, 2), 3, 4)
        assert_that(rectangle.position, equal_to(Point2d(1, 2)))
        assert_that(rectangle.width, equal_to(3))
        assert_that(rectangle.height, equal_to(4))
        assert_that(rectangle.direction, equal_to(Vector2d(1, 0)))

    def test_repr(self):
        """Testing of method Rectangle2d.__repr__."""
        rectangle = Rectangle2d(Point2d(1, 2), 3, 4)
        expected = "Rectangle2d(position=Point2d(x=1, y=2), "
        expected += "width=3, height=4, "
        expected += "direction=Vector2d(x=1, y=0))"
        assert_that(str(rectangle), equal_to(expected))

    def test_points(self):
        """Testing top/left and bottom/right."""
        rectangle = Rectangle2d(Point2d(1, 2), 3, 4)
        assert_that(rectangle.top_left(), equal_to(Point2d(1, 2)))
        assert_that(rectangle.bottom_right(), equal_to(Point2d(4, -2)))

    def test_equal(self):
        """Testing of Rectangle2d.__eq__ method."""
        rectangle_a = Rectangle2d(Point2d(1, 2), 3, 4)
        rectangle_b = Rectangle2d(Point2d(1, 2), 3, 4)
        rectangle_c = Rectangle2d(Point2d(2, 2), 3, 4)
        rectangle_d = Rectangle2d(Point2d(1, 2), 5, 4)
        rectangle_e = Rectangle2d(Point2d(1, 2), 3, 5)
        rectangle_f = Rectangle2d(Point2d(1, 2), 3, 4, Vector2d(0, 1))
        assert_that(rectangle_a, equal_to(rectangle_b))
        assert_that(rectangle_a, is_not(equal_to(rectangle_c)))
        assert_that(rectangle_a, is_not(equal_to(rectangle_d)))
        assert_that(rectangle_a, is_not(equal_to(rectangle_e)))
        assert_that(rectangle_a, is_not(equal_to(rectangle_f)))
        assert_that(rectangle_a.__eq__(1234), equal_to(False))

    def test_rotate(self):
        """Testing Rectangle2d.rotate"""
        rectangle = Rectangle2d(Point2d(1, 1), 3, 4)
        rectangle.rotate(90.0 * math.pi / 180.0)
        assert_that(rectangle.direction, equal_to(Vector2d(0, 1)))
        assert_that(rectangle.top_left(), equal_to(Point2d(1, 1)))
        assert_that(rectangle.bottom_right(), equal_to(Point2d(5, 4)))
