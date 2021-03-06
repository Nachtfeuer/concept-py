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
from concept.primes.is_prime import is_prime
from concept.primes.sieve_of_eratosthenes_optimized import sieve_of_eratosthenes_optimized


class TestSieveOfEratosthenesOptimized(unittest.TestCase):

    """ Testing prime sieve. """

    def test_sieve(self):
        """ Testing prime generation. """
        sieve = sieve_of_eratosthenes_optimized(20)
        sieve.calculate()
        assert_that([2, 3, 5, 7, 11, 13, 17, 19], equal_to(sieve.get_primes()))

    def test_is_sieve(self):
        """ Testing is_sieve method. """
        sieve = sieve_of_eratosthenes_optimized(101)
        sieve.calculate()

        expected = [n for n in range(1, 100 + 1) if is_prime(n)]
        given = [2] + [n for n in range(3, 100 + 1, 2) if sieve.is_prime(n)]
        assert_that(given, equal_to(expected))
