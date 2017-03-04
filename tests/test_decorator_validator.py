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
from hamcrest import assert_that, equal_to
from concept.tools.decorator import validate_test_responsibility_for


class TestDecoratorValidator(unittest.TestCase):
    """Testing validator decorator."""

    def test_simple_fail(self):
        """simple example were a missing test does raise an exception."""
        class Foo(object):
            """just a test class."""

            def bar():
                """just a test function."""
                pass

        try:
            @validate_test_responsibility_for(Foo)
            class TestFoo(object):
                """Test class for class Foo."""

                pass
            # we should not get here:
            assert_that(True, equal_to(False))
        except Exception as exception:
            expected = "\n...failed to provide test method 'TestFoo.test_bar' for method 'Foo.bar'"
            assert_that(str(exception), equal_to(expected))

    def test_simple_succeed(self):
        """simple example were a missing test does not raise an exception."""
        class Foo2(object):
            """just a test class."""

            def bar():
                """just a test function."""
                pass

        # should not raise an exception
        @validate_test_responsibility_for(Foo2)
        class TestFoo2(object):
            """Test class for class Foo2."""

            def test_bar(self):
                """test function for method 'bar'."""
                pass

    def test_simple_equal(self):
        """simple example for special handling of __eq__."""
        class Foo3(object):
            """just a test class."""

            def __eq__(self, other):
                """just a test function."""
                return False

        # should not raise an exception
        @validate_test_responsibility_for(Foo3)
        class TestFoo3(object):
            """Test class for class Foo3."""

            def test_equal(self):
                """test function for method '__eq__'."""
                pass

    def test_simple_less(self):
        """simple example for special handling of __lt__."""
        class Foo4(object):
            """just a test class."""

            def __lt__(self, other):
                """just a test function."""
                return False

        # should not raise an exception
        @validate_test_responsibility_for(Foo4)
        class TestFoo4(object):
            """Test class for class Foo4."""

            def test_less(self):
                """test function for method '__lt__'."""
                pass

    def test_simple_greater(self):
        """simple example for special handling of __gt__."""
        class Foo5(object):
            """just a test class."""

            def __gt__(self, other):
                """just a test function."""
                return False

        # should not raise an exception
        @validate_test_responsibility_for(Foo5)
        class TestFoo5(object):
            """Test class for class Foo5."""

            def test_greater(self):
                """test function for method '__gt__'."""
                pass
                """just a test function."""

