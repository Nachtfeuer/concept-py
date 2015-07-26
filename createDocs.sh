#!/bin/bash
export PYTHONPATH=$PWD
[ ! -d docs ] && mkdir docs
sphinx-apidoc -A "Thomas Lehmann" -F -o docs concept
pushd docs
make html
popd
