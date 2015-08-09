"""
   Router for URL to function/method call.

.. module:: convert
    :platform: Unix, Windows
    :synopis: router for URL to function/method call.

.. moduleauthor:: Thomas Lehmann <thomas.lehmann.private@googlemail.com>


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
import re


class router(object):

    """
    The router allows executing a function by a concrete URL.

    Therefor you can define a rule which can be a URL with
    variables (see example) and the router tries to find best match.

    >>> r = router()
    >>> r.add("/test/<name>")
    >>> r.match("/test/1"), r.match("/test/abc")
    (({'name': '1'}, None), ({'name': 'abc'}, None))
    >>> r.add("/test/<name>/<value>")
    >>> r.match("/test/abc")
    ({'name': 'abc'}, None)
    >>> m, f = r.match("/test/abc/123")
    >>> [(k, m[k]) for k in sorted(m)]
    [('name', 'abc'), ('value', '123')]
    """

    def __init__(self):
        """ initializing fields only. """
        self.rules = {}

    def add(self, rule, function=None):
        """
        Trying to add new rule and a function for it (when given).

        :param rule: a kind of URL optional with variable definitions.
        :param function: a function that should have exact same parameters as defined in rule.
        :returns: True when succeeded.
        """
        variables = re.findall("<[a-z]+>", rule)
        if not len(set(variables)) == len(variables):
            raise ValueError("duplicated names in rule")

        key = rule.count("/")
        for variable in variables:
            rule = rule.replace(variable, "(?P<%s>[^/]+)" % variable[1:-1])

        if key not in self.rules:
            self.rules[key] = {rule: function}
        else:
            if rule not in self.rules[key]:
                self.rules[key][rule] = function

    def match(self, url):
        """
        Try to find the best match for given URL.

        :param url: the url to match against a rule.
        :returns: variables (if given) and the relating function.
        """
        key = url.count("/")
        if key in self.rules:
            for rule in self.rules[key]:
                re_match = re.match(rule, url)
                if re_match:
                    return re_match.groupdict(), self.rules[key][rule]
        return {}, None

    def route(self, url):
        """
        Try to execute function for given URL.

        :param url: the url to match against a rule.
        """
        variables, function = self.match(url)
        if function:
            return function(**variables)
