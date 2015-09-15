README
======

[![Build Status](https://travis-ci.org/Nachtfeuer/concept-py.svg?branch=master)](https://travis-ci.org/Nachtfeuer/concept-py)
[![Coverage Status](https://coveralls.io/repos/Nachtfeuer/concept-py/badge.svg?branch=master)](https://coveralls.io/r/Nachtfeuer/concept-py?branch=master)
[![PyPI version](https://badge.fury.io/py/concept-py.png)](http://badge.fury.io/py/concept-py)

### Table Of Contents
[**Welcome**](#welcome)  
[**Quick start**](#quick-start)  
[**Current Content**](#current-content)  
[**Next Action Items (planned)**](#next-action-items-planned)  
[**Requirements**](#requirements)  
[**Examples**](#examples)  
[**Level Of Done**](#level-of-done)  
[**Version Policy**](#version-policy)  
[**Interesting Links**](#interesting-links)  

Welcome
-------
Welcome to the README of my personal Python reference project.
It's a kind of knowledge database and small test environment.

This project is partly synchronized with another project
of mine: https://github.com/Nachtfeuer/concept-cpp

The purpose is - of course - to keep everything clean, simple and
well documented. Please keep in mind and read:

 - [**Level Of Done**](#level-of-done)
 - [**Version Policy**](#version-policy)


Quick start
-----------
Installing latest released version:
```
pip install concept-py
```

Development on this project:
```
 git clone https://github.com/Nachtfeuer/concept-py.git
 cd concept-py
 source srcipts/virtual
 ./runAnalyse.sh
 ./runTests.sh
```

Current Content
---------------
 - enabled Travis CI build (tested with Python 2.7.x, 3.2.x, 3.3.x, 3.4.x, PyPy and PyPy3).
 - enabled for virtual environment
 - math classes
   - prime function/classes
     - is_prime and sieve_of_eratosthenes and its optimized version
     - segmented sieve (a first - working - version)
   - digit functions: sum_digits, count_digits, is_pandigital, is_palindrome
   - factorization: probe.
   - number functions: is_square, triangle, is_triangle, pentagonal, is_pentagonal,
     hexagonal, is_hexagonal.
   - matrix class.
 - container query with
   - 'where' and 'transform'
   - 'sum' and 'average'
   - 'min' and 'max'
 - range select functionality like container query (like concept-cpp)
   - 'shuffled'
 - example folder added (using this library)
   - prime tool
   - sequence generator tool
   - learning tool
     - find missing value in a shuffled sequence of values.
     - date and time when a run was started
     - best time and worst time in test run
     - export of gnuplot (multiplot) script and generated png image
       with average time per max seen entries in a test run.
     - graph for number of tests per test run
     - export displaying "visual" results (see gnuplot)
   - easy mail tool
     - supporting HTML and styles
     - supporting attachment
     - supporting embedded images (example provided; thanks to cooltext.com)
 - crypt/decrypt functions/classes
   - rail fence cipher
   - Caesar cipher
   - Vigenere cipher
 - lightweight gnuplot support to generate some graphs
   - plot class to wrap one plot function.
   - script class that write the script and executes gnuplot.
   - can generate png, svg, jpeg and gif.
   - image width and height adjustable.
   - xlabel and ylabel per plot
   - color and styles adjustments per line style "index"
     (rgb color, line width, ...) 
   - adjusting of fill style per curve (style index as before)
   - enable mode "filledcurves"
   - adding multiplot class for multiple plot on one "page" (image).
 - data decorator for tests
   - execution function/method for each value of the list (single=True parameter)
 - common validator class
 - schema class for defining validation of data
 - router for url


Next Action Items (planned)
---------------------------
 - writing a script that runs tests across multiple python versions
   using the virtual environment.
 - let build fail when pep8, pep257 or flake warnings are NOT 0.
 - let build fail when pylint rating is less or equal 9.
 - math sequence generator
   - writing generated sequences to a database
   - being able to group all sequence which generate same sequence
   - allowing to repeat a formula 'n' times
   - adding integer division function
   - adding integer square root function
   - adding pow function (examples: 2^10 = 1024 or (-1)^x)
   - detection of two formula being opposites like (x+1) and (x-1)
     to avoid to have those as chain.
 - learning tool
   - graph for success/failure per number ...
   - adding trend line for average
 - lightweight gnuplot support to generate some graphs
   - font size for labels (and color).
   - trend lines (note: unfortunately have to print values double).
   - dashed and dotted lines.
 - data decorator for tests
   - values = dict(...) => values = [(k1, v1), (k1, v2), ...]
   - values = func()
 - Travis CI
   - freenode notification? (creation nick name first then the channel)
   - jython support? (https://www.topbug.net/old/use-travis-ci-with-jython/)


Requirements
------------
 - for checking the requirements do following:
   ```
   cat requirements.txt | sed "s/=.*$//g" | xargs -i pip show {}
   ```
 - for installing all requirements do following:
   ```
   pip install -r requirements.txt
   ```

Examples
--------
 - using the prime generation tool:
   ```
   examples/primes.py --max-number=80000000 --sieve=optimized --columns=-1 > primes.txt
   ```
   On my small and relative slow notebook I was able to get it with following results:
   ```
   prime tool
     ... Python 2.7.6 (default, Mar 22 2014, 22:59:56) [GCC 4.8.2]
     ... Platform Linux-3.13.0-24-generic-x86_64-with-LinuxMint-17-qiana
     ... using algorithm "optimized"
     ... searching primes <= 80000000

     >> output of primes <<

     ... 4669382 primes found.
     ... sieve calculation took 43.863128 seconds
     ... prime calculation took 105.560736 seconds
   ```
   Obvious the generation of the final prime list is expensive.
   Requires some investigation.


Level Of Done
-------------
It's mainly about quality and about the tasks you have to consider on each implemenation
indepedent whether it's a new feature or a bug fix. Here's a list of things you <b>ALWAYS</b>
should do - at least for this project (also you should do it for all):

 - <b>clean code</b>
   - don't leave commented code (remove it)
   - ensure consistent style and don't do unfavorable things like long methods, high nested depths,
     too many parameters for a function or method or mixing spaces and tabs (don't use tabs).
   - check issues with ./runAnalyse.sh (pylint.log, pep8.log, pep257.log, flake8.log)
 - <b>clean design</b>
   - ensure re-usable code (DRY)
   - KISS (keep it simple software)
 - <b>proper source code documentation</b>
   - provide example(s) on how to use things where possible
   - don't document things that are obvious
   - check your documentation before you commit (./createDoc.sh)
 - <b>writing unit tests</b>
   - always write unit tests
   - ensure a line coverage above 90%
   - always run the tests before you commit your changes
 - <b>no compiler warnings</b>
   - keep compiler warnings extremely low
   - preferable: 0 warnings
 - <b>ensure consistent versioning</b>
   - read [**Version Policy**](#version-policy)
   - provide a version on each commit (see git log for examples)
 - <b>using other tools</b>
   - check for memory leaks and violations


Version Policy
--------------
 - a version has the form **a.b.c**
 - "a" is the **major version** which is incremented by following reasons:
   - there's a set of **new** features with a lot of code which make it reasonable
     to increment the major version.
   - another reason would be the change of one or more interfaces which have been
     necessary to improve things. Needs to be well documented of course and
     should not happen to often.
 - "b" is the **minor version** which represents:
   - simple **new** features
   - simple **extensions** to given features
   - minor changes like adding missing documentation or style things.
 - "c" is the **bugfix counter** and is incremented on **bugfixes only**.
 - Following additional rules:
   - incrementing "b" resets "c" to zero (0.5.0, 1.0.0, 1.1.0, 1.2.0, 2.0.0, ...)
   - incrementing "a" resets "b" and "c" to zero (0.5.1, 1.0.0, 1.1.2, 2.0.0, ...)
   - each commit message (since policy has been introduced) should refer
     to a version by mentioning it in form: "a.b.c: title" in first line and
     as many details you like in following lines.

Interesting links
-----------------
 - https://travis-ci.org (CI build)
 - https://coveralls.io (coverage report)
 - https://badge.fury.io (badges like version of package in Python package index)
 - https://pypi.python.org/pypi?%3Aaction=pkg_edit&name=concept-py

