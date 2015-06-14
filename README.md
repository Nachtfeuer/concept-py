# concept-py

### Table Of Contents
[**Welcome**](#welcome)  
[**Quick start**](#quick-start)  
[**Current Content**](#current-content)  
[**Next Action Items (planned)**](#next-action-items-planned)  
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
 ./runAnalyse.sh
 ./runTests.sh
```

Current Content
---------------
 - math classes
   - prime function/classes
     - is_prime and sieve_of_eratosthenes
 - example folder added (using this library)
   - prime tool


Next Action Items (planned)
---------------------------
 - math classes
   - prime function/classes
     - segmented sieve


Level Of Done
-------------
It's mainly about quality and about the tasks you have to consider on each implemenation
indepedent whether it's a new feature or a bug fix. Here's a list of things you <b>ALWAYS</b>
should do - at least for this project (also you should do it for all):

 - <b>clean code</b>
   - don't leave commented code (remove it)
   - ensure consistent style and don't do unfavorable things like long methods, high nested depths,
     too many parameters for a function or method or mixing spaces and tabs (don't use tabs).
 - <b>clean design</b>
   - ensure re-usable code (DRY)
   - KISS (keep it simple software)
 - <b>proper source code documentation</b>
   - use C++ comment style /// (not C style)
   - provide example(s) on how to use things where possible
   - don't document things that are obvious
   - when possible also provide formulas (see math::number for examples)
   - check your documentation before you commit (make doc)
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
   - check for memory leaks and violatios (make memcheck)


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
