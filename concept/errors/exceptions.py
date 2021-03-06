"""
   Some custom exceptions.

.. module:: exceptions
    :platform: Unix, Windows
    :synopis: custom exceptions

.. moduleauthor:: Thomas Lehmann <thomas.lehmann.private@googlemail.com>

   =======
   License
   =======
   Copyright (c) 2017 Thomas Lehmann

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


class UnsupportedOperation(RuntimeError):
    """Indicates an operation that is not supported."""

    def __init__(self, message):
        """Initialize exception with a message."""
        super(RuntimeError, self).__init__(message)


class NoLineIntersection(RuntimeError):
    """Indicates intersection between two lines cannot be calculated."""

    def __init__(self, message=""):
        """Initialize exception with a message."""
        super(RuntimeError, self).__init__(message)


class PointIsNotOnTheGivenLine(RuntimeError):
    """Indicates that the point is not on a given line."""

    def __init__(self, message=""):
        """Initialize exception with a message."""
        super(RuntimeError, self).__init__(message)
