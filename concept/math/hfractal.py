"""
   Math H fractal.

.. module:: hfractal
    :platform: Unix, Windows
    :synopis: math H fractal.

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


class HDefinition(object):
    """One H definition as part of an H fractal."""

    def __init__(self, center_position=Point2d(), direction=Vector2d(0.0, 1.0)):
        """Initialize with center coordinates and direction (and size)."""
        self.center_position = center_position
        self.direction = direction

    def generate_lines(self):
        """Provide the 3 lines for given "H"."""
        opvec = self.direction.scaled(0.5)
        return [
            (self.center_position - opvec + opvec.turned_left(), self.direction),
            (self.center_position - opvec + opvec.turned_right(), self.direction),
            (self.center_position + opvec.turned_left(), self.direction.turned_right())
        ]

    def generate_children(self, shrink_factor=3.0):
        """
        Provide children being further H drawins on each tip of the vertica H line.
        :param shrink_factor: each child is usually smaller. The factory define the final size.
        :returns list with four children.
        """
        factor = 1.0/shrink_factor
        opvec = self.direction.scaled(0.5)
        children = []
        children.append(HDefinition(
            self.center_position + opvec + opvec.turned_left(),
            self.direction.scaled(factor)))
        children.append(HDefinition(
            self.center_position + opvec + opvec.turned_right(),
            self.direction.scaled(factor)))
        children.append(HDefinition(
            self.center_position - opvec + opvec.turned_left(),
            self.direction.scaled(factor)))
        children.append(HDefinition(
            self.center_position - opvec + opvec.turned_right(),
            self.direction.scaled(factor)))
        return children


def hfractal(initial_position, initial_direction, shrink_factor, max_depth):
    """
    Generate all H objects depending on given parameters.
    :param initial_position: usually the center point (0, 0).
    :param initial_direction: direction and size of the biggest "H".
    :param shrink_factor: float to use to shrink each child.
    :param max_depth: defines how often to generate children of a given "H".
    """
    assert isinstance(initial_position, Point2d)
    assert isinstance(initial_direction, Vector2d)
    assert isinstance(shrink_factor, float) and shrink_factor > 1.0
    assert isinstance(max_depth, int) and max_depth >= 0

    root = HDefinition(initial_position, initial_direction)
    all_hdefs = [root]
    current_hdefs = [root]
    for _ in range(max_depth):
        new_hdefs = []
        for hdef in current_hdefs:
            new_hdefs.extend(hdef.generate_children(shrink_factor))
        current_hdefs = new_hdefs
        all_hdefs.extend(current_hdefs)
    return all_hdefs
