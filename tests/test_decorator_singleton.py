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
# pylint: disable=R0201,W0612,C0102,R0903,E0211,W0703,W0107,W0105,R0904
import unittest
from hamcrest import assert_that, equal_to, is_not
from concept.tools.decorator import singleton


class TestDecoratorSingleton(unittest.TestCase):

    """ Testing validator decorator. """

    def test_simple_singleton(self):
        """ simple singleton with no parameter. """
        @singleton
        class SimpleSingleton(object):

            """ just a test class. """

            pass

        instance_a = SimpleSingleton()
        instance_b = SimpleSingleton()
        assert_that(instance_a, equal_to(instance_b))

    def test_singleton_with_one_value_parameter(self):
        """ simple singleton with one value parameter. """
        @singleton
        class OneValueSingleton(object):

            """ just a test class. """

            def __init__(self, value):
                """ simple one value c'tor. """
                self.value = value

        instance_a = OneValueSingleton(12345)
        instance_b = OneValueSingleton(12345)
        instance_c = OneValueSingleton(54321)
        assert_that(instance_a, equal_to(instance_b))
        assert_that(instance_a.value, equal_to(instance_b.value))
        assert_that(instance_a, is_not(equal_to(instance_c)))
        assert_that(instance_a.value, is_not(equal_to(instance_c.value)))

    def test_singleton_with_named_value_parameter(self):
        """ simple singleton with one named value parameter. """
        @singleton
        class OneValueSingleton(object):

            """ just a test class. """

            def __init__(self, value):
                """ simple one value c'tor. """
                self.value = value

        instance_a = OneValueSingleton(value=12345)
        instance_b = OneValueSingleton(value=12345)
        instance_c = OneValueSingleton(value=54321)
        instance_d = OneValueSingleton(12345)
        assert_that(instance_a, equal_to(instance_b))
        assert_that(instance_a.value, equal_to(instance_b.value))
        assert_that(instance_a, is_not(equal_to(instance_c)))
        assert_that(instance_a.value, is_not(equal_to(instance_c.value)))
        assert_that(instance_a, is_not(equal_to(instance_d)))
        # that's the difference ... the way how the c'tor is used but the
        # stored value is different. Keep that in mind!
        assert_that(instance_a.value, equal_to(instance_d.value))
