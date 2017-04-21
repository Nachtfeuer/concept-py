"""
.. module:: manager
    :platform: Unix, Windows
    :synopis: providing MovieManager class maintaining all movies
              and providing load and save functionality

.. moduleauthor:: Thomas Lehmann <thomas.lehmann.private@googlemail.com>

   =======
   License
   =======
   Copyright (c) 2013 Thomas Lehmann

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
from concept.data.movies.movie import Movie
from concept.tools.enum import enum
import pickle
import jsonpickle


class MovieManager(Serializable):
    """ providing MovieManager class maintaining all movies
        and providing load and save functionality """

    PERSISTENCE_POLICY = enum("PICKLE JSON XML")

    def __init__(self):
        """ initializing fields only (defaults) """
        super(MovieManager, self).__init__()

        self.movies = []

    def get_serializable_name(self):
        """ XML name of tag """
        return "root"

    def add_movie(self, movie):
        """
        :param: movie: another movie to add
        :rtype: True if the movie has been successfully added otherwise false.
        """
        if not isinstance(movie, Movie):
            return False
        # you need to have a title at least
        if len(movie.title) == 0:
            return False
        # you cannot add same movie twice
        if movie not in self.movies:
            self.movies.append(movie)
            return True
        return False

    def __iter__(self):
        """
        :rtype: iterator to the list of movies
        """
        return iter(self.movies)

    def save_as(self, pathAndFileName, policy):
        """
        :param pathAndFileName: path and name of file where to store the movies
        :param policy: the persistence policy on how to save the data (pickle, XML, ...)
        :return: True when successfully saved.
        """
        if self.PERSISTENCE_POLICY.XML == policy:
            handle = open(pathAndFileName, "wb")
            handle.write(self.to_xml().encode('utf8'))
            handle.close()
            return True

        if self.PERSISTENCE_POLICY.PICKLE == policy:
            handle = open(pathAndFileName, "wb")
            pickle.dump(self.movies, handle)
            handle.close()
            return True

        if self.PERSISTENCE_POLICY.JSON == policy:
            with open(pathAndFileName, "w") as handle:
                handle.write(jsonpickle.encode(self.movies))
            return True

        return False

    def read_from(self, pathAndFileName, policy):
        """
        :param pathAndFileName: path and name of file where to read the movies from
        :param policy: the persistence policy on how to read the data (pickle, ...)
        :return: True when successfully red.
        """
        if self.PERSISTENCE_POLICY.PICKLE == policy:
            handle = open(pathAndFileName, "rb")
            self.movies = pickle.load(handle)
            handle.close()
            return True

        if self.PERSISTENCE_POLICY.JSON == policy:
            with open(pathAndFileName, "r") as handle:
                self.movies = jsonpickle.decode(handle.read())
            return True

        return False

    def get_movies_by_filter(self, search):
        """
        :param: search: string to use for searching in the title
        :rtype: movies with a title containing the search string
        """
        search = search.lower()
        return [movie for movie in self.movies if movie.title.lower().find(search) >= 0]
