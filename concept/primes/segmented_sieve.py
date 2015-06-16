"""
   Creating prime sieve.

.. module:: segmented sieve
    :platform: Unix, Windows
    :synopis: creating prime sieve

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
from concept.primes.sieve_of_eratosthenes import sieve_of_eratosthenes
import math


class segmented_sieve(object):

    """ Segmented prime sieve. """

    def __init__(self, max_n):
        """ initializing sieve for given maximum value. """
        self.max_n = max_n
        self.initial_limit = int(math.sqrt(max_n))
        self.sieve = sieve_of_eratosthenes(self.initial_limit)
        self.primes = []

    def calculate(self):
        """ calculating all primes. """
        # calculating primes up to to square root of maximum number
        self.sieve.calculate()
        self.primes = [2] + [n for n in range(3, self.initial_limit+1, 2) if self.sieve.is_prime(n)]

        segment_size = max(10, (self.max_n - self.initial_limit) // 10)
        other_primes = []

        low = self.initial_limit
        high = min(low + segment_size, self.max_n)
        current = low

        while low < high:
            # TODO: the creation of the segment ... can this be done before loop?
            # (compare creation vs. initialization performance!!!)
            segment = [True] * (high-low+1)
            for prime in self.primes:
                current = low
                remainder = current % prime
                if remainder > 0:
                    current = low - remainder + prime
                while current <= high:
                    # TODO: -low .... can be improved by doing it before loop?
                    segment[current-low] = False
                    current += prime

            # TODO: question: is a loop better than using range? (check performance!!!)
            other_primes += [n for n in range(low, high+1) if segment[n-low]]

            low = high + 1
            high = min(low + segment_size, self.max_n)

        self.primes.extend(other_primes)

    def get_primes(self):
        """
        Providing all primes.

        :returns: list of primes
        """
        return self.primes
