"""
   Representing one movie.

.. module:: movie
    :platform: Unix, Windows
    :synopis: providing data for a movie

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
from concept.tools.serialize import Serializable
from concept.data.movies.director import Director
from concept.data.movies.actor import Actor
from concept.data.movies.composer import Composer
from concept.data.movies.tag import Tag
from concept.data.movies.purchase import Purchase
from concept.tools.compatible import TextType


# R0902 = about too many fields
# pylint: disable=R0902
class Movie(Serializable):
    """Representing one movie (DVD, Blu-ray, ...)."""

    def __init__(self, title=TextType("")):
        """Initializing fields only (defaults)."""
        super(Movie, self).__init__()

        self.title = title            # german title (or your language)
        self.original = ""            # original title
        self.url = ""                 # german url to Wikipedia (or your language)
        self.directors = []           # list of directors
        self.actors = []              # list of actors
        self.composers = []           # list of composers
        self.runtime = 0              # runtime in minutes
        self.aspect_ratio = ""        # aspect ratio
        self.publication = 0          # year of publication
        self.tags = []                # list of tags (strings) to allows grouping by category
        self.purchase = Purchase()    # purchase information

    def is_enabled_for_attributes(self):
        """
        Adjusted to true for writing some fields as XML attributes.

        :rtype: True for writing the fields as attributes of the tag
        """
        return True

    def add_director(self, director):
        """
        Adding a new director.

        :param: director: another director for given movie
        :rtype: True if the director has been successfully added otherwise false.
        """
        if not isinstance(director, Director):
            return False

        if director not in self.directors:
            self.directors.append(director)
            return True
        return False

    def add_actor(self, actor):
        """
        Adding a new actor.

        :param: actor: another actor for given movie
        :rtype: True if the actor has been successfully added otherwise false.
        """
        if not isinstance(actor, Actor):
            return False

        if actor not in self.actors:
            self.actors.append(actor)
            return True
        return False

    def add_composer(self, composer):
        """
        Adding a new composer.

        :param: composer: another composer for given movie
        :rtype: True if the composer has been successfully added otherwise false.
        """
        if not isinstance(composer, Composer):
            return False

        if composer not in self.composers:
            self.composers.append(composer)
            return True
        return False

    def add_tag(self, tag):
        """
        Adding a new tag.

        :param: tag: another tag for given movie
        :rtype: True if the tag has been successfully added otherwise false.
        """
        if not isinstance(tag, Tag):
            return False

        if tag not in self.tags:
            self.tags.append(tag)
            return True
        return False

    def __eq__(self, other):
        """
        Compare this object to be equal with another in type and data.

        :param: other: another movie instance (expected)
        :rtype: True if movies are identical
        """
        if not isinstance(other, Movie):
            return False

        if not self.title == other.title:
            return False

        if not self.directors == other.directors:
            return False

        # we can assume that same title is not directed by same director(s)
        # for two or more different movies
        return True

    def to_xml(self):
        """
        Provide this movie instance as XML string.

        :return: Movie as an XML string with a final line break
        """
        return super(Movie, self).to_xml() + "\n"
