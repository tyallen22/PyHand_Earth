#!/bin/bash
echo Update Packages
sudo apt update

echo Installing Google Earth
cd ~
mkdir google-earth && cd google-earth
wget https://dl.google.com/dl/earth/client/current/google-earth-stable_current_amd64.deb
sudo dpkg -i google-earth-stable*.deb

echo Creating Python3 Virtual Environment: earth01
cd ~
python3 -m venv earth01

echo Activating Virtual Environment
source earth01/bin/activate

echo Installing Dependencies
pip3 install opencv-python==4.2.0.34
pip3 install matplotlib==3.2.2
pip3 install --upgrade tensorflow==2.2.0
pip3 install Keras==2.4.2

echo Install Curl to handle Google Drive redirects
sudo apt install curl

echo Downloading Model
curl -c /tmp/cookies "https://drive.google.com/uc?export=download&id=18oXums8kjOF6iPw9iMwdXVlqqxswEiRm" > /tmp/intermezzo.html
curl -L -b /tmp/cookies "https://drive.google.com$(cat /tmp/intermezzo.html | grep -Po 'uc-download-link" [^>]* href="\K[^"]*' | sed 's/\&amp;/\&/g')" > ~/Desktop/PyHand_Earth/tyler/testing/pyearth_cnn_model_200612_1744.h5

#echo Downloading Python Project File - Won't work unless file is public
#wget https://raw.githubusercontent.com/liujohnj/PyHand_Earth/master/john/test_run_02/hand_recognition_a.py

echo Done