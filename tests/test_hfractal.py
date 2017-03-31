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
from hamcrest import assert_that, equal_to
from concept.math.hfractal import HDefinition, hfractal
from concept.math.point import Point2d
from concept.math.vector import Vector2d


class TestHFractal(unittest.TestCase):
    """ Testing math H fractal. """

    def test_init_default(self):
        """Test HDefinition c'tor without specifying parameters."""
        hdef = HDefinition()
        assert_that(hdef.center_position, equal_to(Point2d()))
        assert_that(hdef.direction, equal_to(Vector2d(0.0, 1.0)))

    def test_generate_children(self):
        """Test HDefinition.generate_children method."""
        hdef = HDefinition()
        children = hdef.generate_children(shrink_factor=2.0)
        assert_that(len(children), equal_to(4))
        assert_that(children[0].center_position, equal_to(Point2d(-0.5, +0.5)))
        assert_that(children[1].center_position, equal_to(Point2d(+0.5, +0.5)))
        assert_that(children[2].center_position, equal_to(Point2d(-0.5, -0.5)))
        assert_that(children[3].center_position, equal_to(Point2d(+0.5, -0.5)))
        assert_that(all(child.direction == Vector2d(0.0, 0.5) for child in children),
                    equal_to(True))

    def test_generate_lines(self):
        """Test HDefinition.generate_lines method."""
        hdef = HDefinition()
        lines = hdef.generate_lines()
        assert_that(len(lines), equal_to(3))
        assert_that(lines[0][0], equal_to(Point2d(-0.5, -0.5)))
        assert_that(lines[0][1], equal_to(Vector2d(0.0, 1.0)))
        assert_that(lines[1][0], equal_to(Point2d(+0.5, -0.5)))
        assert_that(lines[1][1], equal_to(Vector2d(0.0, 1.0)))
        assert_that(lines[2][0], equal_to(Point2d(-0.5, 0.0)))
        assert_that(lines[2][1], equal_to(Vector2d(1.0, 0.0)))

    def test_hfractal_depth0(self):
        """Test hfractal function for max_depth=0."""
        hdefs = hfractal(Point2d(), Vector2d(0.0, 1.0), 2.0, 0)
        assert_that(len(hdefs), equal_to(1))
        assert_that(hdefs[0].center_position, equal_to(Point2d()))
        assert_that(hdefs[0].direction, equal_to(Vector2d(0.0, 1.0)))

    def test_hfractal_depth1(self):
        """Test hfractal function for max_depth=1."""
        hdefs = hfractal(Point2d(), Vector2d(0.0, 1.0), 2.0, 1)
        assert_that(len(hdefs), equal_to(5))
        assert_that(hdefs[0].center_position, equal_to(Point2d()))
        assert_that(hdefs[0].direction, equal_to(Vector2d(0.0, 1.0)))
        assert_that(hdefs[1].center_position, equal_to(Point2d(-0.5, +0.5)))
        assert_that(hdefs[1].direction, equal_to(Vector2d(0.0, 0.5)))
        assert_that(hdefs[2].center_position, equal_to(Point2d(+0.5, +0.5)))
        assert_that(hdefs[2].direction, equal_to(Vector2d(0.0, 0.5)))
        assert_that(hdefs[3].center_position, equal_to(Point2d(-0.5, -0.5)))
        assert_that(hdefs[3].direction, equal_to(Vector2d(0.0, 0.5)))
        assert_that(hdefs[4].center_position, equal_to(Point2d(+0.5, -0.5)))
        assert_that(hdefs[4].direction, equal_to(Vector2d(0.0, 0.5)))

    def test_hfractal_depth2(self):
        """Test hfractal function for max_depth=2."""
        hdefs = hfractal(Point2d(), Vector2d(0.0, 1.0), 2.0, 2)
        assert_that(len(hdefs), equal_to(1 + 4 + 16))
