#!/usr/bin/python
"""
Sequence generator tool.

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
import itertools
import click
from concept.math.functions import square, increment, decrement, multiply
from concept import VERSION


@click.command()
@click.option("--max-number", default=20, help="maximum number for formula (default: 10)")
def main(max_number):
    """
    Sequence generator tool.

    :param max_number: creating a sieve up to this number
    """
    print("sequence generator tool (version %s)" % VERSION)
    print(" ... Python %s" % sys.version.replace("\n", ""))
    print(" ... Platform %s" % platform.platform())

    available_functions = [square(), increment(), increment(offset=2), decrement(),
                           decrement(offset=2), multiply()]
    max_functions = len(available_functions)

    for permutation in itertools.permutations(available_functions, max_functions):
        formula = permutation[-1]
        current = formula

        for function in reversed(permutation[:-1]):
            current.decorate(function)
            function.decorate(None)
            current = function

        print("%s" % formula)
        print(" ... %s" % " ".join([str(formula(n)) for n in range(max_number+1)]))


if __name__ == "__main__":
    main()
