"""
   =======
   License
   =======
   Copyright (c) 2016 Thomas Lehmann

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
import unittest
from hamcrest import assert_that, equal_to
from concept.query.matcher import  Matcher


class TestMatcher(unittest.TestCase):

    """ Testing of Matcher. """

    def test_left_of_with_text_only(self):
        """ Testing of Matcher.left_of method. """
        matcher = Matcher("some text")
        assert_that(matcher.left_of(" text").text, equal_to("some"))

    def test_left_of_with_regex(self):
        """ Testing of Matcher.left_of method. """
        matcher = Matcher("some 1234567")
        assert_that(matcher.left_of(" [0-9]+").text, equal_to("some"))

    def test_right_of_with_text_only(self):
        """ Testing of Matcher.right_of method. """
        matcher = Matcher("some text")
        assert_that(matcher.right_of("some ").text, equal_to("text"))

    def test_right_of_with_regex(self):
        """ Testing of Matcher.right_of method. """
        matcher = Matcher("1234567 text")
        assert_that(matcher.right_of("[0-9]+ ").text, equal_to("text"))

    def test_replace_with_text_only(self):
        """ Testing of Matcher.replace method. """
        matcher = Matcher("some text")
        assert_that(matcher.replace("text", "other text").text,
                    equal_to("some other text"))

    def test_replace_with_regex(self):
        """ Testing of Matcher.replace method. """
        matcher = Matcher("some 1234567")
        assert_that(matcher.replace("[0-9]+", "text").text,
                    equal_to("some text"))

    def test_replace_find_all(self):
        """ Testing of Matcher.find_all method. """
        matcher = Matcher("abc 123 xyz 456 ijk 789")
        assert_that(matcher.find_all("[0-9]+"),
                    equal_to(['123', '456', '789']))
