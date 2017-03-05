"""
   Math polygon 2d.

.. module:: polygon
    :platform: Unix, Windows
    :synopis: math polygon 2d.

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
import math
from concept.math.point import Point2d
from concept.math.vector import Vector2d
from concept.math.line import Line2d


class Polygon2d(object):
    """Math 2d polygon."""

    def __init__(self, points):
        """
        Initialize polygon with points.

        :param points: list of 2d point instances.
        """
        if all(isinstance(point, Point2d) for point in points):
            self.points = points
        elif all(isinstance(point, tuple) and all(isinstance(coord, (float, int)) for coord in point)
                 for point in points):
            self.points = [Point2d(point[0], point[1]) for point in points]
        else:
            raise TypeError("invalid parameter type")

    def __len__(self):
        """:returns: number of points in polygon."""
        return len(self.points)

    def add_point(self, point):
        """
        Adding a point.

        :param point: point to be used to add
        """
        if isinstance(point, Point2d):
            self.points.append(point)
        elif isinstance(point, tuple) and all(isinstance(coord, (float, int)) for coord in point):
            self.points.append(Point2d(point[0], point[1]))
        else:
            raise TypeError("invalid parameter type")

    def translate(self, direction):
        """
        Translate points into dx and dy by given direction.
        :param direction: 2d vector or a tuple of two floats for dx and dy
        """
        if isinstance(direction, Vector2d):
            for point in self.points:
                point += direction
        elif isinstance(direction, tuple) and all(isinstance(coord, (float, int)) for coord in direction):
            for point in self.points:
                point.x += direction[0]
                point.y += direction[1]
        else:
            raise TypeError("invalid parameter type")

    def lines(self):
        """:returns: lines of the polygon."""
        data = []
        max_index = len(self.points)-1
        for pix in range(max_index):
            data.append(
                Line2d(self.points[pix],
                       self.points[pix+1] - self.points[pix]))

        data.append(Line2d(self.points[max_index],
                           self.points[0] - self.points[max_index]))
        return data

    def vectors(self):
        """:returns: list of vectors representing this polygon."""
        data = []
        max_index = len(self.points)-1
        for pix in range(max_index):
            data.append(self.points[pix+1] - self.points[pix])

        data.append(self.points[0] - self.points[max_index])
        return data

    def area(self):
        """:returns: area of polygon."""
        max_index = len(self.points)-1
        total = 0.0
        for pix in range(max_index):
            total += self.points[pix].x * self.points[pix+1].y - \
                     self.points[pix].y * self.points[pix+1].x
        total += self.points[max_index].x * self.points[0].y - \
                 self.points[max_index].y * self.points[0].x
        return abs(total / 2.0)

    def contains(self, point):
        """
        Verify whether point is inside polygon.

        :param point: point to be used to check
        :returns: True when point is in polygon.
        """
        raise NotImplementedError()

    def is_convex(self):
        """
        Check whether there is no angle pointing inwards (angle <= 180.0 degrees).

        :returns: True when polyon is convex.
        """
        max_index = len(self.points)-1
        for pix in range(max_index+1):
            if pix == 0:
                pixmin = max_index
                pixmax = pix+1
            elif pix == max_index:
                pixmin = pix-1
                pixmax = 0
            else:
                pixmin = pix-1
                pixmax = pix+1

            vec_a = self.points[pixmax] - self.points[pix]
            vec_b = self.points[pixmin] - self.points[pix]
            if vec_a.angle(vec_b) > math.pi:
                return False

        return True

    def is_complex(self):
        """
        Check whether one line segment intersects with another.

        :returns: True when polyon is complex.
        """
        raise NotImplementedError()

    def is_regular(self):
        """
        Check that all angles and all sides are equal.

        :returns: True when polygon is regular.
        """
        raise NotImplementedError()

    def is_valid(self):
        """
        Verifies that polygon is valid.
        :returns: True when polygon is valid otherwise False
        """
        return len(self.points) >= 3
