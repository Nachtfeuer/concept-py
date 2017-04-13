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
from hamcrest import assert_that, equal_to, has_item, is_not
from concept.mock import Call


class TestMockCall(unittest.TestCase):
    """Testing of mock call class."""

    def test_name_only(self):
        """Testing call with no method arguments."""
        mock_call = Call("some_name")
        assert_that(str(mock_call), equal_to("Call(some_name)"))

    def test_name_and_value_arguments(self):
        """Testing call with value arguments."""
        mock_call = Call("some_name", 1024, 3.1415, "hello")
        assert_that(str(mock_call), equal_to("Call(some_name, 1024, 3.1415, hello)"))

    def test_name_and_keyword_arguments(self):
        """Testing call with keyword arguments."""
        mock_call = Call("some_name", a=1024, b=3.1415, c="hello")
        assert_that(str(mock_call), equal_to("Call(some_name, a=1024, b=3.1415, c=hello)"))

    def test_calls_in_list_with_names_only(self):
        """Testing to find a call in a list for calls with name only."""
        some_calls = [Call("one"), Call("two")]
        assert_that(some_calls, has_item(Call("one")))
        assert_that(some_calls, has_item(Call("two")))
        assert_that(some_calls, is_not(has_item(Call("three"))))

    def test_calls_in_list_with_name_and_value_arguments_only(self):
        """
        Testing to find a call in a list for calls with name and value arguments only.
        With has_item you cannot test THAT reliable.
        """
        some_calls = [Call("one", 1), Call("one", 1.1), Call("two", 2, 2.2), Call("two", 2, "two")]
        pos = some_calls.index(Call("one", 1))
        assert_that(pos >= 0 and str(some_calls[pos]), equal_to("Call(one, 1)"))
        pos = some_calls.index(Call("one", 1.1))
        assert_that(pos >= 0 and str(some_calls[pos]), equal_to("Call(one, 1.1)"))
        pos = some_calls.index(Call("two", 2, 2.2))
        assert_that(pos >= 0 and str(some_calls[pos]), equal_to("Call(two, 2, 2.2)"))
        pos = some_calls.index(Call("two", 2, "two"))
        assert_that(pos >= 0 and str(some_calls[pos]), equal_to("Call(two, 2, two)"))

        some_calls.insert(0, "abc")
        pos = some_calls.index(Call("one", 1))
        assert_that(pos >= 0 and str(some_calls[pos]), equal_to("Call(one, 1)"))

    def test_calls_in_set_with_name_and_value_arguments_only(self):
        """Testing the hashing aspect."""
        some_calls = set([Call("one", 1), Call("one", 1.1), Call("two", 2, 2.2), Call("two", 2, "two")])
        assert_that(Call("one", 1) in some_calls, equal_to(True))
        assert_that(Call("one", 2) in some_calls, equal_to(False))

    def test_compare(self):
        """Testing of Call.__cmp__."""
        assert_that(Call("one", 1).__cmp__(Call("one", 1)), equal_to(0))
        assert_that(Call("one", 1).__cmp__(None), equal_to(-1))
        assert_that(Call("one", 1).__cmp__(Call("one", 1, 2)), equal_to(-1))
        assert_that(Call("one", 1).__cmp__(Call("two", 1)), equal_to(-1))
        assert_that(Call("one", 1).__cmp__(Call("one", 2)), equal_to(-1))
        assert_that(Call("one", 1), is_not(equal_to(Call("one", 1, 3))))
