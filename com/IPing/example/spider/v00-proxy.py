'''
爬去国内免费代理IP
2018-11-28：保存文件改为json
'''

import requests
import random
from lxml import etree
import os
import json

def getHTML(baseUrl):
    headers = {
        "Host":"www.xicidaili.com"
    }
    headers["User-Agent"] = random.choice(userAgents)
    res = requests.get(baseUrl, headers=headers)
    html = etree.HTML(res.text)
    return html

def writeFile(str):

    with open("proxy.json", "w") as f:
        f.write(str)

def detection(ipDic):
    detectionURL = "https://www.baidu.com"
    proxy = {}
    proxy[str(ipDic["httpType"])] = str(ipDic["ip"]) + ":" + str(ipDic["host"])
    res = requests.get(detectionURL, proxies=proxy)
    if res.status_code == 200:
        return True
    else:
        return False
def startSpider(baseUrl):
    HTML = getHTML(baseUrl)

    tr = HTML.xpath("//table[@id='ip_list']/tr")

    if os.path.exists("proxy.json"):
        os.remove("proxy.json")

    content = []
    for trItem in tr:
        if tr.index(trItem) == 0:
            continue
        ip = trItem[1].text
        host = trItem[2].text
        httpType = trItem[5].text
        writeDic = {"httpType":httpType, "ip":ip, "host":host}
        # 检测代理是否可用
        if detection(writeDic):
            content.append(writeDic)
    jsonObj = json.dumps(content)
    writeFile(jsonObj)


if __name__ == '__main__':
    baseUrl = "http://www.xicidaili.com/nn/1"
    userAgents = [
        "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19",
        "Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0",
        "Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19",
        "Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3",
        "Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3"
    ]
    startSpider(baseUrl)