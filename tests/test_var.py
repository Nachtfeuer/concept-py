"""
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
import unittest
from concept.variables.variable import Var
from concept.tools.decorator import validate_test_responsibility_for


@validate_test_responsibility_for(Var)
class TestVar(unittest.TestCase):
    """ testing of class pydemo.movies.math.object.variable.Var class """

    def test_init(self):
        """ testing of Var.__init__ """
        var = Var()
        self.assertEqual(None, var.value)
        var = Var(1234)
        self.assertEqual(1234, var.value)

    def test_set(self):
        """ testing of Var.set """
        var = Var()
        var.set(1234)
        self.assertEqual(1234, var.value)

    def test_get(self):
        """ testing of Var.get """
        var = Var(1234)
        self.assertEqual(1234, var.get())

    def test_equal(self):
        """ testing of Var.__eq__ """
        var1 = Var(1234)
        var2 = Var(5678)
        var3 = Var(1234)

        self.assertTrue(var1 == var3)
        self.assertFalse(var1 == var2)
        # testing comparison of two different types (not allowed)
        self.assertFalse(var1 == 10)

    def test_repr(self):
        """ testing of Var.__repr__ """
        var = Var(1234)
        self.assertEqual("Var(1234)", str(var))

    def test_is_enabled_for_attributes(self):
        """testing of Var.is_enabled_for_attributes method."""
        var = Var()
        self.assertEqual(True, var.is_enabled_for_attributes())

    def test_get_serializable_name(self):
        """testing of Var.get_serializable_name method."""
        var = Var()
        self.assertEqual("var", var.get_serializable_name())

    def test_get_serializable_field(self):
        """testing of Var.get_serializable_name method."""
        var = Var()
        fields = ["value"]
        self.assertEqual(fields, var.get_serializable_fields())

    def test_to_xml(self):
        """ testing of Var.to_xml method (base class) """
        var = Var(1234)
        expected = """<var value="1234"/>"""
        self.assertEqual(expected, var.to_xml())
