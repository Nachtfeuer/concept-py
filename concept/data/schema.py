"""
   Schema tool.

.. module:: schema
    :platform: Unix, Windows
    :synopis: schema tool.

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
from concept.tools.validator import validator


class schema(object):

    """
    Schema is something like a description of a data class with validation. with validation.

    Basic look and feel. Please check the unit test to see more examples.
    >>> s = schema().add('first-name').add('surname').build()
    >>> s.is_valid({'first-name': 'Agatha', 'surname': 'Christie'})
    True

    The name 'sur-name' does not exist in schema:
    >>> s = schema().add('first-name').add('surname').build()
    >>> s.is_valid({'first-name': 'Agatha', 'sur-name': 'Christie'})
    False

    The type is 'str' not 'int':
    >>> s = schema().add('first-name').add('surname').build()
    >>> s.is_valid({'first-name': 'Agatha', 'surname': 1234})
    False

    The type is 'int' not 'str':
    >>> s = schema().add('age', int).build()
    >>> s.is_valid({'age': 45})
    True
    >>> s.is_valid({'age': "45"})
    False
    """

    def __init__(self):
        """ initialzing fields only. """
        self.description = {}

    def add(self, field_name, field_type=str, field_validator=None):
        """
        Adding a new field.

        :param field_name: mandatory. is a name. cannot be added twice.
        :param field_type: default is str. will be added to validator.
                           can be one of int, float, str, list.
        :param field_validator: flexible validor for the field value.
                                The default does at least verify the type.
        :returns: None when failed otherwise the instance itself for further processing.
        """
        # avoiding registering twice
        if not field_name or not isinstance(field_name, str) or field_name in self.description:
            return None
        # checking for supported type
        if field_type not in [int, float, str, list]:
            return None

        # not specifying a validator the default is taken always being valid when type does fit.
        if field_validator is None:
            field_validator = validator().verify_by(lambda value: isinstance(value, field_type))
        elif not isinstance(field_validator, validator):
            return None
        else:
            field_validator.verify_by(lambda value: isinstance(value, field_type))

        self.description[field_name] = {
            'name': field_name,
            'type': field_type,
            'validator': field_validator
        }

        return self

    def build(self):
        """
        provided for readability.

        :returns: schema instance
        """
        return self

    def is_valid(self, data):
        """ :returns: True when given data fits to given schema. """
        if not isinstance(data, dict):
            return False

        for key in data:
            if key not in self.description:
                return False
            if not self.description[key]['validator'].is_valid(data[key]):
                return False

        return True
