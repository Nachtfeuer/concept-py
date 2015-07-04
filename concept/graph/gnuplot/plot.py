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
        self.ylabel = ""
        self.styles = {}

    def set_xlabel(self, label):
        """ Change x label. """
        self.xlabel = label

    def set_ylabel(self, label):
        """ Change x label. """
        self.ylabel = label

    def set_style(self, style_index, style_description):
        """
        Register style for index.

        It's expected that the style description for lines
        is valid.

        :param style_index: that's the non zero based index of the curve.
        :param style_description: gnuplot specific style description.
        """
        self.styles[style_index] = style_description

    def add_curve(self, title, values):
        """
        Adding one plot curve.

        :param title: title of curve diplayed in legend.
        :param values: table of values (at least two rows expected)
        """
        assert isinstance(title, str) and len(title) > 0
        assert isinstance(values, list) and len(values) >= 2
        self.curves.append((title, values))

    def __repr__(self):
        """ Generate gnuplot script part for a plot. """
        script = "\n# displaying a plot title"
        script += "\nset title \"%s\"" % self.title
        if self.title_font[1] > 0:
            script += " font "
            if len(self.title_font) > 0:
                script += "\"%s," % self.title_font[0]
            else:
                script += "\","

            script += "%d\"" % self.title_font[1]

        if self.use_grid:
            script += "\n# enables displaying a grid"
            script += "\nset grid"

        if self.xlabel and len(self.xlabel) > 0:
            script += "\nset xlabel \"%s\"" % self.xlabel
        if self.ylabel and len(self.ylabel) > 0:
            script += "\nset ylabel \"%s\"" % self.ylabel

        if len(self.curves) > 0:
            for ls in range(1, len(self.curves)+1):
                if ls in self.styles:
                    script += "\nset style line %d %s" % (ls, self.styles[ls])

            script += "\n# plotting values"
            script += "\nplot\\"
            ls = 1
            max_ls = len(self.curves)
            for title, table in self.curves:
                script += "\n    \"-\" with lines ls %d title \"%s\"" % (ls, title)
                if ls < max_ls:
                    script += ",\\"
                ls += 1

            for title, table in self.curves:
                for row in table:
                    script += "\n" + " ".join([str(value) for value in row])
                script += "\nEOF"

        return script + "\n"
