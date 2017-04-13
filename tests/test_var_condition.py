"""
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
import unittest
from concept.variables.variable import Var
from concept.variables.condition import Condition, Equal, Less, More, And, Or, Not
from concept.tools.decorator import validate_test_responsibility_for


@validate_test_responsibility_for(Condition, True)
@validate_test_responsibility_for(Equal, True)
@validate_test_responsibility_for(Less, True)
@validate_test_responsibility_for(More, True)
@validate_test_responsibility_for(And, True)
@validate_test_responsibility_for(Or, True)
@validate_test_responsibility_for(Not, True)
class TestFunction(unittest.TestCase):
    """testing of class concept.variables.condition classes."""

    def test_condition_init(self):
        """testing Condition.__init__."""
        condition = Condition(Var(10), Var(11))
        self.assertEqual(10, condition.value[0].value)
        self.assertEqual(11, condition.value[1].value)

        self.assertRaises(TypeError, Condition, Var(10), 10)
        self.assertRaises(TypeError, Condition, 10, Var(10))
        self.assertRaises(TypeError, Condition, 10, 10)

    def test_condition_set(self):
        """ testing Condition.set (should not do anything) """
        condition = Condition(Var(10), Var(11))

        condition.set(None)
        self.assertEqual(10, condition.value[0].value)
        self.assertEqual(11, condition.value[1].value)

        condition.set((Var(10), Var(11)))
        self.assertEqual(10, condition.value[0].value)
        self.assertEqual(11, condition.value[1].value)

    def test_condition_get(self):
        """ testing Condition.get """
        condition = Condition(Var(10), Var(11))
        self.assertRaises(NotImplementedError, condition.get)

    def test_condition_repr(self):
        """ testing Condition.__repr__ """
        condition = Condition(Var(10), Var(11))
        self.assertRaises(NotImplementedError, condition.__repr__)

    def test_equal_init(self):
        """ testing Equal.__init__ """
        condition = Equal(Var(10), Var(11))
        self.assertEqual(10, condition.value[0].value)
        self.assertEqual(11, condition.value[1].value)

        self.assertRaises(TypeError, Equal, Var(10), 10)
        self.assertRaises(TypeError, Equal, 10, Var(10))
        self.assertRaises(TypeError, Equal, 10, 10)

    def test_equal_get(self):
        """ testing Equal.get """
        self.assertEqual(True, Equal(Var(10), Var(10)).get())
        self.assertEqual(False, Equal(Var(10), Var(11)).get())

        var1, var2 = Var(10), Var(10)
        condition = Equal(var1, var2)
        self.assertEqual(True, condition.get())
        var1.set(var1.get() + 1)
        self.assertEqual(False, condition.get())
        var2.set(var2.get() + 1)
        self.assertEqual(True, condition.get())

    def test_equal_repr(self):
        """ testing Equal.__repr__ """
        condition = Equal(Var(1), Var(3))
        expected = """Equal(Var(1), Var(3))"""
        self.assertEqual(expected, str(condition))

    def test_less_init(self):
        """ testing Less.__init__ """
        condition = Less(Var(10), Var(11))
        self.assertEqual(10, condition.value[0].value)
        self.assertEqual(11, condition.value[1].value)

        self.assertRaises(TypeError, Less, Var(10), 10)
        self.assertRaises(TypeError, Less, 10, Var(10))
        self.assertRaises(TypeError, Less, 10, 10)

    def test_less_get(self):
        """ testing Less.get """
        self.assertEqual(True, Less(Var(10), Var(11)).get())
        self.assertEqual(False, Less(Var(10), Var(10)).get())

        var1, var2 = Var(10), Var(11)
        condition = Less(var1, var2)
        self.assertEqual(True, condition.get())
        var1.set(var1.get() + 1)
        self.assertEqual(False, condition.get())
        var2.set(var2.get() + 1)
        self.assertEqual(True, condition.get())

    def test_less_repr(self):
        """ testing Less.__repr__ """
        condition = Less(Var(1), Var(3))
        expected = """Less(Var(1), Var(3))"""
        self.assertEqual(expected, str(condition))

    def test_more_init(self):
        """ testing More.__init__ """
        condition = More(Var(11), Var(10))
        self.assertEqual(11, condition.value[0].value)
        self.assertEqual(10, condition.value[1].value)

        self.assertRaises(TypeError, Less, Var(11), 10)
        self.assertRaises(TypeError, Less, 11, Var(10))
        self.assertRaises(TypeError, Less, 11, 10)

    def test_more_get(self):
        """ testing More.get """
        self.assertEqual(True, More(Var(11), Var(10)).get())
        self.assertEqual(False, More(Var(10), Var(10)).get())

        var1, var2 = Var(11), Var(10)
        condition = More(var1, var2)
        self.assertEqual(True, condition.get())
        var2.set(var2.get() + 1)
        self.assertEqual(False, condition.get())
        var1.set(var1.get() + 1)
        self.assertEqual(True, condition.get())

    def test_more_repr(self):
        """ testing More.__repr__ """
        condition = More(Var(1), Var(3))
        expected = """More(Var(1), Var(3))"""
        self.assertEqual(expected, str(condition))

    def test_and_init(self):
        """ testing And.__init__ """
        condition = And(Equal(Var(1), Var(1)), Equal(Var(2), Var(2)))
        self.assertEqual(1, condition.value[0].value[0].value)
        self.assertEqual(1, condition.value[0].value[1].value)
        self.assertEqual(2, condition.value[1].value[0].value)
        self.assertEqual(2, condition.value[1].value[1].value)

        self.assertRaises(TypeError, And, Var(11), 10)
        self.assertRaises(TypeError, And, 11, Var(10))
        self.assertRaises(TypeError, And, 11, 10)

    def test_and_get(self):
        """ testing And.get """
        self.assertEqual(True, And(Less(Var(10), Var(11)), More(Var(11), Var(10))).get())
        self.assertEqual(False, And(Less(Var(10), Var(10)), More(Var(11), Var(10))).get())
        self.assertEqual(False, And(Less(Var(10), Var(11)), More(Var(10), Var(10))).get())

        var1, var2, var3, var4 = Var(11), Var(10), Var(9), Var(8)
        conditionA, conditionB = More(var1, var2), Less(var4, var3)
        condition = Equal(conditionA, conditionB)
        self.assertEqual(True, condition.get())
        var2.set(var2.get() + 1)
        self.assertEqual(False, condition.get())
        var1.set(var1.get() + 1)
        self.assertEqual(True, condition.get())
        var4.set(var4.get() + 1)
        self.assertEqual(False, condition.get())
        var3.set(var3.get() + 1)
        self.assertEqual(True, condition.get())

    def test_and_repr(self):
        """ testing And.__repr__ """
        condition = And(Var(1), Var(3))
        expected = """And(Var(1), Var(3))"""
        self.assertEqual(expected, str(condition))

    def test_or_init(self):
        """ testing Or.__init__ """
        condition = Or(Var(1), Var(2))
        self.assertEqual(1, condition.value[0].value)
        self.assertEqual(2, condition.value[1].value)

        self.assertRaises(TypeError, Or, Var(11), 10)
        self.assertRaises(TypeError, Or, 11, Var(10))
        self.assertRaises(TypeError, Or, 11, 10)

    def test_or_get(self):
        """ testing Or.get """
        condition = Or(Var(True), Var(False))
        self.assertEqual(True, condition.get())
        condition = Or(Var(False), Var(True))
        self.assertEqual(True, condition.get())
        condition = Or(Var(True), Var(True))
        self.assertEqual(True, condition.get())
        condition = Or(Var(False), Var(False))
        self.assertEqual(False, condition.get())

    def test_or_repr(self):
        """ testing Or.__repr__ """
        condition = Or(Var(1), Var(3))
        expected = """Or(Var(1), Var(3))"""
        self.assertEqual(expected, str(condition))

    def test_not_init(self):
        """ testing Not.__init__ """
        condition = Not(Var(1))
        self.assertEqual(1, condition.value[0].value)
        self.assertEqual(None, condition.value[1])

        self.assertRaises(TypeError, Not, 11)

    def test_not_get(self):
        """ testing Not.get """
        condition = Not(Var(True))
        self.assertEqual(False, condition.get())
        condition = Not(Var(False))
        self.assertEqual(True, condition.get())

    def test_not_repr(self):
        """ testing Not.__repr__ """
        condition = Not(Var(1))
        expected = """Not(Var(1))"""
        self.assertEqual(expected, str(condition))
