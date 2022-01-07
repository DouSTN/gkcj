# gkcj
根据当前目录下的gk.json文件，查询是否发布国考成绩

关于json文件的获取，由于能力不够，我是通过crontab每隔5s自动wget实现的：
```shell
* * * * * sleep 5; /usr/bin/wget -q -O *json文件存放路径* http://dl.scs.gov.cn/api/result/checkWritten/8a81f3247b82076f017b95cb49ad002e.json?_=1641465022518
* * * * * sleep 10; /usr/bin/wget -q -O *json文件存放路径* http://dl.scs.gov.cn/api/result/checkWritten/8a81f3247b82076f017b95cb49ad002e.json?_=1641465022518
* * * * * sleep 15; /usr/bin/wget -q -O *json文件存放路径* http://dl.scs.gov.cn/api/result/checkWritten/8a81f3247b82076f017b95cb49ad002e.json?_=1641465022518
* * * * * sleep 20; /usr/bin/wget -q -O *json文件存放路径* http://dl.scs.gov.cn/api/result/checkWritten/8a81f3247b82076f017b95cb49ad002e.json?_=1641465022518
* * * * * sleep 25; /usr/bin/wget -q -O *json文件存放路径* http://dl.scs.gov.cn/api/result/checkWritten/8a81f3247b82076f017b95cb49ad002e.json?_=1641465022518
* * * * * sleep 30; /usr/bin/wget -q -O *json文件存放路径* http://dl.scs.gov.cn/api/result/checkWritten/8a81f3247b82076f017b95cb49ad002e.json?_=1641465022518
* * * * * sleep 35; /usr/bin/wget -q -O *json文件存放路径* http://dl.scs.gov.cn/api/result/checkWritten/8a81f3247b82076f017b95cb49ad002e.json?_=1641465022518
* * * * * sleep 40; /usr/bin/wget -q -O *json文件存放路径* http://dl.scs.gov.cn/api/result/checkWritten/8a81f3247b82076f017b95cb49ad002e.json?_=1641465022518
* * * * * sleep 45; /usr/bin/wget -q -O *json文件存放路径* http://dl.scs.gov.cn/api/result/checkWritten/8a81f3247b82076f017b95cb49ad002e.json?_=1641465022518
* * * * * sleep 50; /usr/bin/wget -q -O *json文件存放路径* http://dl.scs.gov.cn/api/result/checkWritten/8a81f3247b82076f017b95cb49ad002e.json?_=1641465022518
* * * * * sleep 55; /usr/bin/wget -q -O *json文件存放路径* http://dl.scs.gov.cn/api/result/checkWritten/8a81f3247b82076f017b95cb49ad002e.json?_=1641465022518
```
