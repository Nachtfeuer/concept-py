"""
.. module:: variable
    :platform: Unix, Windows
    :synopis: represents a wrapper for a value

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
from concept.tools.serialize import Serializable


class Var(Serializable):
    """ a variable, represents a wrapper for a value """

    def __init__(self, value=None):
        """ initializes with value or None """
        super(Var, self).__init__()
        self.value = value

    def set(self, value):
        """
        Does change the value of the variable to new value.
        :param: value: new value for variable
        """
        self.value = value

    def get(self):
        """
        :rtype: returns current value of variable
        """
        return self.value

    def __eq__(self, other):
        """
        :param: other: expected to be another variable
        :rtype: True when other is a variable with same value
        """
        if not isinstance(other, Var):
            return False
        return self.value == other.get()

    def __repr__(self):
        """ string representation of this class """
        return u"Var(%s)" % self.value

    def is_enabled_for_attributes(self):
        """
        :rtype: True for writing the field as attribute of the tag
        """
        return True
