#!/bin/bash
# Some links to read:
# - http://pypy.org/download.html
# - https://github.com/squeaky-pl/portable-pypy#portable-pypy-distribution-for-linux
# - http://doc.pypy.org/en/latest/install.html
PROMPT="run_python.sh :: "

## @fn init_py27
## Installation of Python 2.7.x from the devtoolset.
function init_py27() {
    yum -y install centos-release-scl yum-utils
    yum-config-manager --enable rhel-server-rhscl-7-rpms
    yum -y install python27
    scl enable python27 "bash -c \"pip install setuptools --upgrade\""
    scl enable python27 "bash -c \"pip install tox\""
    scl enable python27 "bash -c \"/docker/scripts/run_python.sh RUN\""
}

## @fn init_py33
## Installation of Python 3.3.x from the devtoolset.
function init_py33() {
    yum -y install centos-release-scl yum-utils
    yum-config-manager --enable rhel-server-rhscl-7-rpms
    yum -y install python33
    scl enable python33 "bash -c \"easy_install pip\""
    scl enable python33 "bash -c \"pip install pip --upgrade\""
    scl enable python33 "bash -c \"pip install setuptools --upgrade\""
    scl enable python33 "bash -c \"pip install tox\""
    scl enable python33 "bash -c \"/docker/scripts/run_python.sh RUN\""
}

## @fn init_py34
## Installation of Python 3.4.x from the devtoolset.
function init_py34() {
    yum -y install centos-release-scl yum-utils
    yum-config-manager --enable rhel-server-rhscl-7-rpms
    yum -y install rh-python34
    scl enable rh-python34 "bash -c \"pip install pip --upgrade\""
    scl enable rh-python34 "bash -c \"pip install setuptools --upgrade\""
    scl enable rh-python34 "bash -c \"pip install tox\""
    scl enable rh-python34 "bash -c \"/docker/scripts/run_python.sh RUN\""
}

## @fn init_py35
## Installation of Python 3.5.x from the devtoolset.
function init_py35() {
    yum -y install centos-release-scl yum-utils
    yum-config-manager --enable rhel-server-rhscl-7-rpms
    yum -y install rh-python35
    scl enable rh-python35 "bash -c \"pip install pip --upgrade\""
    scl enable rh-python35 "bash -c \"pip install setuptools --upgrade\""
    scl enable rh-python35 "bash -c \"pip install tox\""
    scl enable rh-python35 "bash -c \"/docker/scripts/run_python.sh RUN\""
}

## @fn init_py36
## Installation of Python 3.6.x; here we require a build since there has been no devtoolset available.
function init_py36() {
    yum -y install wget gcc make openssl-devel
    wget -q https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tar.xz
    tar -xf $(ls Python*.tar.xz)
    cd Python*
    ./configure
    make && make altinstall
    ln -s /usr/local/bin/pip3.6 /usr/local/bin/pip
    pip install pip --upgrade
    pip install setuptools --upgrade
    pip install tox
    $0 RUN
}


## @fn init_pypy
## Installation of PyPy with Python 2.7.x compatible version.
function init_pypy() {
    yum -y install wget bzip2
    echo "${PROMPT}Downloading pypy (Python 2.7 compatible) ..."
    wget -q https://bitbucket.org/squeaky/portable-pypy/downloads/pypy-5.7.1-linux_x86_64-portable.tar.bz2
    echo "${PROMPT}unpacking pypy (Python 2.7 compatible) to /opt ..."
    tar -xvjf $(ls pypy*.tar.bz2) -C /opt > /dev/null
    ln -s /opt/$(ls /opt|grep pypy) /opt/pypy
    ln -s /opt/pypy/bin/pypy /usr/local/bin/pypy
    ln -s /opt/pypy/bin/virtualenv-pypy /usr/local/bin/virtualenv
    pypy -m ensurepip
    ln -s /opt/pypy/bin/pip2 /usr/local/bin/pip
    pip install pip --upgrade
    pip install setuptools --upgrade
    pip install tox
    ln -s /opt/pypy/bin/tox /usr/local/bin/tox
    $0 RUN
}

## @fn init_pypy3
## Installation of PyPy with Python 3.5 compatible version.
function init_pypy3() {
    yum -y install wget bzip2
    echo "${PROMPT}Downloading pypy (Python 3.5 compatible) ..."
    wget -q https://bitbucket.org/squeaky/portable-pypy/downloads/pypy3.5-5.7.1-beta-linux_x86_64-portable.tar.bz2
    echo "${PROMPT}unpacking pypy (Python 3.5 compatible) to /opt ..."
    tar -xvjf $(ls pypy3*.tar.bz2) -C /opt > /dev/null
    ln -s /opt/$(ls /opt|grep pypy) /opt/pypy
    ln -s /opt/pypy/bin/pypy /usr/local/bin/pypy
    ln -s /opt/pypy/bin/virtualenv-pypy /usr/local/bin/virtualenv
    pypy -m ensurepip
    ln -s /opt/pypy/bin/pip3 /usr/local/bin/pip
    pip install pip --upgrade
    pip install setuptools --upgrade
    pip install tox
    ln -s /opt/pypy/bin/tox /usr/local/bin/tox
    $0 RUN
}

if [ $# -eq 0 ]; then
    set -euo pipefail
    IFS=$'\n\t'

    echo "PWD=$PWD"
    docker run --rm=true -v $PWD:/docker \
            -e "CI=yes" \
            -e "UID=$(id -u)" -e "UPWD=$PWD" \
            -e "PYTHON_VERSION=$PYTHON_VERSION" \
            -i centos:7.3.1611 /docker/scripts/run_python.sh INIT
else
    case $1 in
        INIT)
            echo "${PROMPT} Init phase ..."
            case ${PYTHON_VERSION} in
                py27)
                    init_py27;
                    ;;
                py33)
                    init_py33;
                    ;;
                py34)
                    init_py34
                    ;;
                py35)
                    init_py35;
                    ;;
                py36)
                    init_py36;
                    ;;
                pypy)
                    init_pypy;
                    ;;
                pypy3)
                    init_pypy3;
                    ;;
               *)
                    echo "${PROMPT}Python version '${PYTHON_VERSION}' not known or not supported!"
                    exit 1
                    ;;

            esac
            ;;
        RUN)
            echo "${PROMPT} Copy phase ..."
            mkdir -p /work
            cd /work
            cp -r /docker/* .
            echo "${PROMPT} What we have available at /work in the container:"
            ls -al /work

            pip -V

            if [ "${CI:-}" == "yes" ]; then
                echo "${PROMPT} Run phase ..."
                if [ -e /usr/local/bin/pypy ]; then
                    pypy -V
                    tox -e pypy
                else
                    python -V
                    tox -e ${PYTHON_VERSION}
                fi

                sed -i "s:/work/concept/:${UPWD}/concept/:g" .coverage
                cp .coverage /docker
                chown -R ${UID} /docker/.coverage
            fi
            ;;
        BASH)
            docker run --name=pydev -v $PWD:/docker \
                    -e "UID=$(id -u)" \
                    -it centos:7.3.1611 bash
            ;;
    esac
fi
