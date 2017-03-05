"""
   Math line 2d and 3d.

.. module:: line
    :platform: Unix, Windows
    :synopis: math line 2d and 3d.

.. moduleauthor:: Thomas Lehmann <thomas.lehmann.private@googlemail.com>

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
from concept.math.point import Point2d
from concept.math.vector import Vector2d
from concept.errors.exceptions import UnsupportedOperation


class Line2d(object):
    """Math 2d line implementation."""

    def __init__(self, position, direction):
        """
        Initialize line.

        :param position: start of the 2d line.
        :param direction: direction and length of line.
        """
        assert isinstance(position, Point2d)
        assert isinstance(direction, Vector2d)
        self.position = position
        self.direction = direction

    def __repr__(self):
        """:returns: String representation of the given line 2d instance."""
        return "Line2d(position=%(position)s, direction=%(direction)s)" % self.__dict__

    def length(self):
        """:returns: length of line."""
        return self.direction.length()

    def angle(self, other):
        """:returns: Angle between two lines."""
        assert isinstance(other, Line2d)
        return self.direction.angle(other.direction)

    def turned_left(self):
        """
        Provide new 2d line rotated 90 degree to the left.

        :returns: new 2d line.
        """
        return Line2d(Point2d(self.position.x, self.position.y),
                      self.direction.turned_left())

    def turned_right(self):
        """
        Provide new 2d line rotated 90 degree to the right.

        :returns: new 2d line.
        """
        return Line2d(Point2d(self.position.x, self.position.y),
                      self.direction.turned_right())

    def intersection(self, other):
        """
        Provide intersection 2d point when given.
        :returns: 2d point or raise an exception when lines are parallel.
        """
        raise NotImplementedError("not yet implemented")

    def is_parallel(self, other):
        """
        Check two lines to be parallel.

        Two lines are parallel when either have same direction or reverse direction.
        :returns: True when both lines are parallel.
        """
        if isinstance(other, Line2d):
            direction_a = self.direction.normalized()
            direction_b = other.direction.normalized()
            if direction_a == direction_b or direction_a == direction_b.inversed():
                return True
            return False
        raise UnsupportedOperation("parallel check for two lines only")

    def point(self, factor):
        """
        Provide point on the line given by factor.

        When the factor is 0.0 then it's the start of the line.
        When the factor is 1.0 then it's the end of line.
        When the factor is 0.5 then it's the middle of the line.
        :returns: 2d point
        """
        return self.position + self.direction.scaled(factor)
