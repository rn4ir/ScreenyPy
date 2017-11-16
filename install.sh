#!/bin/bash

PLATFORM=linux64
VERSION=$(curl http://chromedriver.storage.googleapis.com/LATEST_RELEASE)
DL_DIR="browsers/chromium-local/chrome-linux/"

sudo yum install GConf2 -y

wget "http://chromedriver.storage.googleapis.com/$VERSION/chromedriver_$PLATFORM.zip"
sudo unzip chromedriver_$PLATFORM.zip -d $(echo $PATH | cut -d: -f1)
rm -fv chromedriver_$PLATFORM.zip
