"""
   Decorator tools.

.. module:: decorator
    :platform: Unix, Windows
    :synopis: decorator tools.

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
import json


class data:

    """
    decorator to provide data to a functor or method.

    The default is to get a parameter with name 'values' of type 'list'
    in your final function or method. For consistency reason this parameter
    will ALWAYS be a list.

    You can change the name using the parameter 'key'.
    Instead of using decorator parameter 'values' you can use 'file' to load
    the content of a file. If the filename ends with .json then it is
    loaded as json file.

    >>> @data(values=[1, 2, 3, 4])
    ... def test1(values): print(values)
    >>> test1()
    [1, 2, 3, 4]
    >>> @data(key='some_data', values=[4, 3, 2, 1])
    ... def test2(some_data): print(some_data)
    >>> test2()
    [4, 3, 2, 1]
    """

    def __init__(self, **kwargs):
        """
        Check the decorator parameters and keep the data for the call of the decorator.

        - valid parameters are 'key', 'file' and 'values'
        - you either can use 'file' OR 'values'
        - A file will be simple read as it is or as JSON if the name ends with '.json'
        """
        for key in kwargs:
            assert key in ['key', 'file', 'values']

        self.key = kwargs['key'] if 'key' in kwargs else "values"
        assert isinstance(self.key, str)
        self.values = kwargs['values'] if 'values' in kwargs else []
        assert isinstance(self.values, list)

        if 'file' in kwargs:
            assert len(self.values) == 0
            if kwargs['file'].endswith(".json"):
                self.values.append(json.loads(open(kwargs['file'], 'r').read()))
            else:
                self.values.append(open(kwargs['file'], 'r').read())

    def __call__(self, function):
        """
        Providing the decorator for the function/method.

        When calling the decorator the defined values will
        be passed to the original function.

        :returns: decorator.
        """
        def decorator(*args):
            arguments = {self.key: self.values}
            return function(*args, **arguments)

        decorator.__name__ = function.__name__
        return decorator
