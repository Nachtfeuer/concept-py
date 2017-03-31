"""
   Generator for a defined ranged.

.. module:: select
    :platform: Unix, Windows
    :synopis: Generator for a defined range.

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
import random


class select(object):
    """Container query functionality."""

    def __init__(self, from_value, to_value, step_value):
        """
        Initializing with range parameters.

        :param from_value: start of range
        :param to_value: end of range
        :param step_value: step value
        """
        self.from_value = from_value
        self.to_value = to_value
        self.step_value = step_value
        self.filter_functions = []
        self.transform_functions = []

    def where(self, filter_function):
        """
        Register a where clause for filtering entries.

        :param filter_function: accepts one parameter and returns True to keep the entry.
        :returns: self to allow applying further filter and transformation.

        >>> select(1, 10, 1).where(lambda n: n % 2 == 0).build()
        [2, 4, 6, 8, 10]
        """
        assert callable(filter_function)
        self.filter_functions.append(filter_function)
        return self

    def transform(self, transform_function):
        """
        Register a trasnformation clause for changing entries.

        :param filter_function: accepts one parameter and returns True to keep the entry.
        :returns: self to allow applying further filter and transformation.

        >>> select(1, 10, 1).transform(lambda n: n**2).build()
        [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        """
        assert callable(transform_function)
        self.transform_functions.append(transform_function)
        return self

    def build(self):
        """
        Provide final result(s) after applying filters and transformations.

        >>> select(1, 10, 1).build()
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        >>> select(1, 10, 2).build()
        [1, 3, 5, 7, 9]
        """
        condition = lambda a, b: a <= b
        if self.step_value < 0:
            condition = lambda a, b: a >= b

        results = []
        current = self.from_value
        while condition(current, self.to_value):
            ignore = False
            for filter_function in self.filter_functions:
                if not filter_function(current):
                    ignore = True
                    break

            if not ignore:
                value = current
                for transform_function in self.transform_functions:
                    value = transform_function(value)
                results.append(value)

            current += self.step_value

        return results

    def sum(self):
        """
        Calculate sum of entries.

        :returns: sum of entries.

        >>> select(1, 10, 1).sum()
        55
        >>> select(1, 10, 1).transform(lambda n: n**2).sum()
        385
        """
        return sum(self.build())

    def average(self):
        """
        Calculate average of entries.

        :returns: average of entries.

        >>> select(1, 3, 1).average()
        2.0
        >>> select(1, 2, 1).average()
        1.5
        """
        results = self.build()
        return sum(results) / float(len(results))

    def min(self):
        """
        Calculate minimum of entries.

        :returns: minimum of entries.

        >>> select(3, 1, -1).min()
        1
        """
        return min(self.build())

    def max(self):
        """
        Calculate maximum of entries.

        :returns: maximum of entries.

        >>> select(1, 3, 1).max()
        3
        """
        return max(self.build())

    def median(self):
        """
        Calculate median of entries.

        :returns: median of entries.

        >>> select(1, 3, 1).median()
        2.0
        >>> select(3, 0, -1).median()
        1.5
        """
        results = self.build()
        results.sort()

        if len(results) % 2 == 0:
            pos = len(results) // 2 - 1
            return (results[pos] + results[pos + 1]) / 2.0

        return float(results[len(results) // 2])

    def shuffled(self):
        """
        Shuffle values in the list.

        :returns: shuffled values.
        """
        results = self.build()
        random.shuffle(results)
        return results
