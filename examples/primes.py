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
import sys
import platform
import click
from concept.primes.sieve_of_eratosthenes import sieve_of_eratosthenes
from concept.primes.sieve_of_eratosthenes_optimized import sieve_of_eratosthenes_optimized
from concept.performance.measurement import track_duration_of


@click.command()
@click.option("--max-number", default=1000, help="maximum number for sieve (default: 1000)")
@click.option("--sieve", default="default", help="sieve algorithm (default: standard eratosthenes)")
@click.option("--columns", default=20, help="number of columns per line (default: 10)")
def main(max_number, sieve, columns):
    """
    Prime tool.

    :param max_number: creating a sieve up to this number
    :param sieve: sieve algorithms ("default" or "optimized")
    :param columns: number of prime columns
    """
    print("prime tool")
    print(" ... Python %s" % sys.version.replace("\n", ""))
    print(" ... Platform %s\n" % platform.platform())

    if max_number < 2:
        print(" ... no primes for max. number %d" % max_number)
        sys.exit(1)

    sieve_algorithm = None
    if sieve == "default":
        sieve_algorithm = sieve_of_eratosthenes(max_number)
    elif sieve == "optimized":
        sieve_algorithm = sieve_of_eratosthenes_optimized(max_number)

    sieve_duration = track_duration_of(sieve_algorithm.calculate)

    primes = [2]
    primes_duration = track_duration_of(lambda: \
        primes.extend([n for n in range(3, max_number+1, 2) if sieve_algorithm.is_prime(n)]))

    prime_format = "%%%dd" % len("%d" % (max_number+1))
    text = ""
    column = 0
    for prime in primes:
        text += prime_format % prime
        column += 1
        if column % columns == 0:
            text += "\n"
    text += "\n"

    print(text)
    print(" ... %d primes found." % len(primes))
    print(" ... sieve calculation took %f seconds" % sieve_duration)
    print(" ... prime calculation took %f seconds" % primes_duration)


if __name__ == "__main__":
    main()
