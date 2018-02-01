#### ScreenyPy - A command-line tool to take screenshots of websites from different geographical locations. (***WIP***)

#### Requirements

- Python 3.x
- [requirements.txt](https://github.com/rn4ir/ScreenyPy/blob/master/requirements.txt)

#### Purpose

The purpose of this script is to take screenshots for a given URL from different geographical locations, from the command-line interface.  
The script currently using only supports Chromium and has a website URL hardcoded within.
  
#### Usage  
  
1. Install all the prerequisites:  
```
$ python3 -m pip install -r requirements.txt
$ sudo ./install.sh
```
  
2. Options:  
```
$ python screeny.py --help

usage: screeny.py [-h] [-c [CHROME]] [-f [FIREFOX]]

screenypy - A python script that generates screenshots of a website from
various random locations.

optional arguments:
  -h, --help            show this help message and exit
  -c [CHROME], --chrome [CHROME]
                        Generates screenshots using Chromium
  -f [FIREFOX], --firefox [FIREFOX]
                        Generates screenshots using Mozilla Firefox
```
  
2a. To generate a screenshot using Chromium:  
```
$ python screeny.py -c

The website will be test from the following IPs:

200.223.197.74:8080
187.53.62.82:80
201.183.227.197:8080

Browser selected: Chromium
Generating screenshots using Chromium


--- screenshot 200.223.197.74_chromium1.png generated in 0.7663443088531494 seconds ---
--- screenshot 187.53.62.82_chromium2.png generated in 18.873610734939575 seconds ---
--- screenshot 201.183.227.197_chromium3.png generated in 2.50515151023865 seconds ---
```  
2b. To generate a screenshot using Firefox:
```
$ python screeny.py -f

The website will be test from the following IPs:

199.7.220.121:8080
85.10.236.172:1080
209.126.124.73:9283

Browser selected: Firefox
Generating screenshots using Firefox


--- screenshot 199.7.220.121_firefox1.png generated in 3.5610098838806152 seconds ---
--- screenshot 85.10.236.172_firefox2.png generated in 3.918879747390747 seconds ---
--- screenshot 209.126.124.73_firefox3.png generated in 3.439244270324707 seconds ---
```
  
##### TODO:  

- User-Input validation.
- A more reliable source of proxies.
