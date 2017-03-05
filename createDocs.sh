#!/bin/bash
export PYTHONPATH=$PWD
[ ! -d docs ] && mkdir docs
sphinx-apidoc -A "Thomas Lehmann" -F -o docs/api concept
sed -i "s/\(extensions = \[\)/\1'sphinx.ext.mathjax',/g" docs/api/conf.py
sphinx-build -b html docs/api docs/html
