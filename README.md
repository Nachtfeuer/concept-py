README
======

[![Build Status](https://travis-ci.org/Nachtfeuer/concept-py.svg?branch=master)](https://travis-ci.org/Nachtfeuer/concept-py)
[![Coverage Status](https://coveralls.io/repos/Nachtfeuer/concept-py/badge.svg?branch=master)](https://coveralls.io/r/Nachtfeuer/concept-py?branch=master)

### Table Of Contents
[**Welcome**](#welcome)  
[**Quick start**](#quick-start)  
[**Current Content**](#current-content)  
[**Next Action Items (planned)**](#next-action-items-planned)  
[**Requirements**](#requirements)  
[**Examples**](#examples)  
[**Level Of Done**](#level-of-done)  
[**Version Policy**](#version-policy)  

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
```
 git clone https://github.com/Nachtfeuer/concept-py.git
 cd concept-py
 source srcipts/virtual
 ./runAnalyse.sh
 ./runTests.sh
```

Current Content
---------------
 - enabled Travis CI build (tested with Python 2.7.x, 3.2.x, 3.3.x, 3.4.x and PyPy).
 - enabled for virtual environment
 - math classes
   - prime function/classes
     - is_prime and sieve_of_eratosthenes and its optimized version
     - segmented sieve (a first - working - version)
   - digit functions: sum_digits, count_digits, is_pandigital, is_palindrome
   - factorization: probe.
   - number functions: is_square, triangle, is_triangle, pentagonal, is_pentagonal
 - example folder added (using this library)
   - prime tool
   - sequence generator tool
 - crypt/decrypt functions/classes
   - rail fence cipher
   - Caesar cipher
   - Vigenère cipher


Next Action Items (planned)
---------------------------
 - statistic mechanism for different algorithms enable using R.
 - crypt/decrypt functions/classes
   - other
 - math sequence generator
   - writing generated sequences to a database
   - being able to group all sequence which generate same sequence
   - allowing to repeat a formula 'n' times
   - adding integer division function
   - adding integer square root function
   - adding pow function (examples: 2^10 = 1024 or (-1)^x)
 - example folder
   - encrypt tool (choosable algorithm)
   - decrypt tool (choosable algorithm)

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
