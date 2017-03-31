"""
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
# pylint: disable=R0201
import unittest
from hamcrest import assert_that, equal_to
from concept.math.functions import function, square, increment, decrement, multiply


class TestFunctions(unittest.TestCase):

    """ Testing of function objects. """

    def test_base(self):
        """ Testing base class. """
        func1 = function(lambda x: 2 * x)
        assert_that(func1.other_function(10), equal_to(20))

        func2 = function()
        assert_that(func2.other_function, equal_to(None))
        func2.decorate(lambda x: x + 1)
        assert_that(func2.other_function(10), equal_to(11))

    def test_square(self):
        """ Testing square function. """
        func = square()
        assert_that(1024, equal_to(func(32)))
        assert_that("x^2", equal_to(str(func)))
        func = square(square())
        assert_that("x^2^2", equal_to(str(func)))
        assert_that(256, equal_to(func(4)))

    def test_increment(self):
        """ Testing increment function. """
        func = increment()
        assert_that(1000, equal_to(func(999)))
        assert_that("(x + 1)", equal_to(str(func)))
        func = increment(increment())
        assert_that("((x + 1) + 1)", equal_to(str(func)))
        assert_that(1001, equal_to(func(999)))

    def test_decrement(self):
        """ Testing decrement function. """
        func = decrement()
        assert_that(999, equal_to(func(1000)))
        assert_that("(x - 1)", equal_to(str(func)))
        func = decrement(decrement())
        assert_that("((x - 1) - 1)", equal_to(str(func)))
        assert_that(998, equal_to(func(1000)))

    def test_multiply(self):
        """ Testing multiply function. """
        func = multiply()
        assert_that(20, equal_to(func(10)))
        assert_that("(x * 2)", equal_to(str(func)))
        func = multiply(multiply())
        assert_that("((x * 2) * 2)", equal_to(str(func)))
        assert_that(40, equal_to(func(10)))
