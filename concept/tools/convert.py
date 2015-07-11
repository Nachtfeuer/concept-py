"""
   Conversion functions.

.. module:: convert
    :platform: Unix, Windows
    :synopis: conversion functions.

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


def dict2list(obj):
    """
    Converting a dictionary into a list of pairs.

    >>> dict2list({"first-name": "Agatha", "surname": "Christie"})
    [('first-name', 'Agatha'), ('surname', 'Christie')]
    """
    assert isinstance(obj, dict)
    return [(key, value) for key, value in sorted(obj.items())]


def list2dict(obj):
    """
    Converting a list of pairs into a dictionary.

    >>> data = list2dict([("first-name", "Agatha"), ("surname", "Christie")])
    >>> data['first-name']
    'Agatha'
    >>> data['surname']
    'Christie'
    """
    assert isinstance(obj, list) and all([(isinstance(entry, tuple) or isinstance(entry, list))
                                          and len(entry) == 2 for entry in obj])
    return dict(obj)
