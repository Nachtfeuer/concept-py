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
import unittest
from hamcrest import assert_that, equal_to
from concept.primes.segmented_sieve import segmented_sieve
from concept.primes.is_prime import is_prime


class TestSegmentedSieve(unittest.TestCase):

    """ Testing segmented prime sieve. """

    def test_sieve(self):
        """ Testing prime generation. """
        sieve = segmented_sieve(20)
        sieve.calculate()
        assert_that([2, 3, 5, 7, 11, 13, 17, 19], equal_to(sieve.get_primes()))

    def test_sieve_with_is_prime(self):
        sieve = segmented_sieve(10000)
        sieve.calculate()
        primes = [n for n in range(10000+1) if is_prime(n)]
        assert_that(primes, equal_to(sieve.get_primes()))


