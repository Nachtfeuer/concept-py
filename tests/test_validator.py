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


@validate_test_responsibility_for(validator)
class TestValidator(unittest.TestCase):

    """ Testing validator class. """

    def test_init(self):
        """ Testing validator.__init__. """
        vidator = validator()
        assert_that(vidator.valid_values, equal_to([]))

    def test_allow_values(self):
        """ Testing validator.allow_values. """
        vidator = validator().allow_values(1, 4, 9, 16).build()
        assert_that(vidator.is_valid(4), equal_to(True))
        assert_that(vidator.is_valid(3), equal_to(False))

    def test_is_valid(self):
        """ Testing validator.is_valid. """
        # at least one funtion OR one value is required to be specified otherwise it fail:
        assert_that(validator().build().is_valid(1234), equal_to(False))
        # correct value:
        assert_that(validator().allow_values(1234).build().is_valid(1234), equal_to(True))
        # wrong value:
        assert_that(validator().allow_values(4321).build().is_valid(1234), equal_to(False))

    def test_build(self):
        """ Testing validator.__init__. """
        vidator = validator()
        assert_that(vidator.build().valid_values, equal_to([]))

    def test_is_type(self):
        """ Testing validator.is_type. """
        assert_that(validator.is_type(1234, int), equal_to(True))
        assert_that(validator.is_type(3.1415, float), equal_to(True))
        assert_that(validator.is_type([1, 2, 3], list), equal_to(True))
        assert_that(validator.is_type((1, 2, 3), tuple), equal_to(True))
        assert_that(validator.is_type({'a': 1, 'b': 2, 'c': 3}, dict), equal_to(True))
        assert_that(validator.is_type(1234, 12.34), equal_to(False))

    def test_using_range(self):
        """ Testing validator.allow_values using a range. """
        vidator = validator().allow_values(range(1, 10 + 1)).build()
        assert_that(vidator.is_valid(0), equal_to(False))
        assert_that(vidator.is_valid(1), equal_to(True))
        assert_that(vidator.is_valid(10), equal_to(True))
        assert_that(vidator.is_valid(11), equal_to(False))

    def test_using_list(self):
        """ Testing validator.allow_values using a list. """
        vidator = validator().allow_values(list(range(1, 10 + 1))).build()
        assert_that(vidator.is_valid(0), equal_to(False))
        assert_that(vidator.is_valid(1), equal_to(True))
        assert_that(vidator.is_valid(10), equal_to(True))
        assert_that(vidator.is_valid(11), equal_to(False))

    def test_verify_by(self):
        """ Testing validator.verify_by. """
        vidator = validator().verify_by(lambda n: n % 2 == 0).build()
        for value in range(100 + 1):
            assert_that(vidator.is_valid(value), equal_to(value % 2 == 0))
