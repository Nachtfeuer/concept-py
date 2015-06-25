"""
   Creating prime sieve (optimized version).

.. module:: sieve_of_eratosthenes_optimized
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
import math


class sieve_of_eratosthenes_optimized(object):

    """ Prime sieve. """

    def __init__(self, max_n):
        """ Initialize sieve. """
        self.max_n = max_n
        self.sieve = [True] * (self.max_n//2 + 1)
        self.sieve[0] = False
        self.sieve[1] = True

    def calculate(self):
        """ Strike out all multiples of a prime as none prime. """
        limit = int(math.sqrt(self.max_n))

        value_i = 3
        while value_i <= limit:
            if self.sieve[value_i//2]:
                value_j = value_i**2
                offset = 2*value_i
                while value_j <= self.max_n:
                    self.sieve[value_j//2] = False
                    value_j += offset

            value_i += 2

    def get_primes(self):
        """
        Get all primes.

        :returns: list of primes
        """
        return [2]+[n for n in range(3, self.max_n+1, 2) if self.sieve[n//2]]

    def is_prime(self, value):
        """
        Checking sieve for value.

        It's expected that given value is a odd value since
        the sieve does ignore even values.

        :param value: value to be checked to be a prime.
        :returns: True when given number is a prime.
        """
        return self.sieve[value//2]
