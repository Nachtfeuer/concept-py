#!/bin/bash
#                      _                _                      _     
#  _ __ _   _ _ __    / \   _ __   __ _| |_   _ ___  ___   ___| |__  
# | '__| | | | '_ \  / _ \ | '_ \ / _` | | | | / __|/ _ \ / __| '_ \ 
# | |  | |_| | | | |/ ___ \| | | | (_| | | |_| \__ \  __/_\__ \ | | |
# |_|   \__,_|_| |_/_/   \_\_| |_|\__,_|_|\__, |___/\___(_)___/_| |_|
#                                         |___/                      
# creating console report
radon cc -a concept tests examples

# creating XML report
radon cc -a --xml concept tests examples > ccm.xml 2>&1

# creating pylint report
pylint --rcfile=./.rclint.2.x concept tests examples > pylint.log 2>&1
grep "rated at" pylint.log

# creating pep8 report
pep8 --max-line-length=110 --ignore=E731 concept tests examples >  pep8.log 2>&1
echo "`cat pep8.log | wc -l` pep8 warnings/errors (see pep8.log)"

# creating pep257 report
pep257 concept tests examples > pep257.log 2>&1
echo "`cat pep257.log | wc -l` pep257 warnings/errors (see pep257.log)"

# creating flake8 report
flake8 --max-line-length=120 --ignore=E731 --exclude=virt_env,docs * | grep "\.py" > flake8.log 2>&1
echo "`cat flake8.log |  wc -l` flake8 warnings/errors (see flake8.log)"
