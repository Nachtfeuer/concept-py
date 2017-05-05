"""
   Mock class that tries to simulate to be something else.

.. module:: mock
    :platform: Unix, Windows
    :synopis: Mock class that tries to simulate to be something else.

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
from concept.mock.call import Call
from concept.mock.attribute import Attribute


class Mock(object):
    """
    The mock class is for tracking of actions.

    Actions are methods calls and read or write operation to attributes.
    """

    def __init__(self, *args, **kwargs):
        """initializing mock data and adding c'tor call to history."""
        self.__data = {'name': '__init__', 'attributes': {}, 'key/value': {},
                       'history': [], 'reference': None}
        self.mock_add_call('__init__', *args, **kwargs)

    def mock_history(self):
        """:returns: history of actions."""
        return self.__data['history']

    def mock_add_call(self, name, *args, **kwargs):
        """
        Adding a c'tor or method call to history.

        :param name: name of the method.
        :param args: used value arguments for the method call.
        :param kwargs: used keyword arguments for the method call.
        """
        self.__data['history'].append(Call(name, *args, **kwargs))

    def mock_add_change(self, name, value):
        """
        Adding create/change of attribute to history.

        :param name: name of the attribute.
        :param value: initial/new value for the attribute.
        """
        if name not in self.__data['attributes']:
            self.__data['history'].append(
                Attribute(operation=Attribute.CREATED, name=name, given_value=value))
        else:
            self.__data['history'].append(
                Attribute(operation=Attribute.CHANGED,
                          name=name,
                          given_value=self.__data['attributes'][name],
                          new_value=value))

    def mock_add_read(self, name, value):
        """
        Adding read of attribute to history.

        :param name: name of the attribute.
        :param value: current value for the attribute.
        """
        self.__data['history'].append(
            Attribute(operation=Attribute.READ, name=name, given_value=value))

    def mock_reference(self, name, other):
        """
        When called then delegate all to that mock instance.

        :param name: name of the reference.
        :param other: other mock to use.
        """
        assert isinstance(name, str) and isinstance(other, Mock)
        self.__data['name'] = name
        self.__data['reference'] = other

    def __getattr__(self, name):
        """
        Retreiving attribute or function by name.

        :param name: name of "something"
        :return: a registered attribute or another mock if not known.
        """
        if name in self.__data['attributes']:
            value = self.__data['attributes'][name]
            self.mock_add_read(name, value)
            return value
        # we don't know what <name> is so we provide a mock for it
        mock = Mock()
        mock.mock_reference(name, self)
        return mock

    def __setattr__(self, name, value):
        """
        Basic mechanism of changing an attribute.

        :param name: name of attribute.
        :param value: value for the attribute
        """
        if name == "_Mock__data":
            super(Mock, self).__setattr__(name, value)
        else:
            self.mock_add_change(name, value)
            self.__data['attributes'][name] = value

    def __call__(self, *args, **kwargs):
        """
        Call as a function.

        :param args: used value arguments.
        :param kwargs: used keyword arguments.
        :return: None at the moment (can be changed later on).
        """
        if self.__data['reference']:
            return self.__data['reference'].mock_add_call(self.__data['name'], *args, **kwargs)

        return self.mock_add_call(self.__data['name'], *args, **kwargs)
