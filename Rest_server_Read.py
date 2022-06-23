#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/6/21 13:20
# @Author: JiangXingGang
# @File  : Rest_server_Read.py
import json

import requests

url = "https://LAPTOP-1LPMQ8UR:39320/iotgateway/read?ids=MNQSL.HS.Random1&ids=MNQSL.HS.Random2"

payload = {}
headers = {}
# GET 方法 可以同时读取多个tag，post 只能读取1个
response = requests.request("GET", url, headers=headers, data=payload, verify=False)
res_json = response.json()
print_json = json.dumps(res_json, sort_keys=True, indent=4, separators=(',', ': '))
print(print_json)

response_dict = response.json()
for s1 in response_dict['readResults']:
    print(s1['t'], s1['v'], s1['id'])
    # if s1['id'] == "MNQSL.HS.Random1":
    #     print(s1['t'], s1['v'], s1['id'])
    # if s1['id'] == "MNQSL.HS.Random2":
    #     print(s1['t'], s1['v'], s1['id'])
