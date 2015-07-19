"""
   Validator tool.

.. module:: validator
    :platform: Unix, Windows
    :synopis: validator tool.

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


class validator(object):

    """
    Common validator functionality.

    You can use one or multiple values, a range or a list of values.
    You can specify a function to verify a value.
    If you have specified a function then you don't have to
    specify a value too (optional then).

    >>> v = validator().allow_values(1, 3, 6, 9).build()
    >>> [v.is_valid(n) for n in [1, 2, 3, 4, 5, 6]]
    [True, False, True, False, False, True]
    >>> v = validator().allow_values(range(1, 3+1)).build()
    >>> [v.is_valid(n) for n in [0, 1, 2, 3, 4]]
    [False, True, True, True, False]
    >>> v = validator().verify_by(lambda n: n % 2 == 0).build()
    >>> [v.is_valid(n) for n in range(1, 6+1)]
    [False, True, False, True, False, True]
    """

    def __init__(self):
        """ initializing fields only. """
        self.valid_values = []
        self.verify_functions = []

    def allow_values(self, *values):
        """
        Adding one or more valid values.

        :param values: one or more values that are valid.
        :returns: itself for further processing.
        """
        for value in values:
            if validator.is_type(value, list):
                self.valid_values += value
            elif validator.is_type(value, range):
                self.valid_values += list(value)
            else:
                self.valid_values.append(value)
        return self

    def verify_by(self, function):
        """
        Register function to verify one value.

        :param function: one function that can verify a value returning True or False.
        :returns: itself for further processing.
        """
        self.verify_functions.append(function)
        return self

    def build(self):
        """ :returns: itself for further processing. """
        return self

    def is_valid(self, value):
        """
        Checking given value to be valid.

        :param value: value to check to be valid.
        :returns: True when given value is considered as valid.
        """
        if len(self.verify_functions) > 0:
            if not all([verify(value) for verify in self.verify_functions]):
                return False

            return len(self.valid_values) == 0 or value in self.valid_values
        else:
            return value in self.valid_values

    @staticmethod
    def is_type(value, expected_type):
        """
        Check type of value to be expected one.

        :param value: any value
        :param expected_type: any type
        :returns: True when given value has expected type.
        """
        try:
            return isinstance(value, expected_type)
        except TypeError:
            return False
