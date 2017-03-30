#!/bin/bash
export PYTHONPATH=$PWD

OPTIONS=""
OPTIONS="$OPTIONS --no-byte-compile"
OPTIONS="$OPTIONS --with-doctest"
OPTIONS="$OPTIONS --with-xunit"
OPTIONS="$OPTIONS --xunit-file=tests.xml"
OPTIONS="$OPTIONS --failure-detail"

if [ "$1" == "watch" ]; then
    OPTIONS="$OPTIONS --with-watch"
else
    OPTIONS="$OPTIONS --with-coverage"
    OPTIONS="$OPTIONS --cover-erase"
    OPTIONS="$OPTIONS --cover-package=concept"
    OPTIONS="$OPTIONS --cover-html"
    OPTIONS="$OPTIONS --cover-html-dir=coverage"
    OPTIONS="$OPTIONS --cover-xml"
    OPTIONS="$OPTIONS --cover-xml-file=coverage.xml"
    OPTIONS="$OPTIONS --cover-min-percentage=98"
fi

echo "nosetests $OPTIONS"
nosetests ${OPTIONS}
