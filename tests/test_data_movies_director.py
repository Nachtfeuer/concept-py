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
from concept.data.movies.director import Director
from concept.tools.decorator import validate_test_responsibility_for
from concept.tools.compatible import TextType


@validate_test_responsibility_for(Director)
class TestComposer(unittest.TestCase):
    """testing of class concept.data.movies.director.Director class."""

    def test_init(self):
        """testing of Director.__init__ method."""
        director = Director()
        self.assertEqual("", director.name)

        composer = Director(TextType("Alfred Hitchcock"))
        self.assertEqual("Alfred Hitchcock", composer.name)

    def test_repr(self):
        """ testing of Composer.__repr__ method """
        director = Director(TextType("Alfred Hitchcock"))
        self.assertEqual("Director(name=Alfred Hitchcock)", str(director))

    def test_get_serializable_name(self):
        """ testing of Director.get_serializable_name method """
        director = Director()
        self.assertEqual("director", director.get_serializable_name())

    def test_get_serializable_fields(self):
        """ testing of Director.get_serializable_fields method """
        director = Director()
        fields = ["name"]
        self.assertEqual(fields, director.get_serializable_fields())

    def test_is_enabled_for_attributes(self):
        """ testing of Director.is_enabled_for_attributes method """
        director = Director()
        self.assertEqual(True, director.is_enabled_for_attributes())

    def test_equal(self):
        """ testing of Actor.__eq__ method """
        directorA = Director(TextType("Alfred Hitchcock"))
        directorB = Director(TextType("Billy Wilder"))
        directorC = Director(TextType("Alfred Hitchcock"))

        self.assertNotEqual(directorA, directorB)
        self.assertNotEqual(directorB, directorC)
        self.assertEqual(directorA, directorC)
        # wrong type
        self.assertFalse(directorA.__eq__(1234))

    def test_to_xml(self):
        """ testing of Director.toXML method (base class) """
        director = Director(TextType("Alfred Hitchcock"))
        expected = """<director name="Alfred Hitchcock"/>"""
        self.assertEqual(expected, director.to_xml())
