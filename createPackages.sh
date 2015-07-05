#!/bin/bash
export PYTHONPATH=$PWD
echo "python setup.py sdist"
python setup.py sdist

if [ -z "${PYTHON}" ]; then
    PYTHON=/usr/bin/python
fi

echo "python setup.py bdist_rpm"
python setup.py bdist_rpm --python=${PYTHON} --requires="gnuplot"
