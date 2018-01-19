#!/bin/bash

install_chromium (){
    yum install epel-release -y
    yum install chromium -y

    echo -e "\nChromium installation complete.\n"
    which chromium
}

install_firefox (){
    cd /usr/local
    wget https://ftp.mozilla.org/pub/firefox/releases/57.0.4/linux-x86_64/en-US/firefox-57.0.4.tar.bz2
    tar xvjf firefox*
    ln -s /usr/local/firefox/firefox /usr/bin/firefox

    echo -e "\nFirefox installation complete.\n"
    which firefox
}


if [[ $(/usr/bin/id -u) != "0" ]]; then
    echo -e "This looks like a 'non-root' user.\nPlease switch to 'root', or run the script with 'sudo'."
    exit
fi

install_chromium
install_firefox
