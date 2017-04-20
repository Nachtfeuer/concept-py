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
from concept.data.movies.tag import Tag
from concept.tools.decorator import validate_test_responsibility_for


@validate_test_responsibility_for(Tag)
class TestTag(unittest.TestCase):
    """ testing of class pydemo.movies.tag.Tag class """

    def test_init(self):
        """ testing of Tag.__init__ method """
        director = Tag()
        self.assertEqual("", director.name)

        tag = Tag("Martial Art")
        self.assertEqual("Martial Art", tag.name)

    def test_repr(self):
        """ testing of Tag.__repr__ method """
        tag = Tag("Martial Art")
        self.assertEqual("Tag(name=Martial Art)", str(tag))

    def test_get_serializable_name(self):
        """ testing of Tag.get_serializable_name method """
        tag = Tag()
        self.assertEqual("tag", tag.get_serializable_name())

    def test_get_serializable_fields(self):
        """ testing of Tag.get_serializable_fields method """
        tag = Tag()
        fields = ["name"]
        self.assertEqual(fields, tag.get_serializable_fields())

    def test_is_enabled_for_attributes(self):
        """ testing of Tag.is_enabled_for_attributes method """
        tag = Tag()
        self.assertEqual(True, tag.is_enabled_for_attributes())

    def test_equal(self):
        """ testing of Tag.__eq__ method """
        tagA = Tag("Martial Art")
        tagB = Tag("Science Fiction")
        tagC = Tag("Martial Art")

        self.assertNotEqual(tagA, tagB)
        self.assertNotEqual(tagB, tagC)
        self.assertEqual(tagA, tagC)
        # wrong type
        self.assertFalse(tagA.__eq__(1234))

    def test_to_xml(self):
        """ testing of Tag.to_xml method (base class) """
        tag = Tag("Science Fiction")
        expectedXML = """<tag name="Science Fiction"/>"""
        self.assertEqual(expectedXML, tag.to_xml())
