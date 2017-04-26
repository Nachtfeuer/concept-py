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
from concept.data.movies.movie import Movie
from concept.data.movies.actor import Actor
from concept.data.movies.director import Director
from concept.data.movies.composer import Composer
from concept.data.movies.tag import Tag
from concept.data.movies.purchase import Purchase
from concept.tools.decorator import validate_test_responsibility_for
from concept.tools.compatible import TextType


@validate_test_responsibility_for(Movie)
class TestMovie(unittest.TestCase):
    """testing of class pydemo.movies.movie.Movie class."""

    def test_init(self):
        """testing of Movie.__init__ verifying the defaults."""
        movie = Movie()
        self.assertEqual("", movie.title)
        self.assertEqual("", movie.original)
        self.assertEqual("", movie.url)
        self.assertEqual("", movie.aspect_ratio)
        self.assertEqual([], movie.directors)
        self.assertEqual([], movie.actors)
        self.assertEqual([], movie.composers)
        self.assertEqual(0, movie.runtime)

    def test_is_enabled_for_attributes(self):
        """ testing of Movie.is_enabled_for_attributes method """
        movie = Movie()
        self.assertEqual(True, movie.is_enabled_for_attributes())

    def test_add_actor(self):
        """testing of Movie.addActor method."""
        movie = Movie()
        self.assertTrue(movie.add_actor(Actor(TextType("John Wayne"), TextType("Sean Mercer"))))
        self.assertFalse(movie.add_actor(Actor(TextType("John Wayne"), TextType("Sean Mercer"))))
        self.assertFalse(movie.add_actor(Composer(TextType("Henry Mancini"))))

    def test_add_director(self):
        """testing of Movie.add_director method."""
        movie = Movie()
        self.assertTrue(movie.add_director(Director(TextType("Alfred Hitchcock"))))
        self.assertFalse(movie.add_director(Director(TextType("Alfred Hitchcock"))))
        self.assertFalse(movie.add_director(Composer(TextType("Henry Mancini"))))

    def test_add_composer(self):
        """testing of Movie.add_composer method."""
        movie = Movie()
        self.assertTrue(movie.add_composer(Composer(TextType("Henry Mancini"))))
        self.assertFalse(movie.add_composer(Composer(TextType("Henry Mancini"))))
        self.assertFalse(movie.add_composer(Director(TextType("Alfred Hitchcock"))))

    def test_add_tag(self):
        """testing of Movie.addComposer method."""
        movie = Movie()
        self.assertTrue(movie.add_tag(Tag(TextType("Science Fiction"))))
        self.assertFalse(movie.add_tag(Tag(TextType("Science Fiction"))))
        self.assertFalse(movie.add_tag(Director(TextType("Alfred Hitchcock"))))

    def test_get_serializable_name(self):
        """ testing of Movie.get_serializable_name method """
        movie = Movie()
        self.assertEqual("movie", movie.get_serializable_name())

    def test_get_serializable_fields(self):
        """ testing of Movie.get_serializable_fields method """
        movie = Movie()
        fields = sorted(["title", "original", "url", "actors", "directors",
                         "composers", "runtime", "aspect_ratio", "tags", "publication", "purchase"])
        self.assertEqual(fields, movie.get_serializable_fields())

    def test_equal(self):
        """ testing of Movie.__eq__ method """
        movie_a, movie_b, movie_c = Movie(), Movie(), Movie()

        movie_a.title = "title A"
        movie_b.title = "title A"
        movie_c.title = "title C"

        self.assertEqual(Movie(), Movie())
        self.assertEqual(movie_a, movie_b)
        self.assertNotEqual(movie_a, movie_c)

        movie_b.add_director(Director(TextType("Alfred Hitchcock")))
        self.assertNotEqual(movie_a, movie_b)

    def test_to_xml(self):
        """ testing of Movie.toXML method """
        movie = Movie()
        movie.title = "Ein Hauch von Nerz"
        movie.original = "That Touch of Mink"
        movie.url = "http://de.wikipedia.org/wiki/Ein_Hauch_von_Nerz"
        movie.aspect_ratio = "16:9 - 1.77:1"
        movie.runtime = 94
        movie.publication = 1962
        movie.add_director(Director(TextType("Delbert Mann")))
        movie.add_actor(Actor(TextType("Sean Connery"), TextType("James Bond")))
        movie.add_composer(Composer(TextType("Henry Mancini")))
        movie.add_tag(Tag(TextType("Komoedie")))
        movie.purchase = Purchase(where=TextType("Amazon"),
                                  when=TextType("2007-07-18"),
                                  url=TextType("http://amazon.de/dp/B00004X07N"))
        expected = """<movie """ \
            + """aspect_ratio="16:9 - 1.77:1" """ \
            + """original="That Touch of Mink" """ \
            + """publication="1962" """ \
            + """runtime="94" """ \
            + """title="Ein Hauch von Nerz" """ \
            + """url="http://de.wikipedia.org/wiki/Ein_Hauch_von_Nerz">""" \
            + """<actors><actor name="Sean Connery" role="James Bond"/></actors>""" \
            + """<composers><composer name="Henry Mancini"/></composers>""" \
            + """<directors><director name="Delbert Mann"/></directors>""" \
            + """<purchase url="http://amazon.de/dp/B00004X07N" when="2007-07-18" where="Amazon"/>""" \
            + """<tags><tag name="Komoedie"/></tags>""" \
            + "</movie>\n"
        self.assertEqual(expected, movie.to_xml())
