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
# pylint: disable=R0201
import unittest
from hamcrest import assert_that, equal_to
from concept.mock import Attribute


class TestMockAttribute(unittest.TestCase):
    """Testing of mock attribute class."""

    def test_create_operation(self):
        """Testing values how it is used to represent a create operation."""
        attribute = Attribute(Attribute.CREATED, "foo", 99)
        assert_that(attribute.operation, equal_to(Attribute.CREATED))
        assert_that(attribute.name, equal_to("foo"))
        assert_that(attribute.given_value, equal_to(99))
        assert_that(attribute.new_value, equal_to(None))
        assert_that(str(attribute),
                    equal_to("Attribute(operation=created, name=foo, value=99)"))

    def test_change_operation(self):
        """Testing values how it is used to represent a change operation."""
        attribute = Attribute(Attribute.CHANGED, "foo", given_value=99, new_value=100)
        assert_that(attribute.operation, equal_to(Attribute.CHANGED))
        assert_that(attribute.name, equal_to("foo"))
        assert_that(attribute.given_value, equal_to(99))
        assert_that(attribute.new_value, equal_to(100))
        assert_that(str(attribute),
                    equal_to("Attribute(operation=changed, name=foo, value=99 -> 100)"))

    def test_read_operation(self):
        """Testing values how it is used to represent a read operation."""
        attribute = Attribute(Attribute.READ, "foo", 99)
        assert_that(attribute.operation, equal_to(Attribute.READ))
        assert_that(attribute.name, equal_to("foo"))
        assert_that(attribute.given_value, equal_to(99))
        assert_that(attribute.new_value, equal_to(None))
        assert_that(str(attribute),
                    equal_to("Attribute(operation=read, name=foo, value=99)"))

    def test_attribute_in_list(self):
        """Testing to find an attribute in a list."""
        some_attributes = [Attribute(Attribute.READ, "foo", 10),
                           Attribute(Attribute.READ, "foo", 11),
                           Attribute(Attribute.READ, "bar", 11),
                           Attribute(Attribute.CHANGED, "foo", 10, 11),
                           Attribute(Attribute.CHANGED, "foo", 10, 12)]

        pos = some_attributes.index(Attribute(Attribute.READ, "foo", 10))
        assert_that(pos >= 0 and str(some_attributes[pos]), equal_to(str(some_attributes[0])))
        pos = some_attributes.index(Attribute(Attribute.READ, "foo", 11))
        assert_that(pos >= 0 and str(some_attributes[pos]), equal_to(str(some_attributes[1])))
        pos = some_attributes.index(Attribute(Attribute.READ, "bar", 11))
        assert_that(pos >= 0 and str(some_attributes[pos]), equal_to(str(some_attributes[2])))
        pos = some_attributes.index(Attribute(Attribute.CHANGED, "foo", 10, 11))
        assert_that(pos >= 0 and str(some_attributes[pos]), equal_to(str(some_attributes[3])))
        pos = some_attributes.index(Attribute(Attribute.CHANGED, "foo", 10, 12))
        assert_that(pos >= 0 and str(some_attributes[pos]), equal_to(str(some_attributes[4])))

        some_attributes.insert(0, "abc")
        pos = some_attributes.index(Attribute(Attribute.READ, "foo", 10))
        assert_that(pos >= 0 and str(some_attributes[pos]), equal_to(str(some_attributes[1])))

    def test_cmp(self):
        """Testing compare."""
        assert_that(Attribute(Attribute.READ, "foo")
            .__cmp__(Attribute(Attribute.READ, "foo")), equal_to(0))
