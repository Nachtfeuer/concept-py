#!/bin/bash
rm -rf docs
rm -rf dist
rm -rf build
rm -f MANIFEST
rm -f pylint.log
rm -f pep8.log
rm -f pep257.log
rm -f flake8.log
rm -f tests/.coverage
rm -f tests/coverage.xml
rm -rf tests/coverage
rm -f tests/tests.xml
rm -f `find . -name "*.pyc"`
rm -f ccm.xml
