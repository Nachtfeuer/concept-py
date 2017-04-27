"""
   Math rectangle 2d and 3d.

.. module:: rectangle
    :platform: Unix, Windows
    :synopis: math rectangle 2d and 3d.

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


class Rectangle2d(object):
    """Math 2d rectangle implementation."""

    def __init__(self, position, width, height, direction=Vector2d(1, 0)):
        """Initialize Rectangle."""
        self.position = position
        self.width = width
        self.height = height
        self.direction = direction.normalized()

    def __repr__(self):
        """:returns: String representation of the given rectangle 2d instance."""
        text = "Rectangle2d(position=%(position)s" % self.__dict__
        text += ", width=%(width)s" % self.__dict__
        text += ", height=%(height)s" % self.__dict__
        text += ", direction=%(direction)s)" % self.__dict__
        return text

    def top_left(self):
        """:returns: top left position."""
        return self.position

    def bottom_right(self):
        """:returns: bottom right position."""
        return self.position + \
            (self.direction.scaled(self.width) +
             self.direction.turned_right().scaled(self.height))

    def __eq__(self, other):
        """:returns: True when both rectangle data are identical."""
        if not isinstance(other, Rectangle2d):
            return False
        return self.position == other.position and \
            self.width == other.width and \
            self.height == other.height and \
            self.direction == other.direction

    def rotate(self, angle):
        """Rotate rectangle by given angle."""
        self.direction = self.direction.rotated(angle)
