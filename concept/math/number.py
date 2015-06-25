"""
   Number functions.

.. module:: functions
    :platform: Unix, Windows
    :synopis: math number functions.

.. moduleauthor:: Thomas Lehmann <thomas.lehmann.private@googlemail.com>

   =======
   License
   =======
   Copyright (c) 2015 Thomas Lehmann

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
from concept.math.factorization import probe


def is_square(value):
    """
    Checking value to be a square.

    :param value: value to be checked to be a square
    :returns: true when given value is a square.

    >>> [n for n in range(1, 100+1) if is_square(n)]
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    """
    square_root = math.sqrt(value)
    return square_root == int(square_root)


def triangle(nth):
    """
    Providing n'th triangle number.

    :param nth: index for n'th triangle
    :returns: n'th triangle number
    see http://en.wikipedia.org/wiki/Triangular_number

    >>> triangle(3)
    6
    >>> triangle(4)
    10
    """
    return (nth * (nth + 1)) // 2


def is_triangle(number):
    """
    Check given number to be a triangle number.

    :param number: value to be checked to be a triangle number.
    :returns: True when given value is a triangle number
    see http://en.wikipedia.org/wiki/Triangular_number

    >>> is_triangle(10)
    True
    >>> is_triangle(4)
    False
    """
    return is_square(8 * number + 1)


def pentagonal(nth):
    """
    Providing n'th pentagonal number.

    :param nth: index for n'th pentagonal
    :returns: n'th pentagonal number
    see http://en.wikipedia.org/wiki/Pentagonal_number

    >>> pentagonal(3)
    12
    >>> pentagonal(4)
    22
    """
    return (nth * (3 * nth - 1)) // 2


def is_pentagonal(number):
    """
    Check given number to be a pentagonal number.

    :param number: value to be checked to be a pentagonal number.
    :returns: True when given value is a pentagonal number
    see http://en.wikipedia.org/wiki/Pentagonal_number

    >>> is_pentagonal(12)
    True
    >>> is_pentagonal(13)
    False
    """
    value = (math.sqrt(24 * number + 1) + 1) / 6.0
    return value > 0.0 and value == int(value)


def hexagonal(nth):
    """
    Providing n'th hexagonal number.

    :param nth: index for n'th hexagonal
    :returns: n'th hexagonal number
    see http://en.wikipedia.org/wiki/Hexagonal_number

    >>> hexagonal(3)
    15
    >>> hexagonal(4)
    28
    """
    return nth * (2 * nth - 1)


def is_hexagonal(number):
    """
    Check given number to be a hexagonal number.

    :param number: value to be checked to be a hexagonal number.
    :returns: True when given value is a hexagonal number
    see http://en.wikipedia.org/wiki/Hexagonal_number

    >>> is_hexagonal(15)
    True
    >>> is_hexagonal(14)
    False
    """
    value = (math.sqrt(8 * number + 1) + 1) / 4.0
    return value == int(value)


def is_abundant(number):
    """
    Check number to be a abundant number; 12 is the first (1+2+3+4+6=16 which is greater than 12).

    :returns: true when the sum of the divisors of the given number is greater as the number
    see http://en.wikipedia.org/wiki/Abundant_number

    >>> is_abundant(12)
    True
    >>> is_abundant(13)
    False
    """
    return (sum(probe(number)) - number) > number
