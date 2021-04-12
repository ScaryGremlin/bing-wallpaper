#!/bin/bash

apt install python3-pip python3-virtualenv -y
virtualenv venv --python=python3
source venv/bin/activate
pip3 install -r requirements.txt
