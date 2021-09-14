import os
os.system('clear')
import time
from bs4 import BeautifulSoup
from collections import deque
import json
import nmap
import os
import re
import requests
import requests.exceptions
import time
from time import gmtime, strftime
from urllib.error import URLError
from urllib.parse import urlsplit
import urllib3
import urllib.request
from urllib.request import urlopen
import os
import sys
import threading
import string
import base64
import urllib.request
import urllib.parse
import random

def banner():
    print("""\033[1;31;40m
  
                               _               |
     _                              _   __
     | \          .-'               |    \     .- |__
     |  -,-.-.   '-. _  \_.\_.  .   |     || | `. |
     |  |  | |     || `\|  |  \_|   |  `._/`-'_.' |
     '          '-' `._/     .  |   |             `-'
                       |      `-'                _  .
      _  _  .  \ |__   |     _     .-.  _    _ .' | |
     /  | `||,-. |     |--. /-'   |  __| `\/' ||  | |
     ._ `-'`|  | |     |   |\_,   |   |`._/\_.' \_| '
               ` '-    |`-'__      `-'              o
  
  
   \n""")
def menu():
    print("\33[1;31;40mIP INFO TOOL\n")
    print("--------------------")
    print("1.   Whois Lookup")
    print("2.   Ip tracker")
    print("3.   Dns lookup")
    print("4.   Update")
    print("5.   ANON-SMS")
    print("6.   Url shortener")
    print("7.   Exit")
    print("--------------------")

def nuker():
    choice = ("1")
    banner()

    while choice != ("3"):
        menu()
        choice = input("\033[1;31;40mNuker~#:\033[1;m ")

        if choice == ("1"):
            try:
                target = input("\033[1;31;40mEnter Domain or IP Address: ").lower()
                os.system("reset")
                print("\033[1;31;40mWhois Lookup: ".format(target) + target)
                time.sleep(1.5)
                command = ("whois " + target)
                proces = os.popen(command)
                results = str(proces.read())
                print(" \033[1;31;40m" + results + command + "\033[0m")
                input('\033[1;31;40mWe are done now....\n Press Enter To Exit....')
                os.system('clear')
            except Exception:
                pass


        if choice == ("2"):
            try:
                target = input("\033[1;31;40mEnter Domain or IP Address: ").lower()
                url = ("http://ip-api.com/json/")
                response = urllib.request.urlopen(url + target)
                data = response.read()
                jso = json.loads(data)
                os.system("reset")
                print("\033[32m IP tracking: \033[0m".format(url) + target)
                time.sleep(1.5)

                print("\n [+] \033[34mUrl: " + target + "\033[0m")
                os.system('clear')
                print(" ")
                print("\033[1;31;40mBitches IP: " + jso["query"]+ "\033[0m")
                print(" ")
                print("\033[1;31;40mBitches Country: " + jso["country"] + "\033[0m")
                print(" ")
                print("\033[1;31;40mBitches Region and city: " + jso["regionName"] + ", " + jso["city"] + "\033[0m") 
                print(" ")
                print("\033[1;31;40mBitches Zipcode: " + jso["zip"] + "\033[0m")
                print(" ")
                print("\033[1;31;40mBitches Lat & Lon: " + str(jso['lat']) + " & " + str(jso['lon']) + "\033[0m")
                print(" ")
                print("\033[1;31;40mBitches ISP: " + jso["isp"] + "\033[0m")  
                print(" ")
                print("\033[1;31;40mBitches AS: " + jso["as"] + "\033[0m")
                print(" ")
                print("\033[1;31;40mBitches TimeZone: " + jso["timezone"] + "\033[0m")
                print(" ")
                input('\033[1;31;40mWe are done now....\n Press Enter To Exit....')
                os.system('clear')
            except URLError:
                print("\033[1;32m[-] Please provide a valid IP address!\033[1;m")
        
            except Exception:
                pass

        elif choice == ("3"):
            try:
                target = input("\033[1;31;40mEnter Domain or IP Address: \033[1;m").lower()
                os.system("reset")
                print("\033[1;31;40mSearching for DNS Lookup: \033[0m".format(target) + target)
                time.sleep(1.5)
                command = ("dig " + target + " +trace ANY")
                proces = os.popen(command)
                results = str(proces.read())
                print(results + command)
                input('\033[1;31;40mWe are done now....\n Press Enter To Exit....')
                os.system('clear')

            except Exception:
                pass
        elif choice == ("4"):
	         os.system("clear")
	         os.system("git clone https://github.com/KlumzyBish/Nuker")
	         os.system("cd Nuker && bash update.sh")

        elif choice == ("5"):
	         os.system("clear")
	         os.system("git clone https://github.com/HACK3RY2J/Anon-SMS")
	         os.system("cd Nuker && cd Anon-SMS && python3 Run.py")
			

        elif choice == ("6"):
	         os.system("clear")
	         os.system("git clone https://github.com/KlumzyBish/url-shortener")
	         os.system("cd url-shortener && bash short.sh")
			
			
			
			
        elif choice == ("7"):
            time.sleep(1)
            print("\n\t\033[32mFUCK\033[0m LIFE \033[34mBITCHHHH\033[0m\n")
            sys.exit()
        else:
            print("\033[1;33m[-] Invalid option!\033[1;m")




if __name__ == "__main__":
    nuker()
