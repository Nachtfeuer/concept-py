"""
   Testing concept.math.number functions.

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
import unittest
from hamcrest import assert_that, equal_to
from concept.math.number import is_square, triangle, is_triangle, pentagonal, is_pentagonal


class TestNumber(unittest.TestCase):

    """ Testing of number functions. """

    def test_is_square(self):
        """ Testing is_square function. """
        given = [n for n in range(1, 100+1) if is_square(n)]
        expected = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        assert_that(expected, equal_to(given))

    def test_triangle(self):
        """ Testing triangle function. """
        given = [triangle(n) for n in range(1, 10+1)]
        expected = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        assert_that(given, equal_to(expected))

    def test_is_triangle(self):
        """ Testing is_triangle function. """
        assert_that(is_triangle(10), equal_to(True))
        assert_that(is_triangle(4), equal_to(False))

    def test_penatgonal(self):
        """ Testing pentagonal function. """
        given = [pentagonal(n) for n in range(1, 10+1)]
        expected = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
        assert_that(given, equal_to(expected))

    def test_is_pentagonal(self):
        """ Testing is_pentagonal function. """
        assert_that(is_pentagonal(23), equal_to(False))
        assert_that(is_pentagonal(22), equal_to(True))
        assert_that(is_pentagonal(21), equal_to(False))
