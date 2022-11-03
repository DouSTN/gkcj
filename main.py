#!/usr/bin/python

import simplejson as json
import requests
import time


# 服务器地址
base_url = "http://dl.scs.gov.cn"
headers = {'Content-Type': 'application/json'}


#
# 获取配置
#
def get_config():
    try:
        data = requests.get(base_url + "/api/result/checkWritten/8a81f6d080ff71970182cddc44f10338.json?_=1667463783387").text
        return json.loads(data)
    except Exception as e:
        print(repr(e))
        return False


while 1:
    if get_config()['scoreTime'] == "0":
        print("当前时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("当前暂未公布成绩")
        print()
        time.sleep(3)

    if get_config()['scoreTime'] == "1":
        print("当前时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("当前已公布成绩")
        print()
        exit()
