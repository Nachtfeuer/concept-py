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
from concept.data.movies.composer import Composer
from concept.tools.decorator import validate_test_responsibility_for


@validate_test_responsibility_for(Composer)
class TestComposer(unittest.TestCase):
    """ testing of class concept.data.movies.composer.Composer class """

    def test_init(self):
        """ testing of Composer.__init__ method """
        composer = Composer()
        self.assertEqual("", composer.name)

        composer = Composer("Henry Mancini")
        self.assertEqual("Henry Mancini", composer.name)

    def test_repr(self):
        """ testing of Composer.__repr__ method """
        composer = Composer("Henry Mancini")
        self.assertEqual("Composer(name=Henry Mancini)", str(composer))

    def test_get_serializable_name(self):
        """ testing of Composer.get_serializable_name method """
        composer = Composer()
        self.assertEqual("composer", composer.get_serializable_name())

    def test_get_serializable_fields(self):
        """ testing of Composer.get_serializable_fields method """
        composer = Composer()
        fields = ["name"]
        self.assertEqual(fields, composer.get_serializable_fields())

    def test_is_enabled_for_attributes(self):
        """ testing of Composer.is_enabled_for_attributes method """
        composer = Composer()
        self.assertEqual(True, composer.is_enabled_for_attributes())

    def test_equal(self):
        """testing of Composer.__eq__ method """
        composerA = Composer("Henry Mancini")
        composerB = Composer("Jerry Goldsmith")
        composerC = Composer("Henry Mancini")

        self.assertNotEqual(composerA, composerB)
        self.assertNotEqual(composerB, composerC)
        self.assertEqual(composerA, composerC)
        # wrong type
        self.assertFalse(composerA.__eq__(1234))

    def test_to_xml(self):
        """ testing of Composer.toXML method (base class) """
        composer = Composer("Henry Mancini")
        expected = """<composer name="Henry Mancini"/>"""
        self.assertEqual(expected, composer.to_xml())
