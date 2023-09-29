#!/bin/bash



DIR=$(dirname "${BASH_SOURCE[0]}")
## VENVNAME=$DIR/src/venv

## apt-get install python3-pip python3-dev libpq-dev -y

pushd $DIR
##pip3 install virtualenv
##virtualenv -p python3 $VENVNAME
##source $VENVNAME/bin/activate
python3 src/ClientWeather2.py
##deactivate
popd
