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

def main():
    """
    Main function.
    Checks command-line arguments and calls the relevant function.
    """

    cli_argparser = argparse.ArgumentParser(description='pymyip - A python script that generates screenshots of a website from various random locations.')
    cli_argparser.add_argument('-c', '--chrome', nargs='?', const=1, help="Generates screenshots using Chromium", required=False)
    cli_argparser.add_argument('-f', '--firefox', nargs='?', const=1, help="Generates screenshots using Mozilla Firefox", required=False)

    cli_args = cli_argparser.parse_args()

    if (cli_args.chrome):
        (myip("a"))
    elif (cli_args.firefox):
        (myip("l"))
    else:
        print ("\nYour WAN IP is: " + myip() + "\n")

if __name__ == '__main__':
    sys.exit(main())
