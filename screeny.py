#!/usr/bin/env python

from selenium import webdriver
import time, requests, json

CHROME_BIN = "/bin/chromium-browser"
PROXY_URL = "http://pubproxy.com/api/proxy?limit=3&format=txt&https=true&type=http&last_check=5&level=elite"
read_proxy = requests.get(PROXY_URL)

PROXY_LISTTXT = read_proxy.text
PROXY_LIST = PROXY_LISTTXT.splitlines()

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
    driver.get('http://whatismyip.host/')
    print("--- screenshot " + "ip_chromium" + str(ctr) + ".png"  +  " generated in %s seconds ---" % (time.time() - start_time))
    driver.implicitly_wait(10)

    driver.get_screenshot_as_file(FILE_NAME)
