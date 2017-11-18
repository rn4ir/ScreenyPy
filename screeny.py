#!/usr/bin/env python

from selenium import webdriver

CHROME_BIN = "browsers/chromium-local/chrome-linux/chrome"

options = webdriver.ChromeOptions()

options.binary_location = CHROME_BIN
options.add_argument('headless')
options.add_argument('window-size=1200x600')
options.add_argument('no-sandbox')
options.add_argument('disable-gpu')

driver = webdriver.Chrome(chrome_options=options)

driver.get('https://muchbits.com')
driver.implicitly_wait(10)

driver.get_screenshot_as_file('muchbits.png')
