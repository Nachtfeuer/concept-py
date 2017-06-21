"""
Parser for log files using regular expressions.

.. module:: logparser
    :platform: Unix, Windows
    :synopis: Parser for log files using regular expressions.

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
import re
from datetime import datetime
from concept.tools.compatible import TextType
import yaml


class LogParser(object):
    """Log parser configurable via a yaml file."""

    def __init__(self, log_filter):
        """Initializing log parser."""
        self.log_filter = log_filter
        self.data = []

    @staticmethod
    def from_yaml(path_and_filename):
        """Creating a log parser for given configuration."""
        log_filter = []
        contants = {}
        for key, value in yaml.load(open(path_and_filename).read()).items():
            if key == "filter" and isinstance(value, list) and \
               all(isinstance(entry, dict) and "regex" in entry for entry in value):
                log_filter = value
            elif key == "constants" and isinstance(value, dict) and \
                    all(isinstance(k, (TextType, str)) and
                        isinstance(v, (TextType, str)) for k, v in value.items()):
                contants = value

        for pos, entry in enumerate(log_filter):
            for key, value in contants.items():
                log_filter[pos]['regex'] = log_filter[pos]['regex'].replace("${%s}" % key, value)

        return LogParser(log_filter)

    def parse_string(self, content):
        """:returns: True when string did contain at least one match."""
        success = False
        for line in content.split("\n"):
            for current_log_filter in self.log_filter:
                match = re.match(current_log_filter['regex'], line)
                if match:
                    now = datetime.now()
                    # default date and time information
                    time_info = {
                        'year': now.year, 'month': now.month, 'day': now.day,
                        'hour': now.hour, 'minute': now.minute, 'second': now.second,
                        'microsecond': now.microsecond
                    }
                    # all matched details
                    entry = match.groupdict()
                    # when it looks like having date information:
                    if 'year' in entry or 'month' in entry or 'day' in entry:
                        # we update the date information only when complete:
                        if 'year' in entry and 'month' in entry and 'day' in entry:
                            time_info['year'] = int(entry['year'])
                            time_info['month'] = int(entry['month'])
                            time_info['day'] = int(entry['day'])

                    # todo: when filter doesn't contain complete time information ...
                    #       then missing fields should be set to 0.
                    reset = any(key in entry for key in ['hour', 'minute', 'second', 'microsecond'])
                    for key in ['hour', 'minute', 'second', 'microsecond']:
                        if reset:
                            time_info[key] = 0
                        if key in entry:
                            time_info[key] = int(entry[key])

                    # creating final timestamp and text
                    text = "" if "text" not in entry else entry['text']
                    timestamp = datetime(
                        time_info['year'], time_info['month'], time_info['day'],
                        hour=time_info['hour'], minute=time_info['minute'],
                        second=time_info['second'], microsecond=time_info['microsecond'])

                    self.data.append({'timestamp': timestamp, 'text': text})
                    success = True
        return success
