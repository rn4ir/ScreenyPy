#!/usr/bin/env python

import requests
import zipfile
import io
import os
import shutil

DL_DIR = "browsers/chromium-local"
#https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Linux_x64/ >> LAST_CHANGE >> chrome-linux.zip
DL_URL = "https://storage.googleapis.com/chromium-browser-snapshots/Linux_x64/514946/chrome-linux.zip"
CHROME_PATH = DL_DIR + "/chrome-linux/chrome"

def download_zip(req_url):
    """Download data from url."""
    r = requests.get(req_url)

    if not os.path.isdir(DL_DIR):
        os.makedirs(DL_DIR, exist_ok=True)
    else:
        shutil.rmtree(DL_DIR, ignore_errors=True)
        os.makedirs(DL_DIR, exist_ok=True)

    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(DL_DIR)

    os.chmod(CHROME_PATH, 0o755)

download_zip(DL_URL)
