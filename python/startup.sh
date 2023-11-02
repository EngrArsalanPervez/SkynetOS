#! /bin/sh
cd /usr/local/src/
screen -dmS startupPython
screen -S startupPython -p 0 -X stuff 'python3 main.py\n'