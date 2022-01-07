#!/usr/bin/python
#修改 *json文件存放绝对路径* 和 *短信发送脚本存放绝对路径* 即可使用

import simplejson as json
import os
import time

with open('*json文件存放绝对路径*','r',encoding='utf8')as fp:
    json_data = json.load(fp)

ti = {'scoreTime':'0'}

while json_data == ti:
    time.sleep(5)
    with open('*json文件存放绝对路径*', 'r', encoding='utf8') as fp:
        json_data = json.load(fp)
    print ("当前时间：%s" % time.ctime())
    print ('还未检测到国考成绩发布')
    print (' ')


print('国考成绩已发布，正在发送短信通知！')
os.system('/usr/bin/python *短信发送脚本存放绝对路径*')
time.sleep(7200)
