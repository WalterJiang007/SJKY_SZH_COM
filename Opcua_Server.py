#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/4/2 13:25
# @Author: JiangXingGang
# @File  : Opcua_Server.py
from opcua import Server
from random import randint
import datetime
import time

server = Server()

url = "opc.tcp://127.0.0.1:4840"
server.set_endpoint(url)

name = "OPC_SIMULATION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace, "Parameters")

Temp = Param.add_variable(addspace, "Temperature", 0)
Press = Param.add_variable(addspace, "Pressure", 0)
Time = Param.add_variable(addspace, "Time", 0)
yu = Param.add_variable(addspace, "大家好", 0)

yu.set_writable()
Temp.set_writable()
Press.set_writable()
Time.set_writable()

server.start()
print("Server started at {}".format(url))

while True:
    Temperature = randint(10,50)
    Pressure = randint(200, 999)
    TIME = datetime.datetime.now()
    大家好 = randint(10,50)
    print(Temperature, Pressure, TIME)

    Temp.set_value(Temperature)
    Press.set_value(Pressure)

    Time.set_value(TIME)
    yu.set_value(大家好)
    time.sleep(2)
