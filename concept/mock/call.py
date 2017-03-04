"""
   Represents a call.

.. module:: call
    :platform: Unix, Windows
    :synopis: represents a call

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
from concept.tools.compatible import compare


class Call(object):
    """Represents a method call (history data)."""

    def __init__(self, name, *args, **kwargs):
        """ Store a call. """
        self.name = name
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        """String representation of this class."""
        call = "Call(" + self.name

        if len(self.args) > 0 or len(self.kwargs) > 0:
            call += ", "

        if len(self.args) > 0:
            call += ", ".join([str(entry) for entry in self.args])

        if len(self.kwargs) > 0:
            if len(self.args) > 0:
                call += ", "
            call += ", ".join(["%s=%s" % (key, self.kwargs[key]) for key in sorted(self.kwargs)])

        return call + ")"

    def __hash__(self):
        """ hash code for call required for hash containers. """
        return hash((self.name, self.args, frozenset(self.kwargs.items())))

    def __eq__(self, other):
        """ testing two calls to be equal. """
        if not isinstance(other, Call):
            return False
        if not self.name == other.name:
            return False
        if not len(self.args) == len(other.args):
            return False
        for entry, other_entry in zip(self.args, other.args):
            if not entry == other_entry:
                return False
        return True

    def __cmp__(self, other):
        """ comparing two instances. """
        if not isinstance(other, Call):
            return compare(str(self), str(other))

        diff = compare(self.name, other.name)
        if not diff == 0:
            return diff

        diff = len(self.args) - len(other.args)
        if not diff == 0:
            return diff

        for entry, other_entry in zip(self.args, other.args):
            diff = compare(entry, other_entry)
            if not diff == 0:
                return diff

        return 0
