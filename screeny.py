#!/usr/bin/env python

from selenium import webdriver
import time

CHROME_BIN = "/bin/chromium-browser"
PROXY_LIST = ["151.80.140.233:54566", "173.249.9.82:8080"]
ctr = 0

for proxy in PROXY_LIST:
    ctr = ctr+1
    FILE_NAME = "ip_chromium" + str(ctr) + ".png"
    options = webdriver.ChromeOptions()

    options.binary_location = CHROME_BIN
    options.add_argument('headless')
    options.add_argument('window-size=1200x600')
    options.add_argument('disable-gpu')
    options.add_argument('--proxy-server=%s' % proxy)

    driver = webdriver.Chrome(chrome_options=options)

    start_time = time.time()
    driver.get('http://whatismyipaddress.com/')
    print("--- %s seconds ---" % (time.time() - start_time))
    driver.implicitly_wait(10)

    driver.get_screenshot_as_file(FILE_NAME)
