#!/usr/bin/python
"""
Tool for analyzing logs.

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
import sys
import platform
import os
import click
import requests
from concept import VERSION
from concept.tools.logparser import LogParser
from concept.graph.gnuplot import plot, script


@click.command()
@click.option('--configuration',
              default=os.path.join(os.getcwd(), 'logparser.yml'),
              help="Yaml file that contains the logparser configuration")
@click.option('--url', default='',
              help="When specified reading log from given URL")
def main(configuration, url):
    """logparser tool."""
    print("logparser tool (version %s)" % VERSION)
    print(" ... Python %s" % sys.version.replace("\n", ""))
    print(" ... Platform %s" % platform.platform())
    print(" ... Using configuration %s" % configuration)

    if len(url) > 0:
        response = requests.get(url)
        parser = LogParser.from_yaml(configuration)
        parser.parse_string(response.content)
        max_pos = len(parser.data) - 1
        data = []
        for pos, entry in enumerate(parser.data):
            if pos < max_pos:
                duration = parser.data[pos + 1]['timestamp'] - parser.data[pos]['timestamp']
                print("%10.5f - %s" % (duration.total_seconds(), entry['text']))
                data.append((pos, duration.total_seconds()))

        duration_plot = plot()
        duration_plot.set_ylabel("duration (seconds)")
        duration_plot.set_xlabel("nth duration")
        duration_plot.set_xtics("1")
        duration_plot.set_ytics("1")
        duration_plot.set_line_style(1, "lc rgb \"#00ff00\" lw 2")
        duration_plot.set_fill_style(1, "transparent solid 0.4 border")
        duration_plot.add_curve("Duration of log sections", values=data,
                                mode=plot.FILLEDCURVES)

        script("logparser.gp", duration_plot, width=800, height=600).execute()


if __name__ == "__main__":
    main()
