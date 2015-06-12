#!/bin/bash
export PYTHONPATH=$PWD

OPTIONS="--with-coverage"
OPTIONS="$OPTIONS --cover-package=concept"
OPTIONS="$OPTIONS --cover-html"
OPTIONS="$OPTIONS --cover-html-dir=coverage"
OPTIONS="$OPTIONS --cover-xml"
OPTIONS="$OPTIONS --cover-xml-file=coverage.xml"
OPTIONS="$OPTIONS --with-doctest"
OPTIONS="$OPTIONS --with-xunit"
OPTIONS="$OPTIONS --xunit-file=tests.xml"
OPTIONS="$OPTIONS --failure-detail"
cd tests
echo "nosetests $OPTIONS"
nosetests $OPTIONS test_*.py
cd ..
