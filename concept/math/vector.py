"""
   Math vector 2d and 3d.

.. module:: vector
    :platform: Unix, Windows
    :synopis: math vector 2d and 3d.

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


class Vector2d(object):
    """
    Math vector 2d implementation.

    >>> a = Vector2d(3, 4)
    >>> b = Vector2d(1, 3)
    >>> a + b
    Vector2d(x=4, y=7)
    >>> a - b
    Vector2d(x=2, y=1)
    >>> a.scalar_product(b)
    15.0
    >>> a.length()
    5.0
    >>> a.scaled(2)
    Vector2d(x=6, y=8)
    >>> a.normalized().length()
    1.0
    >>> 180.0 / math.pi * Vector2d(0.0, 1.0).angle(Vector2d(1.0, 0.0))
    90.0
    >>> v = Vector2d(0.0, 1.0).rotated(-math.pi/180.0 * 90.0)
    >>> abs(v.x - 1.0) < 1e-10 and abs(v.y) < 1e-10
    True
    """

    def __init__(self, x=0.0, y=0.0):
        """Initialize vector."""
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        """:returns: String representation of the given vector 2d instance."""
        return "Vector2d(x=%(x)g, y=%(y)g)" % self.__dict__

    def __add__(self, other):
        """
        Sum of two vectors.

        $\vec{a} + \vec{b} = \begin{pmatrix}a_x + b_x\\a_y + b_y\end{pmatrix}$
        """
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Subtraction of two 2d vectors.

        :math: `\vec{a} - \vec{b} = \begin{pmatrix}a_x - b_x\\a_y - b_y\end{pmatrix}`
        :returns: new 2d vector instance.
        """
        return Vector2d(self.x - other.x, self.y - other.y)

    def scalar_product(self, other):
        """
        Scalar (dot) product of two 2d vectors.

        :math: `\vec{a} \cdot \vec{b} = a_x \cdot b_x + a_y \cdot b_y`
        :param other: another 2d vector instance
        :returns: scalar product of two 2d vectors.
        """
        assert isinstance(other, Vector2d)
        return self.x * other.x + self.y * other.y

    def cross_product(self, other):
        """
        Cross product of two vectors.

        :param other: another 2d vector instance
        :returns: float value representing cross product of two vectors.
        """
        assert isinstance(other, Vector2d)
        return self.x * other.y - self.y * other.x

    def length(self):
        """:returns: length of the vector."""
        return math.sqrt(self.scalar_product(self))

    def scale(self, factor):
        """
        Scale current vector by given factor.

        :param factor: integer or float value expected
        """
        assert isinstance(factor, int) or isinstance(factor, float)
        self.x *= factor
        self.y *= factor

    def scaled(self, factor):
        """
        Provide scaled vector by given factor; current instance will not be changed.

        :param factor: integer or float value expected
        :return: new scaled 2d vector instance
        """
        assert isinstance(factor, int) or isinstance(factor, float)
        return Vector2d(self.x * factor, self.y * factor)

    def normalized(self):
        """
        Provide a normalized vector (vector length is 1).
        """
        return self.scaled(1.0 / self.length())

    def angle(self, other):
        """
        Calculate angle between two vectors.

        :param other: another 2d vector
        :returns: angle between two vectors (unit: rad).
        """
        assert isinstance(other, Vector2d)
        return math.atan2(self.y, self.x) - math.atan2(other.y, other.x)

    def turned_left(self):
        """
        Provide vector rotated 90 degrees left.

        :returns: new 2d vector instance.
        """
        return Vector2d(-self.y, self.x)

    def turned_right(self):
        """
        Provide vector rotated 90 degrees right.

        :returns: new 2d vector instance.
        """
        return Vector2d(self.y, -self.x)

    def rotated(self, rotation_angle):
        """
        Provide angle rotated by given angle.

        :param rotation_angle: angle to use for rotation (unit: rad)
        :returns: new 2d vector instance.
        """
        return Vector2d(self.x * math.cos(rotation_angle) - self.y * math.sin(rotation_angle),
                        self.x * math.sin(rotation_angle) + self.y * math.cos(rotation_angle))

    def __eq__(self, other):
        """Comparing two vectors to be equal."""
        if isinstance(other, Vector2d):
            return abs(self.x - other.x) < 1e-10 and abs(self.y - other.y) < 1e-10
        return False

    def inversed(self):
        """:returns: inversed vector (rotated by 180 degrees)."""
        return Vector2d(-self.x, -self.y)
