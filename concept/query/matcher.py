"""
   Matching text.

.. module:: matcher
    :platform: Unix, Windows
    :synopis: matching text.

.. moduleauthor:: Thomas Lehmann <thomas.lehmann.private@googlemail.com>


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
import re


class Matcher(object):
    """Basic functionality for matching some text."""

    def __init__(self, text):
        """Initialize with text."""
        self.original_text = text
        self.text = text

    def left_of(self, regex_expression):
        """
        Use current text to find all text left of expression or simple text.

        >>> matcher = Matcher("left_and_right")
        >>> matcher.left_of("_and_right").text
        'left'
        >>> matcher = Matcher("xxxx123hello world")
        >>> matcher.right_of("[0-9]+").text
        'hello world'

        :param regex_expression: regular expressions or just simple text.
        :return: matcher itself for further processing.

        .. note:: when found the current text is changed to result.
        """
        match = re.search(regex_expression, self.text)
        if match:
            self.text = self.text[0: match.start()]

        return self

    def right_of(self, regex_expression):
        """
        Use current text to find all text right of expression or simple text.

        >>> matcher = Matcher("left_and_right")
        >>> matcher.right_of("left_and_").text
        'right'
        >>> matcher = Matcher("hello world123xxx")
        >>> matcher.left_of("[0-9]+").text
        'hello world'

        :param regex_expression: regular expressions or just simple text.
        :return: matcher itself for further processing.

        .. note:: when found the current text is changed to result.
        """
        match = re.search(regex_expression, self.text)
        if match:
            self.text = self.text[match.end():]
        return self

    def replace(self, regex_expression, repl):
        r"""
        Replace parts of a the text.

        >>> matcher = Matcher('abc\nxyz\n123')
        >>> matcher.replace('\n', "|").text
        'abc|xyz|123'
        >>> matcher.replace('[0-9]+', "foo").text
        'abc|xyz|foo'

        :param regex_expression: regular expressions or just simple text.
        :param repl: string for replace or a function (see re.sub)
        :return: matcher itself for further processing.

        .. note:: when found the current text is changed to result.
        """
        self.text = re.sub(regex_expression, repl, self.text)
        return self

    def find_all(self, regex_expression):
        """
        Use current text to find all occurrences.

        >>> matcher = Matcher("left_and_123 456 789_and_right")
        >>> matcher.find_all("[0-9]+")
        ['123', '456', '789']

        :param regex_expression: regular expressions or just simple text.
        :return: list of found sub strings. Can be empty if nothing has been found.

        .. note::
          * It dies not modify the content of the matcher.
          * It's a final method; you cannot call further matcher functions on the result.
        """
        return [self.text[match.start(): match.end()]
                for match in re.finditer(regex_expression, self.text)]
