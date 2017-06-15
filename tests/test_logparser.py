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
# pylint: disable=R0201
import unittest
import os
from datetime import datetime
from hamcrest import assert_that, equal_to
from concept.tools.logparser import LogParser


class TestLogParser(unittest.TestCase):
    """Testing of the LogParser class."""

    def test_full_time_information(self):
        """Testing when all time information are given."""
        test_yaml_configration = os.path.join(os.path.dirname(__file__), 'data/logparser.yml')
        parser = LogParser.from_yaml(test_yaml_configration)
        assert_that(parser.parse_string("""11.06.2017 18:33:12 This is a simple log text"""), equal_to(True))
        assert_that(len(parser.data), equal_to(1))
        assert_that(parser.data[0]['timestamp'].year, equal_to(2017))
        assert_that(parser.data[0]['timestamp'].month, equal_to(6))
        assert_that(parser.data[0]['timestamp'].day, equal_to(11))
        assert_that(parser.data[0]['timestamp'].hour, equal_to(18))
        assert_that(parser.data[0]['timestamp'].minute, equal_to(33))
        assert_that(parser.data[0]['timestamp'].second, equal_to(12))
        assert_that(parser.data[0]['text'], equal_to(' This is a simple log text'))

    def test_auto_date(self):
        """Testing when automatic date from today."""
        test_yaml_configration = os.path.join(os.path.dirname(__file__), 'data/logparser.yml')
        parser = LogParser.from_yaml(test_yaml_configration)
        now = datetime.now()
        assert_that(parser.parse_string("""18:33:12 no date"""), equal_to(True))
        assert_that(len(parser.data), equal_to(1))
        assert_that(parser.data[0]['timestamp'].year, equal_to(now.year))
        assert_that(parser.data[0]['timestamp'].month, equal_to(now.month))
        assert_that(parser.data[0]['timestamp'].day, equal_to(now.day))
        assert_that(parser.data[0]['timestamp'].hour, equal_to(18))
        assert_that(parser.data[0]['timestamp'].minute, equal_to(33))
        assert_that(parser.data[0]['timestamp'].second, equal_to(12))
        assert_that(parser.data[0]['text'], equal_to(''))

    def test_auto_date_and_incomplete_time(self):
        """Testing when automatic date from today and 0 for not given time information.."""
        test_yaml_configration = os.path.join(os.path.dirname(__file__), 'data/logparser.yml')
        parser = LogParser.from_yaml(test_yaml_configration)
        now = datetime.now()
        assert_that(parser.parse_string("""18:33 no date and incomplete time"""), equal_to(True))
        assert_that(len(parser.data), equal_to(1))
        assert_that(parser.data[0]['timestamp'].year, equal_to(now.year))
        assert_that(parser.data[0]['timestamp'].month, equal_to(now.month))
        assert_that(parser.data[0]['timestamp'].day, equal_to(now.day))
        assert_that(parser.data[0]['timestamp'].hour, equal_to(18))
        assert_that(parser.data[0]['timestamp'].minute, equal_to(33))
        assert_that(parser.data[0]['timestamp'].second, equal_to(0))
        assert_that(parser.data[0]['timestamp'].microsecond, equal_to(0))
        assert_that(parser.data[0]['text'], equal_to(''))
