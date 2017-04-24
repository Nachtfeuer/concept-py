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
from concept.query.select import select


class TestQuerySelect(unittest.TestCase):

    """ Testing of select functionality. """

    def test_select_no_function(self):
        """ Testing select without 'where' and 'transform'. """
        entries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = entries
        given = select(entries).build()
        assert_that(given, equal_to(expected))

    def test_select_with_one_where_clause(self):
        """ Testing select with one 'where' call. """
        entries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [n for n in entries if n % 2 == 0]
        given = select(entries).where(lambda n: n % 2 == 0).build()
        assert_that(given, equal_to(expected))

    def test_select_with_multiple_where_clause(self):
        """ Testing select with multiple 'where' calls. """
        entries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [n for n in entries if n % 2 == 0 and 4 <= n <= 8]
        given = select(entries) \
            .where(lambda n: n % 2 == 0) \
            .where(lambda n: 4 <= n <= 8) \
            .build()
        assert_that(given, equal_to(expected))

    def test_select_with_one_transform(self):
        """ Testing select with one 'transform' call. """
        entries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [n ** 2 for n in entries]
        given = select(entries).transform(lambda n: n ** 2).build()
        assert_that(given, equal_to(expected))

    def test_select_with_multiple_transform(self):
        """ Testing select with multiple 'transform' calls. """
        entries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [n ** 2 + 1 for n in entries]
        given = select(entries) \
            .transform(lambda n: n ** 2) \
            .transform(lambda n: n + 1) \
            .build()
        assert_that(given, equal_to(expected))

    def test_sum(self):
        """ Testing sum of elements. """
        assert_that(select([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).sum(), equal_to(55))

    def test_sum_with_where_clause(self):
        """ Testing sum of elements. """
        assert_that(select([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                    .where(lambda n: n % 2 == 0).sum(), equal_to(30))

    def test_average(self):
        """ Testing average of elements. """
        assert_that(select([1, 2, 3]).average(), equal_to(2))
        assert_that(select([1, 2]).average(), equal_to(1.5))

    def test_average_with_where_clause(self):
        assert_that(select([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                    .where(lambda n: n % 2 == 0).average(), equal_to(6))

    def test_min(self):
        """ Testing minimum of elements. """
        assert_that(select([3, 2, 1]).min(), equal_to(1))

    def test_max(self):
        """ Testing maximum of elements. """
        assert_that(select([1, 2, 3]).max(), equal_to(3))

    def test_median(self):
        """ Testing median of elements. """
        assert_that(select([2, 3, 1]).median(), equal_to(2.0))
        assert_that(select([3, 2, 1, 0]).median(), equal_to(1.5))
