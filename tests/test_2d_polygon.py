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
from concept.math.polygon import Polygon2d
from concept.math.point import Point2d
from concept.math.vector import Vector2d
from concept.math.line import Line2d


class TestPolygon2d(unittest.TestCase):
    """Testing math 2d polygon."""

    def test_init_with_point2d(self):
        """Testing initialize with list of 2d points."""
        polygon = Polygon2d([Point2d(0, 0), Point2d(2, 0), Point2d(1, 2)])
        assert_that(len(polygon), equal_to(3))
        assert_that(polygon.points[0], equal_to(Point2d(0, 0)))
        assert_that(polygon.points[1], equal_to(Point2d(2, 0)))
        assert_that(polygon.points[2], equal_to(Point2d(1, 2)))

    def test_init_with_tuple(self):
        """Testing initialize with list of 2d points."""
        polygon = Polygon2d([(0, 0), (2, 0), (1, 2)])
        assert_that(len(polygon), equal_to(3))
        assert_that(polygon.points[0], equal_to(Point2d(0, 0)))
        assert_that(polygon.points[1], equal_to(Point2d(2, 0)))
        assert_that(polygon.points[2], equal_to(Point2d(1, 2)))

    def test_translate_with_vector2d(self):
        """Testing moving a polygon via Vector2d."""
        polygon = Polygon2d([Point2d(0, 0), Point2d(2, 0), Point2d(1, 2)])
        polygon.translate(Vector2d(1, 2))
        assert_that(polygon.points[0], equal_to(Point2d(1, 2)))
        assert_that(polygon.points[1], equal_to(Point2d(3, 2)))
        assert_that(polygon.points[2], equal_to(Point2d(2, 4)))

    def test_translate_with_tuple(self):
        """Testing moving a polygon via tuple."""
        polygon = Polygon2d([Point2d(0, 0), Point2d(2, 0), Point2d(1, 2)])
        polygon.translate((1, 2))
        assert_that(polygon.points[0], equal_to(Point2d(1, 2)))
        assert_that(polygon.points[1], equal_to(Point2d(3, 2)))
        assert_that(polygon.points[2], equal_to(Point2d(2, 4)))

    def test_lines(self):
        """Testing Polygon2d.lines."""
        polygon = Polygon2d([(0, 0), (0, 1), (1, 1), (1, 0)])
        lines = polygon.lines()
        assert_that(len(lines), equal_to(4))
        assert_that(lines[0], equal_to(Line2d(Point2d(0, 0), Vector2d(0, 1))))
        assert_that(lines[1], equal_to(Line2d(Point2d(0, 1), Vector2d(1, 0))))
        assert_that(lines[2], equal_to(Line2d(Point2d(1, 1), Vector2d(0, -1))))
        assert_that(lines[3], equal_to(Line2d(Point2d(1, 0), Vector2d(-1, 0))))

    def test_vectors(self):
        """Testing Polygon2d.vectors."""
        polygon = Polygon2d([(0, 0), (0, 1), (1, 1), (1, 0)])
        vectors = polygon.vectors()
        assert_that(len(vectors), equal_to(4))
        assert_that(vectors[0], equal_to(Vector2d(0, 1)))
        assert_that(vectors[1], equal_to(Vector2d(1, 0)))
        assert_that(vectors[2], equal_to(Vector2d(0, -1)))
        assert_that(vectors[3], equal_to(Vector2d(-1, 0)))

    def test_area(self):
        """Testing Polygon2d.area."""
        polygon = Polygon2d([(0, 0), (0, 1), (1, 1), (1, 0)])
        assert_that(polygon.area(), equal_to(1.0))
        polygon = Polygon2d([(0, 0), (1, 0), (1, 1), (0, 1)])
        assert_that(polygon.area(), equal_to(1.0))

    def test_is_convex_clockwise(self):
        """Testing Polygon2d.is_convex."""
        polygon = Polygon2d([(0, 0), (0, 1), (1, 1), (1, 0)])
        assert_that(polygon.is_convex(), equal_to(True))
        polygon = Polygon2d([(0.75, 0.75), (0, 1), (1, 1), (1, 0)])
        assert_that(polygon.is_convex(), equal_to(False))

        # TODO: how to find out that a polygon is clockwise?
        # why does that fail, when it anti clockwise?
        # I believe it's the sign of the angle
        # query that "orientation" :is_clockwise? whatever the
        # offical naming is for that!
        # polygon = Polygon2d([(0, 0), (1, 0), (1, 1), (0, 1)])
        # assert_that(polygon.is_convex(), equal_to(True))

    def test_contains(self):
        """Testing Polygon2d.contains."""
        polygon = Polygon2d([(0, 0), (0, 1), (1, 1), (1, 0)])
        assert_that(calling(polygon.contains).with_args(Point2d(0.5, 0.5),
                    raises(NotImplementedError)))

    def test_is_regular(self):
        """Testing Polygon2d.is_regular."""
        polygon = Polygon2d([(0, 0), (0, 1), (1, 1), (1, 0)])
        assert_that(calling(polygon.is_regular), raises(NotImplementedError))

    def test_is_complex(self):
        """Testing Polygon2d.is_complex."""
        polygon = Polygon2d([(0, 0), (0, 1), (1, 1), (1, 0)])
        assert_that(calling(polygon.is_complex), raises(NotImplementedError))

    def test_convex_is_clockwise(self):
        """Testing Polygon2d.is_clockwise."""
        polygon = Polygon2d([(0, 0), (0, 1), (1, 1), (1, 0)])
        assert_that(polygon.is_clockwise(), equal_to(True))
        polygon = Polygon2d([(0, 0), (1, 0), (1, 1), (0, 1)])
        assert_that(polygon.is_clockwise(), equal_to(False))

    def test_concav_is_clockwise(self):
        """Testing Polygon2d.is_clockwise."""
        polygon = Polygon2d([(0.75, 0.75), (0, 1), (1, 1), (1, 0)])
        assert_that(polygon.is_clockwise(), equal_to(True))
        polygon = Polygon2d([(0.75, 0.75), (1, 0), (1, 1), (0, 1)])
        assert_that(polygon.is_clockwise(), equal_to(False))
