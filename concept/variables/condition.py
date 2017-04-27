"""
   Condition classes behaving like variables.

.. module:: condition
    :platform: Unix, Windows
    :synopis: represents conditions behaving like variables

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
from concept.variables.variable import Var


class Condition(Var):
    """Base class for conditions."""

    def __init__(self, value_a, value_b):
        """Initializing with a variable or function (like this class)."""
        if not isinstance(value_a, Var) or not issubclass(value_a.__class__, Var):
            raise TypeError("wrong type")
        if value_b:
            if not isinstance(value_b, Var) or not issubclass(value_b.__class__, Var):
                raise TypeError("wrong type")

        super(Condition, self).__init__((value_a, value_b))

    def get(self):
        """A derived class is required to implement this."""
        raise NotImplementedError

    def set(self, value):
        """You cannot set a value; the value is calculated only."""
        pass

    def __repr__(self):
        """A derived class is required to implement this."""
        raise NotImplementedError


class Equal(Condition):
    """Class that compares two values of the decorated function or variable to be equal."""

    def __init__(self, value_a, value_b):
        """Initializing with a variable or function (like this class)."""
        super(Equal, self).__init__(value_a, value_b)

    def get(self):
        """Return True if equal, otherwise false."""
        return self.value[0].get() == self.value[1].get()

    def __repr__(self):
        """
        String representation of "equal" instance.

        :rtype: string representation of the complete equal condition
        """
        return """Equal(%s, %s)""" % (self.value[0], self.value[1])


class Less(Condition):
    """Class that compares two values of the decorated function or variable to be less (a < b)."""

    def __init__(self, value_a, value_b):
        """Initializing with a variable or function (like this class)."""
        super(Less, self).__init__(value_a, value_b)

    def get(self):
        """Return True if equal, otherwise false."""
        return self.value[0].get() < self.value[1].get()

    def __repr__(self):
        """
        String representation of "less" instance.

        :rtype: string representation of the complete "less" condition
        """
        return """Less(%s, %s)""" % (self.value[0], self.value[1])


class More(Condition):
    """Class that compares two values of the decorated function or variable to be more (a > b)."""

    def __init__(self, value_a, value_b):
        """Initializing with a variable or function (like this class)."""
        super(More, self).__init__(value_a, value_b)

    def get(self):
        """Return True if equal, otherwise false."""
        return self.value[0].get() > self.value[1].get()

    def __repr__(self):
        """
        String representation of "more" instance.

        :rtype: string representation of the complete "more" condition
        """
        return """More(%s, %s)""" % (self.value[0], self.value[1])


class And(Condition):
    """
    Class that compares two values of the decorated function or variable to be both true.

    >>> var1, var2 = Var(True), Var(False)
    >>> condition = And(var1, var2)
    >>> print(condition.get())
    False
    >>> var2.set(True)
    >>> print(condition.get())
    True
    """

    def __init__(self, value_a, value_b):
        """Initializing with a variable or function (like this class)."""
        super(And, self).__init__(value_a, value_b)

    def get(self):
        """Return True if both are True, otherwise false."""
        return self.value[0].get() and self.value[1].get()

    def __repr__(self):
        """
        String representation of "and" instance.

        :rtype: string representation of the complete "and" condition
        """
        return """And(%s, %s)""" % (self.value[0], self.value[1])


class Or(Condition):
    """
    Class that compares two values of the decorated function or variable to be both true.

    >>> var1, var2 = Var(True), Var(False)
    >>> condition = Or(var1, var2)
    >>> print(condition.get())
    True
    >>> var1.set(False)
    >>> print(condition.get())
    False
    """

    def __init__(self, value_a, value_b):
        """Initializing with a variable or function (like this class)."""
        super(Or, self).__init__(value_a, value_b)

    def get(self):
        """Return True if one is True, otherwise false."""
        return self.value[0].get() or self.value[1].get()

    def __repr__(self):
        """
        String representation of "or" instance.

        :rtype: string representation of the complete "or" condition
        """
        return """Or(%s, %s)""" % (self.value[0], self.value[1])


class Not(Condition):
    """
    Class that compares two values of the decorated function or variable to be both true.

    >>> var = Var(True)
    >>> condition = Not(var)
    >>> print(condition.get())
    False
    >>> var.set(False)
    >>> print(condition.get())
    True
    """

    def __init__(self, value):
        """Initializing with a variable or function (like this class)."""
        super(Not, self).__init__(value, None)

    def get(self):
        """Return True if one is True, otherwise false."""
        return not self.value[0].get()

    def __repr__(self):
        """
        String representation of "not" instance.

        :rtype: string representation of the complete "or" condition
        """
        return """Not(%s)""" % self.value[0]
