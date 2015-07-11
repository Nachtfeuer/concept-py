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
from concept.math.digits import sum_digits, count_digits, is_pandigital, is_palindrome


class TestDigits(unittest.TestCase):

    """ Testing of digit function. """

    def test_sum_digits(self):
        """ Testing sum_digits function. """
        assert_that(sum_digits(1024), equal_to(7))
        assert_that(sum_digits(1234567890), equal_to(45))
        assert_that(sum_digits(-1234567890), equal_to(45))

    def test_count_digits(self):
        """ Testing count_digits function. """
        assert_that(count_digits(0), equal_to(1))
        assert_that(count_digits(1024), equal_to(4))
        assert_that(count_digits(1234567890), equal_to(10))
        assert_that(count_digits(-1234567890), equal_to(10))

    def test_is_pandigital(self):
        """ Testing is_pandigital function. """
        assert_that(is_pandigital(1234567890), equal_to(True))
        assert_that(is_pandigital(9876543210), equal_to(True))
        assert_that(is_pandigital(1024), equal_to(True))
        assert_that(is_pandigital(10240), equal_to(False))
        assert_that(is_pandigital(1223), equal_to(False))

    def test_is_palindrome(self):
        """ Testing is_palindrome function. """
        assert_that(is_palindrome(123454321), equal_to(True))
        assert_that(is_palindrome(1222221), equal_to(True))
        assert_that(is_palindrome(22), equal_to(True))
        assert_that(is_palindrome(-22), equal_to(True))
        assert_that(is_palindrome(1231), equal_to(False))
        assert_that(is_palindrome(1321), equal_to(False))
