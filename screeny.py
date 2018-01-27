#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time, requests, json

CHROME_BIN = "/bin/chromium-browser"
FIREFOX_BIN = "/bin/firefox"

PROXY_URL = "http://pubproxy.com/api/proxy?limit=3&format=txt&https=true&type=http&last_check=5&level=elite"
read_proxy = requests.get(PROXY_URL)

PROXY_LISTTXT = read_proxy.text
PROXY_LIST = PROXY_LISTTXT.splitlines()

ctr = 0

for proxy in PROXY_LIST:
    ctr = ctr+1
    """
    FILE_NAME = proxy.split(':')[0] + "_chromium" + str(ctr) + ".png"
    options = webdriver.ChromeOptions()

    options.binary_location = CHROME_BIN
    options.add_argument('headless')
    options.add_argument('window-size=1200x600')
    options.add_argument('disable-gpu')
    options.add_argument('--proxy-server=%s' % proxy)

    driver = webdriver.Chrome(chrome_options=options)

    start_time = time.time()
    driver.get('http://en.wikipedia.org/')
    print("--- screenshot " + proxy.split(':')[0] + "_chromium" + str(ctr) + ".png"  +  " generated in %s seconds ---" % (time.time() - start_time))
    driver.implicitly_wait(10)

    driver.get_screenshot_as_file(FILE_NAME)
    """
    FILE_NAME = proxy.split(':')[0] + "_firefox" + str(ctr) + ".png"
#    options = webdriver.Firefox()

    options = Options()
    options.binary_location = FIREFOX_BIN
    options.add_argument('headless')
    options.add_argument('window-size=1200x600')
    options.add_argument('disable-gpu')
    options.add_argument('--proxy-server=%s' % proxy)

    driver = webdriver.Firefox(firefox_options=options)

    start_time = time.time()
    driver.get('http://en.wikipedia.org/')
    print("--- screenshot " + proxy.split(':')[0] + "_firefox" + str(ctr) + ".png"  +  " generated in %s seconds ---" % (time.time() - start_time))
    driver.implicitly_wait(10)

    driver.get_screenshot_as_file(FILE_NAME)

