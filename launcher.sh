#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/Crypto10bot
sudo python scrapertop10.py
cd /

cd /
cd home/pi/Crypto10bot/top10winners
sudo python top10winners.py
cd /

cd /
cd home/pi/Crypto10bot/top10losers
sudo python top10losers.py
cd /