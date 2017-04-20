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
from concept.data.movies.actor import Actor
from concept.tools.decorator import validate_test_responsibility_for


@validate_test_responsibility_for(Actor)
class TestActor(unittest.TestCase):
    """ testing of class pydemo.movies.movie.Movie class """

    def test_init(self):
        """ testing of Actor.__init__ method """
        actor = Actor()
        self.assertEqual("", actor.name)
        self.assertEqual("", actor.role)

        actor = Actor("Sean Connery", "James Bond")
        self.assertEqual("Sean Connery", actor.name)
        self.assertEqual("James Bond", actor.role)

    def test_repr(self):
        """ testing of Actor.__repr__ method """
        actor = Actor("Sean Connery", "James Bond")
        self.assertEqual("Actor(name=Sean Connery, role=James Bond)", str(actor))

    def test_get_serializable_name(self):
        """ testing of Actor.get_serializable_name method """
        actor = Actor()
        self.assertEqual("actor", actor.get_serializable_name())

    def test_get_serializable_fields(self):
        """ testing of Actor.get_serializable_fields method """
        actor = Actor()
        fields = sorted(["name", "role"])
        self.assertEqual(fields, actor.get_serializable_fields())

    def test_is_enabled_for_attributes(self):
        """ testing of Actor.is_enabled_for_attributes method """
        actor = Actor()
        self.assertEqual(True, actor.is_enabled_for_attributes())

    def test_equal(self):
        """ testing of Actor.__eq__ method """
        actorA = Actor("Sean Connery", "James Bond")
        actorB = Actor("Roger Moore", "James Bond")
        actorC = Actor("Sean Connery", "Ahmed ben Mohammed el-Raisuli")
        actorD = Actor("Sean Connery", "James Bond")

        self.assertNotEqual(actorA, actorB)
        self.assertNotEqual(actorA, actorC)
        self.assertNotEqual(actorB, actorC)
        self.assertEqual(actorA, actorD)
        # wrong type
        self.assertFalse(actorA.__eq__(1234))

    def test_to_xml(self):
        """ testing of Actor.toXML method (base class) """
        actor = Actor("Sean Connery", "James Bond")
        expected = """<actor name="Sean Connery" role="James Bond"/>"""
        self.assertEqual(expected, actor.to_xml())
