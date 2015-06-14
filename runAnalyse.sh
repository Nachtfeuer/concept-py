#!/bin/bash
#                      _                _                      _     
#  _ __ _   _ _ __    / \   _ __   __ _| |_   _ ___  ___   ___| |__  
# | '__| | | | '_ \  / _ \ | '_ \ / _` | | | | / __|/ _ \ / __| '_ \ 
# | |  | |_| | | | |/ ___ \| | | | (_| | | |_| \__ \  __/_\__ \ | | |
# |_|   \__,_|_| |_/_/   \_\_| |_|\__,_|_|\__, |___/\___(_)___/_| |_|
#                                         |___/                      
# creating console report
radon cc -a concept

# creating XML report
radon cc -a --xml concept examples > ccm.xml

# creating pylint report
pylint --rcfile=./.rclint.2.x concept examples > pylint.log
grep "rated at" pylint.log

# creating pep8 report
pep8 --max-line-length=100 concept examples > pep8.log
echo "`cat pep8.log | wc -l` pep8 warnings/errors (see pep8.log)"

# creating pep257 report
pep257 2> pep257.log
echo "`cat pep257.log | wc -l` pep257 warnings/errors (see pep257.log)"

# creating flake8 report
flake8 --max-line-length=120 * | grep "\.py" > flake8.log
echo "`cat flake8.log |  wc -l` flake8 warnings/errors (see flake8.log)"
