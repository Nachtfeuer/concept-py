"""
.. module:: function
    :platform: Unix, Windows
    :synopis: represents functions behaving like variables

.. moduleauthor:: Thomas Lehmann <thomas.lehmann.private@googlemail.com>

   =======
   License
   =======
   Copyright (c) 2017 Thomas Lehmann

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
from concept.variables.variable import Var


class Function(Var):
    """ A class as base for function classes keeping a decorated function
        or variable calculating a value """

    def __init__(self, value):
        """ initializing with a variable or function (like this class) """
        if not (isinstance(value, Var) or issubclass(value.__class__, Var)):
            raise TypeError("wrong type")

        super(Function, self).__init__(value)

    def __repr__(self):
        """ string representation of this or derived class """
        return "%s(%s)" % (self.__class__.__name__, self.value)


class Square(Function):
    """ A class that calculates the square of the decorated function
        or variable """

    def __init__(self, value):
        """ initializing with a variable or function (like this class) """
        super(Square, self).__init__(value)

    def get(self):
        """ returns f(x) = x*x """
        return self.value.get() ** 2


class Sqrt(Function):
    """ A class that calculates the square root of the decorated function
        or variable """

    def __init__(self, value):
        """ initializing with a variable or function (like this class) """
        super(Sqrt, self).__init__(value)

    def get(self):
        """ returns f(x) = sqrt(x) """
        return math.sqrt(self.value.get())


class Sin(Function):
    """ A class that calculates the sin of the decorated function
        or variable """

    def __init__(self, value):
        """ initializing with a variable or function (like this class) """
        super(Sin, self).__init__(value)

    def get(self):
        """ returns f(x) = x*x """
        return math.sin(self.value.get())
