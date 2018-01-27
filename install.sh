#!/bin/bash

install_chromium() {
    yum install epel-release -y
    yum install chromium -y

    echo -e "\nChromium installation complete.\n"
    which chromium
}

install_firefox() {
    yum install xorg-x11-server-Xvfb -y
    Xvfb :99 &
    export DISPLAY=:99

    cd /usr/local
    wget https://ftp.mozilla.org/pub/firefox/releases/57.0.4/linux-x86_64/en-US/firefox-57.0.4.tar.bz2
    tar xvjf firefox*
    ln -s /usr/local/firefox/firefox /usr/bin/firefox

    echo -e "\nFirefox installation complete.\n"
    which firefox
}

install_chromedriver() {
    PLATFORM=linux64
    VERSION=$(curl http://chromedriver.storage.googleapis.com/LATEST_RELEASE)

    wget "http://chromedriver.storage.googleapis.com/$VERSION/chromedriver_$PLATFORM.zip"
    unzip chromedriver_$PLATFORM.zip -d $(echo $PATH | cut -d: -f1)
    rm -fv chromedriver_$PLATFORM.zip
}

install_geckodriver() {
    wget "https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz"
    tar zxf geckodriver-v0.19.1-linux64.tar.gz -C $(echo $PATH | cut -d: -f1)
    rm -fv geckodriver-v0.19.1-linux64.tar.gz
}

if [[ $(/usr/bin/id -u) != "0" ]]; then
    echo -e "This looks like a 'non-root' user.\nPlease switch to 'root', or run the script with 'sudo'."
    exit
fi

install_chromium
install_firefox
install_chromedriver
install_geckodriver
