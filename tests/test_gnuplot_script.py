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
import unittest
from hamcrest import assert_that, equal_to
from concept.graph.gnuplot.plot import plot
from concept.graph.gnuplot.script import script


class TestGnuplotScript(unittest.TestCase):

    """ Testing of script class. """

    def test_default(self):
        """ Testing script defaults. """
        plot_obj = plot("test")
        instance = script("/tmp/test.pg", plot_obj)
        assert_that(instance.path_and_filename, equal_to("/tmp/test.pg"))
        assert_that(instance.plot_obj, equal_to(plot_obj))
        assert_that(instance.width, equal_to(640))
        assert_that(instance.height, equal_to(480))
        assert_that(instance.output_format, equal_to(script.PNG))

    def test_header(self):
        """ Testing script header. """
        plot_obj = plot("test")
        instance = script("/tmp/test.pg", plot_obj)
        expected_header = """#!/usr/bin/gnuplot
set terminal png enhanced size 640, 480
set output \"/tmp/test.pg.png\""""
        assert_that(instance.get_script_header(), equal_to(expected_header))
