"""
   Math function objects.

.. module:: functions
    :platform: Unix, Windows
    :synopis: math functions objects

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


class function(object):

    """ Base class for concrete functions like 'square'. """

    def __init__(self, other_function=None):
        """ initializing function to be decorated in c'tor. """
        self.other_function = other_function

    def decorate(self, other_function):
        """ initializing function to be decorated after instantiation. """
        self.other_function = other_function


class square(function):

    """
    Providing square of either the return value of a function or a float value itself.

    >>> square()(4)
    16
    >>> square(square())(4)
    256
    """

    def __init__(self, func=None):
        """
        Initializing fields.

        :param func: optional another function to be decoratored.
        """
        super(square, self).__init__(func)

    def __call__(self, value):
        """
        Executing the square function.

        :param value: value to use for square.
        :returns: squared value or even squared return value of another function
        """
        if self.other_function:
            return self.other_function(value)**2
        return value**2

    def __repr__(self):
        """ string representation of current function. """
        if self.other_function:
            return "%s^2" % str(self.other_function)
        return "x^2"


class increment(function):

    """
    So basically we have a y=f(x)=x+b function with b=1 as default.

    >>> increment()(9)
    10
    >>> increment(increment())(8)
    10
    """

    def __init__(self, func=None, offset=1):
        """
        Initializing fields.

        :param func: another function that can be defined.
        :param offset: the value to increment (default: 1)
        """
        super(increment, self).__init__(func)
        self.offset = offset

    def __call__(self, value):
        """
        Executing the increment function.

        :param value: value to use for increment.
        :returns: incremented value or even incremented return value of another function
        """
        if self.other_function:
            return self.other_function(value) + self.offset
        return value + self.offset

    def __repr__(self):
        """ string representation of current function. """
        if self.other_function:
            return "(%s + %d)" % (str(self.other_function), self.offset)
        return "(x + %d)" % self.offset


class decrement(function):

    """
    So basically we have a y=f(x)=x-b function with b=1 as default.

    >>> decrement()(9)
    8
    >>> decrement(decrement())(9)
    7
    """

    def __init__(self, func=None, offset=1):
        """
        Initializing fields.

        :param func: another function that can be defined.
        :param offset: the value to decrement (default: 1)
        """
        super(decrement, self).__init__(func)
        self.offset = offset

    def __call__(self, value):
        """
        Executing the increment function.

        :param value: value to use for increment.
        :returns: decremented value or even decremented return value of another function
        """
        if self.other_function:
            return self.other_function(value) - self.offset
        return value - self.offset

    def __repr__(self):
        """ string representation of current function. """
        if self.other_function:
            return "(%s - %d)" % (str(self.other_function), self.offset)
        return "(x - %d)" % self.offset


class multiply(function):

    """
    So basically we have a y=f(x)=x*f function with f=2 as default.

    >>> multiply()(2)
    4
    >>> multiply(multiply())(2)
    8
    """

    def __init__(self, func=None, factor=2):
        """
        Initializing fields.

        :param func: another function that can be defined.
        :param factor: the value to multiply (default: 2)
        """
        super(multiply, self).__init__(func)
        self.factor = factor

    def __call__(self, value):
        """
        Executing the multiply function.

        :param value: value to use for multiply.
        :returns: multiplied value or even multiplied return value of another function
        """
        if self.other_function:
            return self.other_function(value) * self.factor
        return value * self.factor

    def __repr__(self):
        """ string representation of current function. """
        if self.other_function:
            return "(%s * %d)" % (str(self.other_function), self.factor)
        return "(x * %d)" % self.factor
