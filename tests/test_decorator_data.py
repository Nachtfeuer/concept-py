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
import os
import unittest
from hamcrest import assert_that, equal_to
from concept.tools.decorator import data


class TestDecoratorData(unittest.TestCase):

    """ Testing data decorator. """

    def test_simple_list(self):
        """ Providing simple list as data call test once. """
        @data(values=[1, 2, 3, 4, 5])
        def test1(values):
            return values

        assert_that(test1(), equal_to([1, 2, 3, 4, 5]))

    def test_simple_file(self):
        """ Reading content of a file; still calling test once. """
        @data(file=__file__)
        def test2(values):
            return values[0].split("\n")[2].strip()

        assert_that(test2(), equal_to("License"))

    def test_simple_json_file(self):
        """ Reading content of a JSON file; still calling test once. """
        @data(file=os.path.join(os.path.dirname(__file__), "data/simple.json"))
        def test3(values):
            return values[0]["message"]

        assert_that(test3(), equal_to("hello world!"))

    def test_multicall(self):
        """ Testing call of function for each element in list. """
        class Multicall(object):
            def __init__(self):
                self.counter = 0
                self.result = 0

            @data(values=[2, 4, 6, 8, 10], single=True)
            def test4(self, values):
                self.counter += 1
                self.result += values[0]

        instance = Multicall()
        instance.test4()

        assert_that(instance.counter, equal_to(5))
        assert_that(instance.result, equal_to(30))
