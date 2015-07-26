#!/usr/bin/python
"""
Learning tool.

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
# pylint: disable=C0325
import sys
import platform
import click
import random
import time
import json
from datetime import datetime
from concept import VERSION
from concept.generator.select import select
from concept.graph.gnuplot import plot, multiplot, script


def average(entry):
    """ providing average time for an individidual test. """
    return entry['total time (s)']/float(entry['correct answers'] + entry['wrong answers'])


def dump_last_result(statistic):
    """
    Print result of last training to stdout.

    :param statistic: results of last training.
    """
    print("\nResults of last test run:")
    print("  %5d answers were correct." % statistic['correct answers'])
    print("  %5d answers were wrong." % statistic['wrong answers'])
    print("  %5.2f seconds in total." % statistic['total time (s)'])
    print("  %5.2f seconds per answer (average)." % average(statistic))
    print("  %5.2f seconds was best time." % statistic['best time (s)'])
    print("  %5.2f seconds was worst time." % statistic['worst time (s)'])


def dump_total_results(statistic_entries):
    """
    Print summary for all done training to stdout.

    :param statistic_entries: a list of dictionaries with test results.
    """
    individual_tests = sum([entry['correct answers'] + entry['wrong answers']
                           for entry in statistic_entries])
    average_per_test = sum([entry['total time (s)'] for entry in statistic_entries]) \
        / float(individual_tests)
    average_per_run = sum([entry['total time (s)'] for entry in statistic_entries]) \
        / float(len(statistic_entries))

    best_time = min([entry['best time (s)'] for entry in statistic_entries])
    worst_time = max([entry['worst time (s)'] for entry in statistic_entries])

    print("\nSummary for all done tests:")
    print("  %5d total test runs" % len(statistic_entries))
    print("  %5d individual tests" % individual_tests)
    print("  %5.1f individual tests per run" % (individual_tests/float(len(statistic_entries))))
    print("  %5.2f seconds per answer (average)" % average_per_test)
    print("  %5.2f seconds per run (average)" % average_per_run)
    print("  %5.2f seconds was best time." % best_time)
    print("  %5.2f seconds was worst time." % worst_time)


def create_gnuplot_statistic(statistic_entries):
    """ Creating a gnuplot script and generates the image for it. """
    grouped_by_number_of_entries = {}
    for statistic in statistic_entries:
        key = statistic['max entries']
        if key not in grouped_by_number_of_entries:
            grouped_by_number_of_entries[key] = [statistic]
        else:
            grouped_by_number_of_entries[key].append(statistic)

    all_plots = multiplot("learn.py statistics", title_font=("", 18), plots_per_row=2)

    pos = 0
    max_pos = len(grouped_by_number_of_entries) - 1
    for key, statistic in grouped_by_number_of_entries.items():
        average_time_plot = plot()
        average_time_plot.set_ylabel("seconds")
        if pos == max_pos:
            average_time_plot.set_xlabel("n'th test run")
        average_time_plot.set_xtics("1")
        average_time_plot.set_ytics("0.5")
        average_time_plot.set_line_style(1, "lc rgb \"#00ff00\" lw 2")
        average_time_plot.set_fill_style(1, "transparent solid 0.4 border")
        values = list(enumerate([average(entry) for entry in statistic], 1))
        average_time_plot.add_curve("average times (max entries=%d)" % key,
                                    values=values, mode=plot.FILLEDCURVES)

        all_plots.add_plot(average_time_plot)

        number_of_tests_plot = plot()
        number_of_tests_plot.set_ylabel("# tests")
        if pos == max_pos:
            number_of_tests_plot.set_xlabel("n'th test run")
        number_of_tests_plot.set_xtics("1")
        number_of_tests_plot.set_ytics("1")
        number_of_tests_plot.set_line_style(1, "lc rgb \"#00ff00\" lw 2")
        number_of_tests_plot.set_fill_style(1, "transparent solid 0.4 border")
        values = list(enumerate([entry['correct answers']+entry['wrong answers']
                                 for entry in statistic], 1))
        number_of_tests_plot.add_curve("# of tests (max entries=%d)" % key,
                                       values=values, mode=plot.FILLEDCURVES)

        all_plots.add_plot(number_of_tests_plot)
        pos += 1

    calculated_height = len(grouped_by_number_of_entries) * 250
    script("learn.gp", all_plots, width=800, height=calculated_height).execute()


def save(statistic_entries):
    """
    Save all statistic entries to a JSON file.

    :param statistic_entries: a list of dictionaries with test results.
    """
    with open('learn.json', 'w') as file:
        json.dump(statistic_entries, file, indent=2)


def load():
    """
    Load all previous statistic results from a JSON file.

    :returns: list of previous statistic results or empty list of not found.
    """
    try:
        with open('learn.json', 'r') as file:
            return json.load(file)
    except IOError:
        return []


@click.command()
@click.option("--max-entries", default=5, help="number of entries to display")
@click.option("--max-tests", default=10, help="number of tests")
def main(max_entries, max_tests):
    """ Learning tool. """
    print("learning tool (version %s)" % VERSION)
    print(" ... Python %s" % sys.version.replace("\n", ""))
    print(" ... Platform %s" % platform.platform())

    print("\nAll possible entries: %s\n" % select(1, max_entries, 1).build())

    previous_results = load()
    started = datetime.now()
    results = []

    test = 1
    while test <= max_tests:
        entries = select(1, max_entries, 1).shuffled()
        pos = random.randint(0, max_entries-1)
        missing_entry = entries[pos]
        del entries[pos]

        start = time.time()
        answer = input("Which entry is missing: %s: " % entries)
        duration = time.time() - start

        if int(answer) == missing_entry:
            print(" ... correct (took %f seconds)" % duration)
            results.append((True, duration))
        else:
            print(" ... wrong, it was %s (took %f seconds)" % (missing_entry, duration))
            results.append((False, duration))

        test += 1

    total_time = sum([entry[1] for entry in results])
    best_time = min([entry[1] for entry in results])
    worst_time = max([entry[1] for entry in results])
    statistic = {'started': started.strftime("%Y-%m-%d %H:%M:%S"),
                 'max entries': max_entries,
                 'correct answers': sum([1 for entry in results if entry[0]]),
                 'wrong answers': sum([1 for entry in results if not entry[0]]),
                 'total time (s)': total_time,
                 'best time (s)': best_time,
                 'worst time (s)': worst_time}

    previous_results.append(statistic)
    save(previous_results)
    dump_last_result(statistic)
    dump_total_results(previous_results)
    create_gnuplot_statistic(previous_results)

if __name__ == "__main__":
    main()
