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
from concept.graph.gnuplot.plot import plot
from concept.graph.gnuplot.multiplot import multiplot


class TestGnuplotMultiPlot(unittest.TestCase):

    """ Testing of multiplot class. """

    def test_one_plot(self):
        """ Testing script defaults. """
        plot_obj = plot("one plot")
        multiplot_obj = multiplot("one multiplot")
        multiplot_obj.add_plot(plot_obj)

        script_part_plot = str(plot_obj)
        script_part_all = str(multiplot_obj)
        expected = "\nset multiplot layout 1, 1 title \"one multiplot\""
        assert_that(script_part_all.replace(script_part_plot, ""), equal_to(expected))

    def test_one_plot_with_title_font(self):
        plot_obj = plot("one plot")
        multiplot_obj = multiplot("one multiplot", title_font=("", 20))
        multiplot_obj.add_plot(plot_obj)

        script_part_plot = str(plot_obj)
        script_part_all = str(multiplot_obj)
        expected = "\nset multiplot layout 1, 1 title \"one multiplot\" font \",20\""
        assert_that(script_part_all.replace(script_part_plot, ""), equal_to(expected))
