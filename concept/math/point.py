"""
   Math point 2d and 3d.

.. module:: point
    :platform: Unix, Windows
    :synopis: math point 2d and 3d.

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
from concept.math.vector import Vector2d
from concept.errors.exceptions import UnsupportedOperation


class Point2d(object):
    """Math 2d point implementation."""

    def __init__(self, x=0.0, y=0.0):
        """Initializing point (default: x=0.0, y=0.0)."""
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        """:returns: String representation of the given point 2d instance."""
        return "Point2d(x=%(x)g, y=%(y)g)" % self.__dict__

    def __sub__(self, other):
        """:returns Vector2d representing direction and distance betwee two points."""
        if isinstance(other, Point2d):
            return Vector2d(self.x - other.x, self.y - other.y)
        if isinstance(other, Vector2d):
            return Point2d(self.x - other.x, self.y - other.y)
        raise UnsupportedOperation("operation pointa-pointb allowed only")

    def __add__(self, other):
        """Add a 2d vector to get another point."""
        if isinstance(other, Vector2d):
            return Point2d(self.x + other.x, self.y + other.y)
        raise UnsupportedOperation("operation point+vector allowed only")

    def __eq__(self, other):
        """Comparing two points to be equal."""
        if isinstance(other, Point2d):
            return abs(self.x - other.x) < 1e-10 and abs(self.y - other.y) < 1e-10
        return False
