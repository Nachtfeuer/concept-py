#!/bin/bash
export PYTHONPATH=$PWD
python setup.py sdist
python setup.py bdist_rpm
