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
import os
import pickle
import inspect

from concept.tools.decorator import validate_test_responsibility_for
from concept.data.movies import MovieManager, Movie, Actor


@validate_test_responsibility_for(MovieManager)
class TestMovieManager(unittest.TestCase):
    """testing of class concept.data.movies.manager.MovieManager class."""

    def test_init(self):
        """ testing of MovieManager.__init__ verifying the defaults """
        manager = MovieManager()
        self.assertEqual([], manager.movies)

    def test_get_serializable_name(self):
        """ testing of MovieManager.get_serializable_name method """
        manager = MovieManager()
        self.assertEqual("root", manager.get_serializable_name())

    def test_add_movie(self):
        """ testing of MovieManager.add_movie method """
        manager = MovieManager()
        self.assertTrue(manager.add_movie(Movie("a simple test")))
        self.assertFalse(manager.add_movie(Movie("a simple test")))
        self.assertFalse(manager.add_movie(Movie()))
        self.assertFalse(manager.add_movie(Actor()))

    def test_to_xml(self):
        """ testing of MovieManager.to_xml method """
        manager = MovieManager()
        expectedXML = "<root><movies>"
        expectedXML += "</movies></root>"

        self.assertEqual(expectedXML, manager.to_xml())

    def test_save_as(self):
        """ testing of MovieManager.save_as method """
        manager = MovieManager()
        manager.add_movie(Movie("test title"))
        self.assertFalse(manager.save_as("testSaveAs.xml", 1234))
        self.assertTrue(manager.save_as("testSaveAs.xml", MovieManager.PERSISTENCE_POLICY.XML))

        expected = "<root><movies>"
        expected += "<movie><actors></actors><aspect_ratio></aspect_ratio><composers></composers>"
        expected += "<directors></directors><original></original><publication>0</publication>"
        expected += """<purchase url="" when="" where=""/><runtime>0</runtime><tags></tags>"""
        expected += """<title>test title</title><url></url></movie>\n"""
        expected += "</movies></root>"
        given = open("testSaveAs.xml").read()
        self.assertEqual(expected, given)
        os.remove("testSaveAs.xml")

        self.assertTrue(manager.save_as("testSaveAs.dat", MovieManager.PERSISTENCE_POLICY.PICKLE))
        data = pickle.load(open("testSaveAs.dat", "rb"))
        self.assertTrue(data is not None)
        self.assertTrue(isinstance(data, list))
        self.assertEqual(1, len(data))
        self.assertEqual(Movie("test title"), data[0])
        os.remove("testSaveAs.dat")

    def test_read_from(self):
        """testing of MovieManager.readFrom method using pickle."""
        managerA = MovieManager()
        managerA.add_movie(Movie("test title"))
        self.assertTrue(managerA.save_as("testSaveAs.dat", MovieManager.PERSISTENCE_POLICY.PICKLE))

        managerB = MovieManager()
        self.assertFalse(managerB.read_from("testSaveAs.dat", MovieManager.PERSISTENCE_POLICY.XML))
        self.assertTrue(managerB.read_from("testSaveAs.dat", MovieManager.PERSISTENCE_POLICY.PICKLE))

        self.assertTrue(managerB.movies is not None)
        self.assertTrue(isinstance(managerB.movies, list))
        self.assertEqual(1, len(managerB.movies))
        self.assertEqual(Movie("test title"), managerB.movies[0])
        os.remove("testSaveAs.dat")

    def test_read_from_json(self):
        """testing of MovieManager.readFrom method using pickle."""
        managerA = MovieManager()
        managerA.add_movie(Movie("test title"))
        self.assertTrue(managerA.save_as("testSaveAs.json", MovieManager.PERSISTENCE_POLICY.JSON))

        managerB = MovieManager()
        self.assertTrue(managerB.read_from("testSaveAs.json", MovieManager.PERSISTENCE_POLICY.JSON))

        self.assertTrue(managerB.movies is not None)
        self.assertTrue(isinstance(managerB.movies, list))
        self.assertEqual(1, len(managerB.movies))
        self.assertEqual(Movie("test title"), managerB.movies[0])
        os.remove("testSaveAs.json")

    def test_iter(self):
        """ testing of MovieManager.__iter__ method """
        manager = MovieManager()
        path = os.path.dirname(inspect.getfile(self.__class__))
        self.assertTrue(manager.read_from(os.path.join(path, "data/movies.pickle"),
                        MovieManager.PERSISTENCE_POLICY.PICKLE))
        counter = 0
        for movie in manager:
            if movie.title.lower().find("ice age") >= 0:
                counter += 1

        self.assertEqual(3, counter)

    def test_get_movies_by_filter(self):
        """ testing of MovieManager.getMoviesByFilter method """
        manager = MovieManager()
        path = os.path.dirname(inspect.getfile(self.__class__))
        manager.read_from(os.path.join(path, "data/movies.pickle"),
                          MovieManager.PERSISTENCE_POLICY.PICKLE)

        movies = manager.get_movies_by_filter("Ice Age")
        self.assertEqual(3, len(movies))
        movies = manager.get_movies_by_filter("ice age")
        self.assertEqual(3, len(movies))
