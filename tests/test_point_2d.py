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
import unittest
from hamcrest import assert_that, equal_to, calling, raises
from concept.math.vector import Vector2d
from concept.math.point import Point2d
from concept.errors.exceptions import UnsupportedOperation


class TestPoint2d(unittest.TestCase):
    """ Testing math 2d point. """

    def test_init(self):
        """Testing of method Poinnt2d.__init__."""
        assert_that(Point2d(1.0, 2.0).x, equal_to(1.0))
        assert_that(Point2d(1.0, 2.0).y, equal_to(2.0))
        assert_that(Point2d(), equal_to(Point2d(0.0, 0.0)))

    def test_repr(self):
        """Testing of method Poinnt2d.__repr__."""
        assert_that(str(Point2d(1.2, 3.4)), equal_to("Point2d(x=1.2, y=3.4)"))

    def test_add(self):
        """Testing of method Point2d.__add__."""
        assert_that(Point2d(1.0, 2.0) + Vector2d(3.0, 4.0), equal_to(Point2d(4.0, 6.0)))
        assert_that(calling(Point2d().__add__).with_args(1234),
                    raises(UnsupportedOperation))

    def test_sub(self):
        """Testing of method Point2d.__sub__."""
        assert_that(Point2d(1.0, 5.0) - Point2d(3.0, 4.0), equal_to(Vector2d(-2.0, 1.0)))
        assert_that(calling(Point2d().__sub__).with_args(1234),
                    raises(UnsupportedOperation))

    def test_eq(self):
        """Testing of method Point2d.__eq__."""
        assert_that(Point2d(1.2, 3.4), equal_to(Point2d(1.2, 3.4)))
        assert_that(Point2d(1.2, 3.4).__eq__(1234), equal_to(False))
