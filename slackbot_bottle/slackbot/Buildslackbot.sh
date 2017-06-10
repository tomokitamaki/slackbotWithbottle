#!/bin/bash

pip3.5 install slackbot requests
git clone https://github.com/tomokitamaki/slackbotWithbottle.git
mv /root/APITOKEN.py /root/slackbotWithbottle/APITOKEN.py
python3.5 /root/slackbotWithbottle/run.py
