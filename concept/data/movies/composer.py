"""
.. module:: composer
    :platform: Unix, Windows
    :synopis: providing one composer of a movie

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
from concept.tools.serialize import Serializable
from concept.tools.decorator import validate_types
from concept.tools.compatible import TextType


class Composer(Serializable):
    """ represents one composer of a movie """

    @validate_types([TextType], offset=1)
    def __init__(self, name=TextType("")):
        """ Initializing from parameters """
        super(Composer, self).__init__()
        self.name = name

    def is_enabled_for_attributes(self):
        """
        :rtype: True for writing the fields as attributes of the tag
        """
        return True

    def __eq__(self, other):
        """
        :param: other: another composer instance (expected)
        :rtype: True if names are identical
        """
        if not isinstance(other, Composer):
            return False

        return self.name == other.name

    def __repr__(self):
        """ readable string representation of an instance of this class """
        return "Composer(name=%(name)s)" % self.__dict__
