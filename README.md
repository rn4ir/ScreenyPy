#### ScreenyPy - A command-line tool to take screenshots of websites from different geographical locations.

#### Requirements

- Python 3.x
- [requirements.txt](https://github.com/rn4ir/ScreenyPy/blob/master/requirements.txt)

#### Purpose

The purpose of this script is to take screenshots for a given URL from different geographical locations, from the command-line interface.  
The script currently using only supports Chromium and has a website URL hardcoded within.
  
#### Usage  
  
```
$ python screeny.py
--- screenshot 52.144.57.75_chromium1.png generated in 1.264365196228027 seconds ---
--- screenshot 122.183.139.101_chromium2.png generated in 6.4740517139434814 seconds ---
--- screenshot 128.199.138.67_chromium3.png generated in 3.6867733001708984 seconds ---
```
  
##### TODO:  

- Firfox support.
- Accept user input for the website URL, to test any URL.
- a more reliable source of proxies.
