#!/bin/bash
nosetests --with-xunit --with-coverage --cover-package=concept --cover-html --cover-html-dir=coverage.html --cover-xml --cover-xml-file=coverage.xml
