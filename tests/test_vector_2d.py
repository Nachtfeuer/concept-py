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
from hamcrest import assert_that, equal_to
from concept.math.vector import Vector2d


class TestVector2d(unittest.TestCase):
    """ Testing math 2d vector. """

    def test_init(self):
        """Testing of method Vector2d.__init__."""
        assert_that(Vector2d(1.0, 2.0).x, equal_to(1.0))
        assert_that(Vector2d(1.0, 2.0).y, equal_to(2.0))
        assert_that(Vector2d(), equal_to(Vector2d(0.0, 0.0)))

    def test_repr(self):
        """Testing of method Vector2d.__repr__."""
        assert_that(str(Vector2d(1.2, 3.4)), equal_to("Vector2d(x=1.2, y=3.4)"))

    def test_add(self):
        """Testing of method Vector2d.__add__."""
        assert_that(Vector2d(1.0, 2.0) + Vector2d(3.0, 4.0), equal_to(Vector2d(4.0, 6.0)))

    def test_sub(self):
        """Testing of method Vector2d.__sub__."""
        assert_that(Vector2d(1.0, 5.0) - Vector2d(3.0, 4.0), equal_to(Vector2d(-2.0, 1.0)))

    def test_scalar_product(self):
        """Testing of method Vector2d.scalar_product."""
        assert_that(Vector2d(2.0, 5.0).scalar_product(Vector2d(3.0, 4.0)), equal_to(26))

    def test_length(self):
        """Testing of method Vector2d.length."""
        assert_that(Vector2d(3.0, 4.0).length(), equal_to(5.0))

    def test_scaled(self):
        """Testing of method Vector2d.scaled."""
        vec = Vector2d(3.0, 4.0)
        assert_that(vec.scaled(2), equal_to(Vector2d(6.0, 8.0)))
        assert_that(vec, equal_to(Vector2d(3.0, 4.0)))

    def test_scale(self):
        """Testing of method Vector2d.scale."""
        vec = Vector2d(3.0, 4.0)
        vec.scale(2.0)
        assert_that(vec, equal_to(Vector2d(6.0, 8.0)))

    def test_rotated(self):
        """Testing of method Vector2d.rotated."""
        vec_a = Vector2d(1.0, 0.0)
        vec_b = vec_a.rotated(math.pi / 180.0 * 90)

        assert_that(abs(vec_b.x) < 1e-10, equal_to(True))
        assert_that(abs(vec_b.y - 1.0) < 1e-10, equal_to(True))

    def test_turned_left(self):
        """Testing of method Vector2d.turned_left."""
        assert_that(Vector2d(1.0, 0.0).turned_left(), equal_to(Vector2d(0.0, 1.0)))
        assert_that(Vector2d(0.0, 1.0).turned_left(), equal_to(Vector2d(-1.0, 0.0)))
        assert_that(Vector2d(-1.0, 0.0).turned_left(), equal_to(Vector2d(0.0, -1.0)))
        assert_that(Vector2d(0.0, -1.0).turned_left(), equal_to(Vector2d(1.0, 0.0)))

    def test_turned_right(self):
        """Testing of method Vector2d.turned_right."""
        assert_that(Vector2d(1.0, 0.0).turned_right(), equal_to(Vector2d(0.0, -1.0)))
        assert_that(Vector2d(0.0, -1.0).turned_right(), equal_to(Vector2d(-1.0, 0.0)))
        assert_that(Vector2d(-1.0, 0.0).turned_right(), equal_to(Vector2d(0.0, 1.0)))
        assert_that(Vector2d(0.0, 1.0).turned_right(), equal_to(Vector2d(1.0, 0.0)))

    def test_angle(self):
        """Testing of method Vector2d.angle."""
        angle_a = Vector2d(0.0, 1.0).angle(Vector2d(1.0, 0.0)) * 180.0 / math.pi
        angle_b = Vector2d(1.0, 0.0).angle(Vector2d(0.0, 1.0)) * 180.0 / math.pi
        assert_that(abs(angle_a - 90.0) <= 1e-10, equal_to(True))
        assert_that(abs(angle_b + 90.0) <= 1e-10, equal_to(True))

    def test_normalized(self):
        """Testing of method Vector2d.normalized."""
        normalized_vec_a = Vector2d(10.0, 0).normalized()
        normalized_vec_b = Vector2d(0.0, 10.0).normalized()
        assert_that(normalized_vec_a, equal_to(Vector2d(1.0, 0.0)))
        assert_that(normalized_vec_b, equal_to(Vector2d(0.0, 1.0)))

    def test_cross_product(self):
        """Testing of method Vector2d.cross_product."""
        assert_that(Vector2d(2.0, 5.0).cross_product(Vector2d(3.0, 4.0)), equal_to(-7.0))

    def test_eq(self):
        """Testing of method Vector2d.__eq__."""
        assert_that(Vector2d(1.2, 3.4), equal_to(Vector2d(1.2, 3.4)))
        assert_that(Vector2d(1.2, 3.4).__eq__(1234), equal_to(False))

    def test_neg(self):
        """Testing negating a vector."""
        assert_that(-Vector2d(1.0, 2.0), equal_to(Vector2d(-1.0, -2.0)))

    def test_is_perpendicular(self):
        """Testing method Vector2d.is_perpendicular."""
        assert_that(Vector2d(0.0, 1.0).is_perpendicular(Vector2d(1.0, 0.0)), equal_to(True))
        assert_that(Vector2d(1.0, 1.0).is_perpendicular(Vector2d(1.0, 0.0)), equal_to(False))
        assert_that(Vector2d(1.0, 1.0).is_perpendicular("hello world"), equal_to(False))
