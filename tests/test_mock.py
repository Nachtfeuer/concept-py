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
from concept.mock import Mock


class TestMock(unittest.TestCase):

    """ Testing of mock class. """

    def test_default_with_no_arguments(self):
        """ Testing default c'tor with no arguments. """
        mock = Mock()
        assert_that(len(mock.mock_history()), equal_to(1))
        assert_that(str(mock.mock_history()[0]), equal_to("Call(__init__)"))

    def test_default_with_value_arguments(self):
        """ Testing default c'tor with no value arguments. """
        mock = Mock(1024, 3.1415, "hello")
        assert_that(len(mock.mock_history()), equal_to(1))
        assert_that(str(mock.mock_history()[0]),
                    equal_to("Call(__init__, 1024, 3.1415, hello)"))

    def test_default_with_named_arguments(self):
        """
        Testing default c'tor with key arguments.
        The order of the keys is not necessarily the same as in the call.
        """
        mock = Mock(age=100, pi=3.1415, message="hello")
        assert_that(len(mock.mock_history()), equal_to(1))
        assert_that(str(mock.mock_history()[0]),
                    equal_to("Call(__init__, age=100, message=hello, pi=3.1415)"))

    def test_default_with_value_arguments_and_named_arguments(self):
        """
        Testing default c'tor with value arguments as well as key arguments.
        The order of the keys is not necessarily the same as in the call.
        """
        mock = Mock(1024, "world", age=100, pi=3.1415)
        assert_that(len(mock.mock_history()), equal_to(1))
        assert_that(str(mock.mock_history()[0]),
                    equal_to("Call(__init__, 1024, world, age=100, pi=3.1415)"))

    def test_one_method_call_with_no_arguments(self):
        """
        Method foo does not exist.
        So we should have now the c'tor call as well as the call to foo().
        """
        mock = Mock()
        mock.foo()
        assert_that(len(mock.mock_history()), equal_to(2))
        assert_that(str(mock.mock_history()[0]), equal_to("Call(__init__)"))
        assert_that(str(mock.mock_history()[1]), equal_to("Call(foo)"))

    def test_one_referenced_method_call_with_no_arguments(self):
        """
        Testing referenced method call with no arguments.
        Method foo does not exist (as before).
        Here we store "foo" in a variable; the variable foo is a second mock.
        Of course we want to have the call "registered" in the first one which
        we are basically "referencing".
        """
        mock = Mock()
        foo = mock.foo
        foo()
        assert_that(len(mock.mock_history()), equal_to(2))
        assert_that(str(mock.mock_history()[0]), equal_to("Call(__init__)"))
        assert_that(str(mock.mock_history()[1]), equal_to("Call(foo)"))

    def test_one_referenced_method_call_with_value_arguments(self):
        """
        Testing referenced method call with with value arguments.
        Method foo does not exist (as before).
        Here we store "foo" in a variable; the variable foo is a second mock.
        Of course we want to have the call "registered" in the first one which
        we are basically "referencing".
        """
        mock = Mock()
        foo = mock.foo
        foo(1024, 3.1415, "hello")
        assert_that(len(mock.mock_history()), equal_to(2))
        assert_that(str(mock.mock_history()[0]), equal_to("Call(__init__)"))
        assert_that(str(mock.mock_history()[1]), equal_to("Call(foo, 1024, 3.1415, hello)"))

    def test_one_referenced_method_call_with_key_arguments(self):
        """
        Testing referenced method call with with key arguments.
        Method foo does not exist (as before).
        Here we store "foo" in a variable; the variable foo is a second mock.
        Of course we want to have the call "registered" in the first one which
        we are basically "referencing".
        """
        mock = Mock()
        foo = mock.foo
        foo(age=100, pi=3.1415, message="hello")
        assert_that(len(mock.mock_history()), equal_to(2))
        assert_that(str(mock.mock_history()[0]), equal_to("Call(__init__)"))
        assert_that(str(mock.mock_history()[1]),
                    equal_to("Call(foo, age=100, message=hello, pi=3.1415)"))

    def test_one_referenced_method_call_with_value_arguments_and_named_arguments(self):
        """
        Testing referenced method call with with value arguments and key arguments.
        Method foo does not exist (as before).
        Here we store "foo" in a variable; the variable foo is a second mock.
        Of course we want to have the call "registered" in the first one which
        we are basically "referencing".
        """
        mock = Mock()
        foo = mock.foo
        foo(1024, "world", age=100, pi=3.1415)
        assert_that(len(mock.mock_history()), equal_to(2))
        assert_that(str(mock.mock_history()[0]), equal_to("Call(__init__)"))
        assert_that(str(mock.mock_history()[1]),
                    equal_to("Call(foo, 1024, world, age=100, pi=3.1415)"))

    def test_create_attribute(self):
        """
        Testing assigning an attribute a value that does not exist.
        The history not contains calls and attribute operations (here: "created")
        """
        mock = Mock()
        mock.age = 99
        assert_that(len(mock.mock_history()), equal_to(2))
        assert_that(str(mock.mock_history()[0]), equal_to("Call(__init__)"))
        assert_that(str(mock.mock_history()[1]),
                    equal_to("Attribute(operation=created, name=age, value=99)"))

    def test_change_attribute(self):
        """
        Testing assigning an attribute a value that does exist.
        The history not contains calls and attribute operations (here: "created" and "changed")
        """
        mock = Mock()
        mock.age = 99   # create attribute
        mock.age = 100  # change attribute
        assert_that(len(mock.mock_history()), equal_to(3))
        assert_that(str(mock.mock_history()[0]), equal_to("Call(__init__)"))
        assert_that(str(mock.mock_history()[1]),
                    equal_to("Attribute(operation=created, name=age, value=99)"))
        assert_that(str(mock.mock_history()[2]),
                    equal_to("Attribute(operation=changed, name=age, value=99 -> 100)"))

    def test_read_attribute(self):
        """
        Testing assigning an attribute a value that does exist.
        The history not contains calls and attribute operations (here: "created" and "changed")
        """
        mock = Mock()
        mock.age = 99   # create attribute
        assert_that(mock.age, equal_to(99))
        assert_that(len(mock.mock_history()), equal_to(3))
        assert_that(str(mock.mock_history()[0]), equal_to("Call(__init__)"))
        assert_that(str(mock.mock_history()[1]),
                    equal_to("Attribute(operation=created, name=age, value=99)"))
        assert_that(str(mock.mock_history()[2]),
                    equal_to("Attribute(operation=read, name=age, value=99)"))

    def test_call(self):
        """ Testing __call__. """
        mock = Mock()
        # the idea is - of course - different which is something like:
        #   foo = mock.foo
        #   foo()
        mock(1, 3.14, "hello")
        assert_that(len(mock.mock_history()), equal_to(2))
        assert_that(str(mock.mock_history()[1]),
                    equal_to("Call(__init__, 1, 3.14, hello)"))
