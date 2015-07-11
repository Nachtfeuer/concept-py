"""
   Gnuplot script class.

.. module:: plot
    :platform: Unix, Windows
    :synopis: Gnuplot script class.

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
import os


class script(object):

    """
    The scripts represents a whole gnuplot script.

    The main intention is to define the format, the file
    and to run gnuplot to generate the image (like png).
    """

    PNG = 0
    SVG = 1
    JPG = 2
    GIF = 3

    def __init__(self, path_and_filename, plot_obj, width=640, height=480, output_format=PNG):
        """
        Init script and assert parameters.

        :param path_and_filename: location to write script and where also to generate image.
        :param plot_obj: instance of a plot (or a multiplot)
        :param width: width of the final image (default 640)
        :param height: height of the final image (default 480)
        :param output_format: can be one of: script.PNG, script.SVG,
                              script.JPG and script.GIF (for now)
        """
        assert isinstance(path_and_filename, str)
        assert width > 0 and height > 0
        assert output_format in [self.PNG, self.SVG, self.JPG, self.GIF]

        self.path_and_filename = path_and_filename
        self.plot_obj = plot_obj
        self.width = width
        self.height = height
        self.output_format = output_format

    def get_script_header(self):
        """
        The scrip header controls output and format.

        :returns: script header.
        """
        header = "#!/usr/bin/gnuplot"
        format_str = ["png enhanced truecolor", "svg",
                      "jpeg enhanced", "gif enhanced"][self.output_format]
        extension = ["png", "svg", "jpeg", "gif"][self.output_format]
        header += "\nset terminal %s size %d, %d" % (format_str, self.width, self.height)
        header += "\nset output \"%s\"" % (self.path_and_filename + ".%s" % extension)
        return header

    def execute(self):
        """
        Create gnuplot script and execute it.

        It requires that the gnuplot tool is already installed
        and in the search path.
        """
        content = self.get_script_header() + str(self.plot_obj)

        with open(self.path_and_filename, "w") as handle:
            handle.write(content)

        for line in os.popen("gnuplot %s" % self.path_and_filename):
            print("%s" % line)
