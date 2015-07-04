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


class TestGnuplotPlot(unittest.TestCase):

    """ Testing of plot class. """

    def test_default(self):
        """ Testing plot. """
        obj = plot()
        assert_that(obj.title, equal_to(""))
        assert_that(obj.use_grid, equal_to(True))
        assert_that(obj.curves, equal_to([]))
        assert_that(obj.styles, equal_to({}))

    def test_repr(self):
        """ Testing plot.__repr__ method. """
        obj = plot("test plot")
        expected_script = """
# displaying a plot title
set title "test plot"
# enables displaying a grid
set grid
"""
        assert_that(str(obj), equal_to(expected_script))

    def test_title_and_font(self):
        """ Testing plot.__repr__ method. """
        obj = plot("test plot", title_font=("Helvetica", 20), use_grid=False)
        expected_script = """
# displaying a plot title
set title "test plot" font "Helvetica,20"
"""
        assert_that(str(obj), equal_to(expected_script))

    def test_xlabel(self):
        """ Testing plot.__repr__ method. """
        obj = plot("test plot", use_grid=False)
        obj.set_xlabel("the x-values")
        expected_script = """
# displaying a plot title
set title "test plot"
set xlabel "the x-values"
"""
        assert_that(str(obj), equal_to(expected_script))

    def test_ylabel(self):
        """ Testing plot.__repr__ method. """
        obj = plot("test plot", use_grid=False)
        obj.set_ylabel("the y-values")
        expected_script = """
# displaying a plot title
set title "test plot"
set ylabel "the y-values"
"""
        assert_that(str(obj), equal_to(expected_script))

    def test_repr_with_one_curve(self):
        """ Testing plot.__repr__ method. """
        obj = plot("test plot")
        obj.add_curve("some data", [[1, 1], [2, 0], [3, 1]])
        expected_script = """
# displaying a plot title
set title "test plot"
# enables displaying a grid
set grid
# plotting values
plot\\
    "-" with lines ls 1 title "some data"
1 1
2 0
3 1
EOF
"""
        assert_that(str(obj), equal_to(expected_script))

    def test_repr_with_two_curves(self):
        """ Testing plot.__repr__ method. """
        obj = plot("test plot")
        obj.add_curve("some data", [[1, 1], [2, 0], [3, 1]])
        obj.add_curve("some other data", [[1, 0], [2, 1], [3, 0]])
        expected_script = """
# displaying a plot title
set title "test plot"
# enables displaying a grid
set grid
# plotting values
plot\\
    "-" with lines ls 1 title "some data",\\
    "-" with lines ls 2 title "some other data"
1 1
2 0
3 1
EOF
1 0
2 1
3 0
EOF
"""
        assert_that(str(obj), equal_to(expected_script))

    def test_repr_with_styles(self):
        """ Testing plot.__repr__ method. """
        obj = plot("test plot")
        obj.add_curve("some data", [[1, 1], [2, 0], [3, 1]])
        obj.set_style(1, "lc rgb \"#00ff00\" lw 2")
        expected_script = """
# displaying a plot title
set title "test plot"
# enables displaying a grid
set grid
set style line 1 lc rgb "#00ff00" lw 2
# plotting values
plot\\
    "-" with lines ls 1 title "some data"
1 1
2 0
3 1
EOF
"""
        assert_that(str(obj), equal_to(expected_script))
