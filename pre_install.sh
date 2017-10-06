#!/bin/bash

prerequisites(){
    mkdir -p sources/{firefox,driver}
    sudo yum install gtk3*
}

download_firefox(){
    curl -o ./sources/firefox/firefox.tar.bz2 https://download-installer.cdn.mozilla.net/pub/firefox/nightly/latest-mozilla-central/firefox-58.0a1.en-US.linux-x86_64.tar.bz2 sources/firefox/firefox.tar.bz2
    tar jxf ./sources/firefox/firefox.tar.bz2 -C ./sources/firefox/
    version=$(./sources/firefox/firefox/firefox --version)
    echo -e "Mozilla Firefox download complete.\nVersion: $version"
}

download_gecko(){
    cd ./sources/driver/; wget https://github.com/mozilla/geckodriver/releases/download/v0.19.0/geckodriver-v0.19.0-linux64.tar.gz; cd -
    tar zxf ./sources/driver/geckodriver-v0.19.0-linux64.tar.gz -C ./sources/driver/
    version=$(./sources/driver/geckodriver -V | head -1)
    echo -e "Gecko driver download complete.\nVersion: $version"
}

prerequisites
download_firefox
download_gecko
