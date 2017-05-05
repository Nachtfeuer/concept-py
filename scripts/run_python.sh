#!/bin/bash
# Some links to read:
# - http://pypy.org/download.html
# - https://github.com/squeaky-pl/portable-pypy#portable-pypy-distribution-for-linux
# - http://doc.pypy.org/en/latest/install.html
PROMPT="run_python.sh :: "
if [ $# -eq 0 ]; then
    docker run --rm=true -v $PWD:/docker \
            -e "UID=$(id -u)" \
            -e "PYTHON_VERSION=$PYTHON_VERSION" \
            -i centos:7.3.1611 /docker/scripts/run_python.sh INIT
else
    case $1 in
        INIT)
            echo "${PROMPT} Init phase ..."
            case ${PYTHON_VERSION} in
                py27)
                    yum -y install centos-release-scl yum-utils
                    yum-config-manager --enable rhel-server-rhscl-7-rpms
                    yum -y install python27
                    scl enable python27 "bash -c \"pip install tox\""
                    scl enable python27 "bash -c \"/docker/scripts/run_python.sh RUN\""
                    ;;
                py33)
                    yum -y install centos-release-scl yum-utils
                    yum-config-manager --enable rhel-server-rhscl-7-rpms
                    yum -y install python33
                    scl enable python33 "bash -c \"easy_install pip\""
                    scl enable python33 "bash -c \"pip install tox\""
                    scl enable python33 "bash -c \"/docker/scripts/run_python.sh RUN\""
                    ;;
                py34)
                    yum -y install centos-release-scl yum-utils
                    yum-config-manager --enable rhel-server-rhscl-7-rpms
                    yum -y install rh-python34
                    scl enable rh-python34 "bash -c \"pip install tox\""
                    scl enable rh-python34 "bash -c \"/docker/scripts/run_python.sh RUN\""
                    ;;
                py35)
                    yum -y install centos-release-scl yum-utils
                    yum-config-manager --enable rhel-server-rhscl-7-rpms
                    yum -y install rh-python35
                    scl enable rh-python35 "bash -c \"pip install tox\""
                    scl enable rh-python35 "bash -c \"/docker/scripts/run_python.sh RUN\""
                    ;;
                pypy)
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
                    pip install tox
                    ln -s /opt/pypy/bin/tox /usr/local/bin/tox
                    $0 RUN
                    ;;
                pypy3)
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
                    pip install tox
                    ln -s /opt/pypy/bin/tox /usr/local/bin/tox
                    $0 RUN
                    ;;
               *)
                    echo "${PROMPT}Python version '${PYTHON_VERSION}' not known or not supported!"
                    exit 1
                    ;;

            esac
            ;;
        RUN)
            mkdir -p /work
            cd /work
            cp -r /docker/* .

            pip -V
            echo "${PROMPT} Run phase ..."
            if [ -e /usr/local/bin/pypy ]; then
                pypy -V
                tox -e pypy
            else
                python -V
                tox -e ${PYTHON_VERSION}
            fi
            ;;
        BASH)
            docker run --rm=true -v $PWD:/docker \
                    -e "UID=$(id -u)" \
                    -it centos:7.3.1611 bash
            ;;
    esac
fi
