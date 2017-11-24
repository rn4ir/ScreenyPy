#!/bin/bash

PLATFORM=linux64
VERSION=$(curl http://chromedriver.storage.googleapis.com/LATEST_RELEASE)
DL_DIR="browsers/chromium-local/chrome-linux/"

sudo yum install GConf2 libXScrnSaver -y
sudo yum install ipa-gothic-fonts xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-utils xorg-x11-fonts-cyrillic xorg-x11-fonts-Type1 xorg-x11-fonts-misc -y

wget "http://chromedriver.storage.googleapis.com/$VERSION/chromedriver_$PLATFORM.zip"
sudo unzip chromedriver_$PLATFORM.zip -d $(echo $PATH | cut -d: -f1)
rm -fv chromedriver_$PLATFORM.zip

python download_chromium.py
