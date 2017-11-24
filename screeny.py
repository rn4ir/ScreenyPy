#!/usr/bin/env python

from selenium import webdriver
import time

CHROME_BIN = "browsers/chromium-local/chrome-linux/chrome"
PROXY_LIST = ["24.42.167.242:3128", "151.80.140.233:54566", "80.211.166.20:80"]
ctr = 0

for proxy in PROXY_LIST:
    ctr = ctr+1
    FILE_NAME = "ip" + str(ctr) + ".png"
    options = webdriver.ChromeOptions()

    options.binary_location = CHROME_BIN
    options.add_argument('headless')
    options.add_argument('window-size=1200x600')
    options.add_argument('no-sandbox')
    options.add_argument('disable-gpu')
    options.add_argument('--proxy-server=%s' % proxy)

    driver = webdriver.Chrome(chrome_options=options)

    start_time = time.time()
    driver.get('http://whatismyipaddress.com/')
    print("--- %s seconds ---" % (time.time() - start_time))
    #driver.implicitly_wait(10)

    driver.get_screenshot_as_file(FILE_NAME)
