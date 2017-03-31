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
from hamcrest import assert_that, equal_to, is_not, calling, raises
from concept.math.vector import Vector2d
from concept.math.point import Point2d
from concept.math.line import Line2d
from concept.errors.exceptions import PointIsNotOnTheGivenLine, UnsupportedOperation,\
    NoLineIntersection


class TestLine2d(unittest.TestCase):
    """ Testing math 2d line. """

    def test_init(self):
        """Testing of method Line2d.__init__."""
        line = Line2d(Point2d(1.0, 2.0), Vector2d(3.0, 4.0))
        assert_that(line.position, equal_to(Point2d(1.0, 2.0)))
        assert_that(line.direction, equal_to(Vector2d(3.0, 4.0)))

    def test_repr(self):
        """Testing of method Line2d.__repr__."""
        line = Line2d(Point2d(1.0, 2.0), Vector2d(3.0, 4.0))
        expected = "Line2d(position=Point2d(x=1, y=2), direction=Vector2d(x=3, y=4))"
        assert_that(str(line), equal_to(expected))

    def test_turned_left(self):
        """Testing of method Line2d.turned_left."""
        line = Line2d(Point2d(1.0, 2.0), Vector2d(1.0, 0.0)).turned_left()
        assert_that(line.position, equal_to(Point2d(1.0, 2.0)))
        assert_that(line.direction, equal_to(Vector2d(0.0, 1.0)))

    def test_turned_right(self):
        """Testing of method Line2d.turned_right."""
        line = Line2d(Point2d(1.0, 2.0), Vector2d(1.0, 0.0)).turned_right()
        assert_that(line.position, equal_to(Point2d(1.0, 2.0)))
        assert_that(line.direction, equal_to(Vector2d(0.0, -1.0)))

    def test_point(self):
        """Testing of method Line2d.point."""
        line = Line2d(Point2d(1.0, 2.0), Vector2d(3.0, 4.0))
        assert_that(line.point(0.0), equal_to(Point2d(1.0, 2.0)))
        assert_that(line.point(0.5), equal_to(Point2d(2.5, 4.0)))
        assert_that(line.point(1.0), equal_to(Point2d(4.0, 6.0)))

    def test_length(self):
        """Testing of method Line2d.length."""
        line = Line2d(Point2d(1.0, 2.0), Vector2d(3.0, 4.0))
        assert_that(line.length(), equal_to(Vector2d(3.0, 4.0).length()))

    def test_is_parallel(self):
        """Testing of method Line2d.is_parallel."""
        line_a = Line2d(Point2d(1.0, 0.0), Vector2d(3.0, 0.0))
        line_b = Line2d(Point2d(2.0, 0.0), Vector2d(6.0, 0.0))
        line_c = Line2d(Point2d(2.0, 0.0), Vector2d(6.0, 1.0))
        assert_that(line_a.is_parallel(line_a), equal_to(True))
        assert_that(line_a.is_parallel(line_b), equal_to(True))
        assert_that(line_a.is_parallel(line_c), equal_to(False))
        assert_that(
            calling(line_a.is_parallel).with_args(1234),
            raises(UnsupportedOperation))

    def test_angle(self):
        """Testing of method Line2d.angle."""
        line_a = Line2d(Point2d(1.0, 2.0), Vector2d(1.0, 0.0))
        line_b = Line2d(Point2d(3.0, 4.0), Vector2d(0.0, 1.0))
        # should be -90 degree
        angle = line_a.angle(line_b) * 180.0 / math.pi
        assert_that(abs(angle + 90.0) < 1e-10, equal_to(True))

    def test_factor(self):
        """Testing of method Line2d.factor."""
        line = Line2d(Point2d(1.0, 1.0), Vector2d(1.0, 1.0))
        assert_that(line.factor(Point2d(1.0, 1.0)), equal_to(0.0))
        assert_that(line.factor(Point2d(1.5, 1.5)), equal_to(0.5))
        assert_that(line.factor(Point2d(2.0, 2.0)), equal_to(1.0))
        assert_that(line.factor(Point2d(0.0, 0.0)), equal_to(-1.0))
        assert_that(line.factor(Point2d(3.0, 3.0)), equal_to(+2.0))
        assert_that(
            calling(line.factor).with_args(Point2d(0.0, 1.0)),
            raises(PointIsNotOnTheGivenLine))

        line = Line2d(Point2d(1.0, 1.0), Vector2d(0.0, 1.0))
        assert_that(line.factor(Point2d(1.0, 1.5)), equal_to(0.5))

    def test_valid_intersection(self):
        """Testing of method Line2d.intersection."""
        line_a = Line2d(Point2d(0.0, 2.0), Vector2d(4.0, 0.0))
        line_b = Line2d(Point2d(3.0, 0.0), Vector2d(0.0, 4.0))
        assert_that(line_a.intersection(line_b), equal_to(Point2d(3.0, 2.0)))

    def test_no_intersection(self):
        """Testing of method Line2d.intersection."""
        line_a = Line2d(Point2d(0.0, 2.0), Vector2d(4.0, 0.0))
        line_b = Line2d(Point2d(0.0, 1.0), Vector2d(4.0, 0.0))
        line_c = Line2d(Point2d(2.0, 0.0), Vector2d(0.0, 1.0))
        # raised because lines are parallel
        assert_that(
            calling(line_a.intersection).with_args(line_b),
            raises(NoLineIntersection))
        # factor of line_c is not between 0 and 1
        assert_that(
            calling(line_a.intersection).with_args(line_c),
            raises(NoLineIntersection))

    def test_equal(self):
        """Testing of method Line2d.__eq__."""
        line_a = Line2d(Point2d(0.0, 2.0), Vector2d(4.0, 0.0))
        line_b = Line2d(Point2d(0.0, 2.0), Vector2d(4.0, 0.0))
        line_c = Line2d(Point2d(3.0, 0.0), Vector2d(0.0, 4.0))
        assert_that(line_a, equal_to(line_b))
        assert_that(line_a, is_not(equal_to(line_c)))
        assert_that(line_a.__eq__(1234), equal_to(False))

    def test_side(self):
        """Testing of method Line2d.side."""
        line = Line2d(Point2d(1.0, 1.0), Vector2d(0.0, 2.0))
        # point should be left of line
        assert_that(line.side(Point2d(0.0, 2.0)), equal_to(-1))
        # point should be right of line
        assert_that(line.side(Point2d(2.0, 2.0)), equal_to(+1))
        # point on the line
        assert_that(line.side(Point2d(1.0, 1.0)), equal_to(0))
        assert_that(line.side(Point2d(1.0, 2.0)), equal_to(0))

        assert_that(
            calling(line.side).with_args("hello world"),
            raises(UnsupportedOperation))
