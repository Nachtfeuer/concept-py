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
from concept.tools.decorator import validate_test_responsibility_for
from concept.tools.validator import validator
from concept.data.schema import schema


@validate_test_responsibility_for(schema)
class TestValidator(unittest.TestCase):

    """ Testing schema class. """

    def test_init(self):
        """Testing schema.__init__."""
        scma = schema()
        assert_that(scma.description, equal_to({}))

    def test_add(self):
        """Testing schema add method."""
        scma = schema().add("first-name")
        assert_that(len(scma.description), equal_to(1))
        assert_that('first-name' in scma.description, equal_to(True))
        assert_that(scma.description['first-name']['name'], equal_to('first-name'))
        assert_that(scma.description['first-name']['type'], equal_to(str))

        # we cannot compare lambda instances so we have to test the given
        # default functionality which is checking the type:
        vidator = scma.description['first-name']['validator']
        assert_that(vidator.is_valid("hello"), equal_to(True))
        assert_that(vidator.is_valid(45), equal_to(False))

        scma = schema().add("first-name").add("first-name")
        assert_that(scma, equal_to(None))
        scma = schema().add("first-name", dict)
        assert_that(scma, equal_to(None))

    def test_build(self):
        """For now more or less just provided for readability."""
        scma = schema().build()
        assert_that(scma.description, equal_to({}))

    def test_is_valid(self):
        """Testing schema.is_valid (simple examples)."""
        scma = schema().add("name").build()
        assert_that(scma.is_valid(1234), equal_to(False))
        assert_that(scma.is_valid({'name': 'Barney'}), equal_to(True))
        assert_that(scma.is_valid({'NAME': 'Barney'}), equal_to(False))

        scma = schema().add("age", int).build()
        assert_that(scma.is_valid({'age': 45}), equal_to(True))
        assert_that(scma.is_valid({'age': "45"}), equal_to(False))

        vidator = validator().allow_values(range(1, 100+1)).build()
        scma = schema().add("age", int, vidator).build()
        assert_that(scma.is_valid({'age': 45}), equal_to(True))
        assert_that(scma.is_valid({'age': 0}), equal_to(False))
        assert_that(scma.is_valid({'age': 101}), equal_to(False))
