"""
   Director of a movie.

.. module:: director
    :platform: Unix, Windows
    :synopis: providing one director of a movie

.. moduleauthor:: Thomas Lehmann <thomas.lehmann.private@googlemail.com>

   =======
   License
   =======
   Copyright (c) 2014 Thomas Lehmann

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
from concept.tools.serialize import Serializable
from concept.tools.decorator import validate_types
from concept.tools.compatible import TextType


class Director(Serializable):
    """Represents one director of a movie."""

    @validate_types([TextType], offset=1)
    def __init__(self, name=TextType("")):
        """Initializing from parameters."""
        super(Director, self).__init__()
        self.name = name

    def is_enabled_for_attributes(self):
        """
        Adjusted to true for writing fields as XML attributes.

        :rtype: True for writing the fields as attributes of the tag
        """
        return True

    def __eq__(self, other):
        """
        Comparing this object to be equal with another in type and data.

        :param: other: another director instance (expected)
        :rtype: True if names are identical
        """
        if not isinstance(other, Director):
            return False

        return self.name == other.name

    def __repr__(self):
        """Readable string representation of an instance of this classr."""
        return "Director(name=%(name)s)" % self.__dict__
