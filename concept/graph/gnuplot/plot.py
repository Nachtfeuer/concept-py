"""
   Gnuplot plot class.

.. module:: plot
    :platform: Unix, Windows
    :synopis: Gnuplot plot class.

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


class plot(object):

    """ Representing a gnuplot plot. """

    LINES = 0
    FILLEDCURVES = 1

    def __init__(self, title="", title_font=("", 0), use_grid=True):
        """ Init fields. """
        assert isinstance(title, str)
        assert isinstance(title_font, tuple) and len(title_font) == 2
        assert isinstance(title_font[0], str)
        assert isinstance(title_font[1], int)

        self.title = title
        self.title_font = title_font
        self.use_grid = use_grid
        self.curves = []
        self.xlabel = ""
        self.xtics = ""
        self.ylabel = ""
        self.ytics = ""
        self.line_styles = {}
        self.fill_styles = {}

    def set_xlabel(self, label):
        """ Change x label. """
        self.xlabel = label

    def set_ylabel(self, label):
        """ Change x label. """
        self.ylabel = label

    def set_xtics(self, xtics):
        """ Change x tics. """
        assert isinstance(xtics, str)
        self.xtics = xtics

    def set_ytics(self, ytics):
        """ Change y tics. """
        assert isinstance(ytics, str)
        self.ytics = ytics

    def set_line_style(self, style_index, style_description):
        """
        Register line style for index.

        It's expected that the style description for lines is valid.

        :param style_index: that's the non zero based index of the curve.
        :param style_description: gnuplot specific line style description.
        """
        self.line_styles[style_index] = style_description

    def set_fill_style(self, style_index, style_description):
        """
        Register fill style for index.

        It's expected that the fill style description is valid.

        :param style_index: that's the non zero based index of the curve.
        :param style_description: gnuplot specific fill style description.
        """
        self.fill_styles[style_index] = style_description

    def add_curve(self, title, values, mode=LINES):
        """
        Adding one plot curve.

        :param title: title of curve diplayed in legend.
        :param values: table of values (at least two rows expected)
        :param mode: one of: plot.LINES, plot.FILLEDCURVES
        """
        assert isinstance(title, str) and len(title) > 0
        assert isinstance(values, list) and len(values) >= 1
        assert mode in [self.LINES, self.FILLEDCURVES]
        self.curves.append((title, values, mode))

    def get_title_line(self):
        """ Define the main title and its options. """
        line = "\nset title \"%s\"" % self.title
        if self.title_font[1] > 0:
            line += " font "
            if len(self.title_font[0]) > 0:
                line += "\"%s," % self.title_font[0]
            else:
                line += "\","

            line += "%d\"" % self.title_font[1]
        return line

    def __repr__(self):
        """ Generate gnuplot script part for a plot. """
        script = "\n# displaying a plot title"
        script += self.get_title_line()

        if self.use_grid:
            script += "\n# enables displaying a grid"
            script += "\nset grid"

        if self.xlabel and len(self.xlabel) > 0:
            script += "\nset xlabel \"%s\"" % self.xlabel
        if self.ylabel and len(self.ylabel) > 0:
            script += "\nset ylabel \"%s\"" % self.ylabel

        if self.xtics and len(self.xtics) > 0:
            script += "\nset xtics \"%s\"" % self.xtics
        if self.ytics and len(self.ytics) > 0:
            script += "\nset ytics \"%s\"" % self.ytics

        if len(self.curves) > 0:
            for style in range(1, len(self.curves)+1):
                if style in self.line_styles:
                    script += "\nset style line %d %s" % (style, self.line_styles[style])

            script += "\n# plotting values"
            script += "\nplot\\"
            style = 1
            max_style = len(self.curves)
            for title, table, mode in self.curves:
                mode_str = ["lines", "filledcurves x1"][mode]
                fill_style = " fs %s" % self.fill_styles[style] if style in self.fill_styles else ""
                script += "\n    \"-\" with %s ls %d%s title \"%s\"" \
                          % (mode_str, style, fill_style, title)
                if style < max_style:
                    script += ",\\"
                style += 1

            for title, table, mode in self.curves:
                for row in table:
                    script += "\n" + " ".join([str(value) for value in row])
                script += "\nEOF"

        return script + "\n"
