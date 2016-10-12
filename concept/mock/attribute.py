"""
   Represents attribute operations and states.

.. module:: call
    :platform: Unix, Windows
    :synopis: Represents attribute operations and states.

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
from concept.tools.compatible import compare


class Attribute(object):

    """ Represents mock attribute state for create, read and write and the relating values. """

    CREATED = "created"
    CHANGED = "changed"
    READ = "read"

    def __init__(self, operation, name, given_value=None, new_value=None):
        """
        Storing attribute operation and relevant data.

        :param operation: CREATED, CHANGED or READ
        :param name: name of attribute
        :param given_value: value when created or the value you read
        :param new_value: new value when changing an attribute
        """
        assert operation in [self.CREATED, self.CHANGED, self.READ]
        assert isinstance(name, str)
        self.operation = operation
        self.name = name
        self.given_value = given_value
        self.new_value = new_value

    def __repr__(self):
        """ :return: string representation of an instance of this class. """
        if self.operation in [self.CREATED, self.READ]:
            text = "Attribute(operation=%(operation)s, name=%(name)s, value=%(given_value)s)"
            return text % self.__dict__

        text = "Attribute(operation=%(operation)s, name=%(name)s," + \
               " value=%(given_value)s -> %(new_value)s)"
        return text % self.__dict__

    def __eq__(self, other):
        """ Comparing two attributes two be equal. """
        if not isinstance(other, Attribute):
            return False
        if not self.name == other.name:
            return False
        if not self.given_value == other.given_value:
            return False
        return self.new_value == other.new_value

    def __cmp__(self, other):
        """ Compare two attributes. """
        if not isinstance(other, Attribute):
            return compare(str(self), str(other))

        diff = compare(self.operation, other.operation)
        if not diff == 0:
            return diff

        diff = compare(self.name, other.name)
        if not diff == 0:
            return diff

        diff = compare(self.given_value, other.given_value)
        if not diff == 0:
            return diff

        return compare(self.new_value, other.new_value)
