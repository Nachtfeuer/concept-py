"""
   Gnuplot multiplot class.

.. module:: plot
    :platform: Unix, Windows
    :synopis: Gnuplot multiplot class.

.. moduleauthor:: Thomas Lehmann <thomas.lehmann.private@googlemail.com>

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
from concept.graph.gnuplot.plot import plot


class multiplot(object):

    """
    Wrapper for gnuplot multiplot environment.

    gnuplot docs (entry point): http://www.gnuplot.info/ (documentation as PDF only)
    Example: http://gnuplot.sourceforge.net/demo/layout.html
    """

    def __init__(self, title, title_font=("", 0), plots_per_row=2):
        """ Initialize a multiplot object. """
        assert isinstance(title, str) and len(title) > 0
        assert isinstance(title_font, tuple) and len(title_font) == 2
        assert isinstance(title_font[0], str)
        assert isinstance(title_font[1], int)
        assert isinstance(plots_per_row, int) and plots_per_row > 0
        self.title = title
        self.title_font = title_font
        self.plots_per_row = plots_per_row
        self.plot_objects = []

    def add_plot(self, plot_obj):
        """ Adding a plot object. """
        assert isinstance(plot_obj, plot)
        self.plot_objects.append(plot_obj)

    def get_title_code(self):
        """ Gnuplot script part for title and font. """
        code = "title \"%s\"" % self.title
        if self.title_font[1] > 0:
            code += " font "
            if len(self.title_font[0]) > 0:
                code += "\"%s," % self.title_font[0]
            else:
                code += "\","

            code += "%d\"" % self.title_font[1]
        return code

    def __repr__(self):
        """ Provide gnuplot script for multiplot. """
        cols = min(self.plots_per_row, len(self.plot_objects))
        rows = len(self.plot_objects) // cols
        content = "\nset multiplot layout %d, %d %s" % (rows, cols, self.get_title_code())
        content += "\n".join([str(plot_obj) for plot_obj in self.plot_objects])
        return content
