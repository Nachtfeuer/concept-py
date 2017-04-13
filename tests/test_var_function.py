"""
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
import unittest
import math
from concept.variables.variable import Var
from concept.variables.function import Function, Square, Sqrt, Sin
from concept.tools.decorator import validate_test_responsibility_for


@validate_test_responsibility_for(Square, True)
@validate_test_responsibility_for(Sqrt, True)
@validate_test_responsibility_for(Sin, True)
class TestFunction(unittest.TestCase):
    """ testing of class pydemo.movies.math.object.function classes """

    def test_function_init(self):
        """ testing Square.__init__ """
        function = Function(Var(10))
        self.assertEqual(10, function.value.value)
        # wrong type
        self.assertRaises(TypeError, Function, 1234)

    def test_square_init(self):
        """ testing Square.__init__ """
        square = Square(Var(10))
        self.assertEqual(10, square.value.value)
        # wrong type
        self.assertRaises(TypeError, Square, 1234)

    def test_square_get(self):
        """ testing Square.get """
        square = Square(Var(10))
        self.assertEqual(100, square.get())

        var = Var(2)
        square = Square(Square(var))
        self.assertEqual(16, square.get())
        var.set(3)
        self.assertEqual(81, square.get())

    def test_square_repr(self):
        """ testing Square.__repr__ """
        function = Square(Var(10))
        expected = "Square(Var(10))"
        self.assertEqual(expected, str(function))

    def test_sqrt_init(self):
        """ testing Sqrt.__init__ """
        function = Sqrt(Var(9))
        self.assertEqual(9, function.value.value)
        # wrong type
        self.assertRaises(TypeError, Sqrt, 1234)

    def test_sqrt_get(self):
        """ testing Sqrt.get """
        function = Sqrt(Var(9))
        self.assertEqual(3, function.get())

        var = Var(81)
        function = Sqrt(Sqrt(var))
        self.assertEqual(3, function.get())
        var.set(256)
        self.assertEqual(4, function.get())

    def test_sqrt_repr(self):
        """ testing Sqrt.__repr__ """
        function = Sqrt(Var(9))
        expected = "Sqrt(Var(9))"
        self.assertEqual(expected, str(function))

    def test_sin_init(self):
        """ testing Sin.__init__ """
        sinus = Sin(Var(45))
        self.assertEqual(45, sinus.value.value)
        # wrong type
        self.assertRaises(TypeError, Sin.__init__, 1234)

    def test_sin_get(self):
        """ testing Sin.get """
        # sin(90) == 1
        sinus = Sin(Var(math.radians(90)))
        self.assertEqual(1.0, sinus.get())

        # sin(0) == 0
        var = Var(math.radians(0.0))
        sinus = Sin(var)
        self.assertEqual(math.radians(0.0), sinus.get())
        # sin(pi) == 0
        var.set(math.pi)
        self.assertTrue(sinus.get() < 1e-15)

    def test_sin_repr(self):
        """ testing Sin.__repr__ """
        sinus = Sin(Var(math.radians(90)))
        expected = "Sin(Var(%s))" % math.radians(90)
        self.assertEqual(expected, str(sinus))
