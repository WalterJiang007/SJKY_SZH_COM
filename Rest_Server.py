#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/6/21 11:17
# @Author: JiangXingGang
# @File  : Rest_Server.py
import requests

import json

url = "https://LAPTOP-1LPMQ8UR:39320/iotgateway/read"

payload = json.dumps([
    "MNQSL.HS.Random1"
])
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)
# 格式化json文件
res_json = response.json()
print_json = json.dumps(res_json, sort_keys=True, indent=4, separators=(',', ': '))
print(print_json)
# 加载字典，遍历
response_dict = response.json()
for s1 in response_dict['readResults']:
    print(s1['id'])
    if s1['id'] == "MNQSL.HS.Random1":
        print(s1['t'])
        print(s1['v'])

