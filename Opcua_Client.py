# -*- coding:utf-8 -*-
# @Time  : 2022/3/30 16:07
# @Author: JiangXingGang
# @File  : opcua-client.py
import opcua.ua
import threading
import time
from opcua import Client

client = Client("opc.tcp://10.4.20.89:49320")


try:

    client.connect()
    while True:
        sa = client.get_node('ns=2;s=SWBZ_2_PLC_1.SWBZ_2_PLC_1._System._SecondsInError')
        sa1 = sa.get_value()
        print(sa1)
        time.sleep(0.5)

    # va = client.get_node('ns=2;s=分拣.分拣PLC.箱码')
    # T = va.get_value()
    # print(T)
    # va.set_value(opcua.ua.DataValue(opcua.ua.Variant('2003020402698-220329003446-220412111812010-X0100-136786065-B5401046-100/10-100-206-N-D', opcua.ua.VariantType.String)))
    # print(va.get_value())
    # while True:
    #     va2 = client.get_node('ns=2;s=分拣.分拣PLC.ERP箱码')
    #     T2 = va2.get_value()
    #     print(T2)
    #     va2.set_value(opcua.ua.DataValue(opcua.ua.Variant(va.get_value(), opcua.ua.VariantType.String)))
    #     print(va2.get_value())

#  va1 = client.get_node('ns=2;s=分拣.分拣PLC.ERP应答')
#  T1 = va1.get_value()
#  print(T1)
#  # va.set_value(opcua.ua.DataValue(opcua.ua.Variant(, opcua.ua.VariantType.String)))
#  va1.set_value(opcua.ua.DataValue(opcua.ua.Variant(1, opcua.ua.VariantType.UInt16)))
#  print(va1.get_value())

except Exception as e:
    print(e)
finally:
    client.disconnect()
