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
from concept.graph.gnuplot.plot import plot
from concept.tools.decorator import data


class TestGnuplotPlot(unittest.TestCase):

    """ Testing of plot class. """

    def test_default(self):
        """ Testing plot. """
        obj = plot()
        assert_that(obj.title, equal_to(""))
        assert_that(obj.use_grid, equal_to(True))
        assert_that(obj.curves, equal_to([]))
        assert_that(obj.line_styles, equal_to({}))
        assert_that(obj.fill_styles, equal_to({}))
        assert_that(obj.xlabel, equal_to(""))
        assert_that(obj.ylabel, equal_to(""))
        assert_that(obj.xtics, equal_to(""))
        assert_that(obj.ytics, equal_to(""))

    def test_get_title_line(self):
        """ Testing plot.get_title_line method. """
        obj = plot("test plot")
        expected = "\nset title \"test plot\""
        assert_that(obj.get_title_line(), equal_to(expected))

    @data(key="content", file=os.path.join(os.path.dirname(__file__), "data/title_and_grid.gp"))
    def test_repr(self, content):
        """ Testing plot.__repr__ method. """
        obj = plot("test plot")
        assert_that(str(obj), equal_to(content[0]))

    @data(key="content", file=os.path.join(os.path.dirname(__file__), "data/title_and_font.gp"))
    def test_title_and_font(self, content):
        """ Testing plot.__init__ method with font name and size.. """
        obj = plot("test plot", title_font=("Helvetica", 20), use_grid=False)
        assert_that(str(obj), equal_to(content[0]))

    @data(key="content",
          file=os.path.join(os.path.dirname(__file__), "data/title_and_font_size_only.gp"))
    def test_title_and_font_size_only(self, content):
        """ Testing plot.__init__ method with font size only. """
        obj = plot("test plot", title_font=("", 20), use_grid=False)
        assert_that(str(obj), equal_to(content[0]))

    @data(key="content", file=os.path.join(os.path.dirname(__file__), "data/xlabel.gp"))
    def test_xlabel(self, content):
        """ Testing plot.set_xlabel method. """
        obj = plot("test plot", use_grid=False)
        obj.set_xlabel("the x-values")
        assert_that(str(obj), equal_to(content[0]))

    @data(key="content", file=os.path.join(os.path.dirname(__file__), "data/xtics.gp"))
    def test_xtics(self, content):
        """ Testing plot.set_xtics method. """
        obj = plot("test plot", use_grid=False)
        obj.set_xtics("1")
        assert_that(str(obj), equal_to(content[0]))

    @data(key="content", file=os.path.join(os.path.dirname(__file__), "data/ylabel.gp"))
    def test_ylabel(self, content):
        """ Testing plot.set_ylabel method. """
        obj = plot("test plot", use_grid=False)
        obj.set_ylabel("the y-values")
        assert_that(str(obj), equal_to(content[0]))

    @data(key="content", file=os.path.join(os.path.dirname(__file__), "data/ytics.gp"))
    def test_ytics(self, content):
        """ Testing plot.set_ytics method. """
        obj = plot("test plot", use_grid=False)
        obj.set_ytics("0.5")
        assert_that(str(obj), equal_to(content[0]))

    @data(key="content", file=os.path.join(os.path.dirname(__file__), "data/one_curve.gp"))
    def test_repr_with_one_curve(self, content):
        """ Testing plot.add_curve method one time. """
        obj = plot("test plot")
        obj.add_curve("some data", [[1, 1], [2, 0], [3, 1]])
        assert_that(str(obj), equal_to(content[0]))

    @data(key="content", file=os.path.join(os.path.dirname(__file__), "data/two_curves.gp"))
    def test_repr_with_two_curves(self, content):
        """ Testing plot.add_curve method two times. """
        obj = plot("test plot")
        obj.add_curve("some data", [[1, 1], [2, 0], [3, 1]])
        obj.add_curve("some other data", [[1, 0], [2, 1], [3, 0]])
        assert_that(str(obj), equal_to(content[0]))

    @data(key="content",
          file=os.path.join(os.path.dirname(__file__), "data/one_curve_with_line_style.gp"))
    def test_repr_with_line_styles(self, content):
        """ Testing plot.__repr__ method. """
        obj = plot("test plot")
        obj.add_curve("some data", [[1, 1], [2, 0], [3, 1]])
        obj.set_line_style(1, "lc rgb \"#00ff00\" lw 2")
        assert_that(str(obj), equal_to(content[0]))

    @data(key="content",
          file=os.path.join(os.path.dirname(__file__), "data/one_curve_with_fill_style.gp"))
    def test_repr_with_fill_style(self, content):
        """ Testing plot.set_fill_style method one time. """
        obj = plot("test plot")
        obj.set_fill_style(1, "transparent solid 0.5 border")
        obj.add_curve("some data", [[1, 1], [2, 0], [3, 1]], mode=plot.FILLEDCURVES)
        assert_that(str(obj), equal_to(content[0]))
