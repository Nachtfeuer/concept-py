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
import inspect


class data(object):

    """
    decorator to provide data to a functor or method.

    The default is to get a parameter with name 'values' of type 'list'
    in your final function or method. For consistency reason this parameter
    will ALWAYS be a list.

    You can change the name using the parameter 'key'.
    Instead of using decorator parameter 'values' you can use 'file' to load
    the content of a file. If the filename ends with .json then it is
    loaded as json file.

    With parameter single you can run test decorated method as many entries
    are contained in the list.

    >>> @data(values=[1, 2, 3, 4])
    ... def test1(values): print(values)
    >>> test1()
    [1, 2, 3, 4]
    >>> @data(key='some_data', values=[4, 3, 2, 1])
    ... def test2(some_data): print(some_data)
    >>> test2()
    [4, 3, 2, 1]
    >>> @data(key='some_data', values=[2, 1], single=True)
    ... def test3(some_data): print(some_data)
    >>> test3()
    [2]
    [1]
    """

    def __init__(self, **kwargs):
        """
        Check the decorator parameters and keep the data for the call of the decorator.

        - valid parameters are 'key', 'file' and 'values'
        - you either can use 'file' OR 'values'
        - A file will be simple read as it is or as JSON if the name ends with '.json'
        """
        for key in kwargs:
            assert key in ['key', 'file', 'values', 'single']

        self.key = str(kwargs['key']) if 'key' in kwargs else "values"
        assert isinstance(self.key, str)
        self.values = kwargs['values'] if 'values' in kwargs else []
        assert isinstance(self.values, list)
        self.single = bool(kwargs['single']) if 'single' in kwargs else False

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
            """ decorator function. """
            if self.single:
                for value in self.values:
                    arguments = {self.key: [value]}
                    function(*args, **arguments)
            else:
                arguments = {self.key: self.values}
                return function(*args, **arguments)

        decorator.__name__ = function.__name__
        decorator.__doc__ = function.__doc__
        return decorator


class validate_test_responsibility_for(object):

    """
    Decorator to ensure to test all methods for a given class.

    a class decorator that throws an exception when the test class does not
    implement all tests for all methods of the testable class (unit).
    The next code gives you an example on how it is used and what does happen:

    >>> class Value:
    ...     def __init__(self, value):
    ...         self.value = value
    ...
    >>> try:
    ...     import unittest
    ...     @validate_test_responsibility_for(Value)
    ...     class TestValue(unittest.TestCase):
    ...         pass
    ... except Exception as e:
    ...     print("|%s|" % str(e).strip())
    |...failed to provide test method 'TestValue.test_init' for method 'Value.__init__'|
    """

    def __init__(self, testable_class, include_class_name=False):
        """ store the class for test and checks all methods of that class. """
        if hasattr(testable_class, "decorated_object"):
            testable_class = testable_class.decorated_object

        self.testable_class = testable_class
        self.include_class_name = include_class_name
        self.methods_in_testable_class\
            = self.get_entries(self.testable_class, inspect.isfunction)\
            + self.get_entries(self.testable_class, inspect.ismethod)

    @staticmethod
    def get_entries(the_class, mode):
        """
        Query functions and method of a given class.

        get all entries by given mode (function or method) but the
        members of the concrete class only; not from its base
        """
        classes = {}
        for concrete_class in reversed(inspect.getmro(the_class)):
            classes[concrete_class] = {}
            for name, definition in dict(inspect.getmembers(concrete_class, mode)).items():
                if name.find("subclass") >= 0:
                    continue

                object_name = name
                is_base_method_only = False

                for known_class in classes:
                    if object_name not in classes[known_class]:
                        continue

                    if classes[known_class][object_name] == definition:
                        is_base_method_only = True
                        break

                if not is_base_method_only:
                    classes[concrete_class][object_name] = definition

        return list(classes[the_class].keys())

    def __call__(self, test_class):
        """ called when instantiated; then we have to verify for the required test methods. """
        self.verify(test_class)
        return test_class

    @staticmethod
    def get_test_method(name, prefix=""):
        """ adjusting final test method name. """
        # no underscores wanted (change "__init__" => "init")
        final_name = name.strip("_").lower()

        # ensure more readable name (like "equal" instead of "eq")
        if name == "__eq__":
            final_name = "equal"
        elif name == "__lt__":
            final_name = "less"
        elif name == "__gt__":
            final_name = "greater"

        return "test_" + prefix.lower() + final_name

    def verify(self, test_class):
        """ verification that for each testable method a test method does exist. """
        methods_in_test_class\
            = self.get_entries(test_class, inspect.isfunction)\
            + self.get_entries(test_class, inspect.ismethod)

        missing = []
        for testable_method in self.methods_in_testable_class:
            prefix = ""
            if self.include_class_name:
                prefix = self.testable_class.__name__ + "_"

            test_method = self.get_test_method(testable_method, prefix)
            if test_method in methods_in_test_class:
                continue

            missing.append((test_class.__name__ + "." + test_method,
                            self.testable_class.__name__ + "." + testable_method))

        if len(missing) > 0:
            # creates message with all missing methods throwing an exception for it
            message = ""
            for test_method, testable_method in missing:
                message += "\n...failed to provide test method '%s' for method '%s'" \
                           % (test_method, testable_method)
            raise Exception(message)


def singleton(the_class):
    """ decorator for a class to make a singleton out of it. """
    class_instances = {}

    def get_instance(*args, **kwargs):
        """
        creating or just return the one and only class instance.

        The singleton depends on the parameters used in __init__
        """
        key = (the_class, args, str(kwargs))
        if key not in class_instances:
            class_instances[key] = the_class(*args, **kwargs)
        return class_instances[key]

    return get_instance
