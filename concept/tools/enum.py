"""
.. module:: enum
    :platform: Unix, Windows
    :synopis: simple enum mechanism providing readonly enum type

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


def enum(names):
    """ provides a readonly type with constants and
        automatically assigned values like an enum in C++

        >>> POLICIES = enum("PICKLE XML")
        >>> print(POLICIES)
        enum(PICKLE=0, XML=1)
        >>> POLICIES.PICKLE
        0
        >>> POLICIES.XML
        1
    """
    names = names.replace(',', ' ').upper().split()
    space = dict(map(reversed, enumerate(names)), __slots__=())
    # adding __repr__ method to new type
    space['__repr__'] = lambda self: "enum(%s)" % ", " \
        .join(["%s=%d" % (name, space[name]) for name in names])
    space['__iter__'] = lambda self: iter(names)
    space['__getitem__'] = lambda self, key: space[key]
    return type('enum', (object,), space)()
