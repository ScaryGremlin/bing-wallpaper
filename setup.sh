#!/bin/bash

apt install python3-pip python3-virtualenv -y
virtualenv venv --python=python3
source venv/bin/activate
pip3 install -r requirements.txt
deactivate
PATH_BING_WALLPAPER=$(pwd)
(crontab -l 2>/dev/null; echo "0 */1 * * * $PATH_BING_WALLPAPER/venv/bin/python3 $PATH_BING_WALLPAPER/app/bing-wallpaper.py") | crontab -
