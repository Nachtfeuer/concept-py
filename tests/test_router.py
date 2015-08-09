"""
   =======
   License
   =======
   Copyright (c) 2015 Thomas Lehmann

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
# pylint: disable=R0201
import unittest
from hamcrest import assert_that, equal_to, calling, raises
from concept.tools.decorator import validate_test_responsibility_for
from concept.tools.router import router


@validate_test_responsibility_for(router)
class TestRouter(unittest.TestCase):

    """ Testing of router. """

    def test_init(self):
        """ Testing default state. """
        rinst = router()
        assert_that(rinst.rules, equal_to({}))

    def test_add(self):
        """ Testing adding of a rule. """
        rinst = router()
        rinst.add("/test/<name>")

        expected = {2: {'/test/(?P<name>[^/]+)': None}}
        assert_that(rinst.rules, equal_to(expected))
        assert_that(calling(rinst.add).with_args("/test/<name>/<name>"), raises(ValueError))

    def test_add_with_function(self):
        """ Testing adding of a rule and a function. """
        get_name = lambda name: name

        rinst = router()
        rinst.add("/test/<name>", get_name)

        expected = {2: {'/test/(?P<name>[^/]+)': get_name}}
        assert_that(rinst.rules, equal_to(expected))

    def test_match(self):
        """ Testing matching of a URL against a rule. """
        rinst = router()
        rinst.add("/test/<name>")

        match, function = rinst.match("/test/Agatha")
        assert_that(match, equal_to({'name': 'Agatha'}))
        assert_that(function, equal_to(None))

        match, function = rinst.match("/unknown/Agatha")
        assert_that(match, equal_to({}))
        assert_that(function, equal_to(None))

    def test_match_with_function(self):
        """ Testing matching of a URL against a rule. """
        get_name = lambda name: name

        rinst = router()
        rinst.add("/test/<name>", get_name)

        match, function = rinst.match("/test/Agatha")
        assert_that(match, equal_to({'name': 'Agatha'}))
        assert_that(function, equal_to(get_name))

    def test_route(self):
        """ Testing routing which does apply matched data against registered function. """
        rinst = router()
        rinst.add("/test/<name>", lambda name: name)
        assert_that(rinst.route("/test/Agatha"), equal_to("Agatha"))

    def test_route_advanced(self):
        """ tesing routining with multiple rules. """
        rinst = router()
        rinst.add("/test/<name>", lambda name: name)
        rinst.add("/test/<name>/<value>", lambda name, value: (name, value))

        assert_that(rinst.route("/test/Agatha"), equal_to("Agatha"))
        assert_that(rinst.route("/test/Agatha/Christie"), equal_to(("Agatha", "Christie")))
        assert_that(rinst.route("/test/Agatha/Christie/Book"), equal_to(None))
        assert_that(rinst.route("/test2/Agatha"), equal_to(None))
        assert_that(rinst.route("/test2/Agatha/Christie"), equal_to(None))
