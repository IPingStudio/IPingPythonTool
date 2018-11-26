from lxml import etree
import requests
import random
import os, time

from com.IPing.example.spider.tool.ReadProxyTxt import ReadProxyTxt

def getHTML(baseUrl):
    headers = {
        "Referer":"http://www.mzitu.com"
    }
    headers["User-Agent"] = random.choice(userAgents)
    req = requests.get(baseUrl, headers=headers)
    html = etree.HTML(req.text)
    return html

def getResponse(baseUrl):
    headers = {
        "Referer": "http://www.mzitu.com"
    }
    headers["User-Agent"] = random.choice(userAgents)
    proxy = random.choice(proxys)
    req = requests.get(baseUrl, headers=headers, proxies=proxy)
    return req

def mzitu_spider(baseUrl):
    html = getHTML(baseUrl)

    # 获取详情页信息
    img_src = html.xpath("//div[@class='postlist']/ul/li/a/@href")

    for img_url in img_src:
        img_parse(img_url)

def img_parse(img_url):
    html = getHTML(img_url)

    img_title = html.xpath("//div[@class='content']/h2/text()")[0]
    img_totalPage = html.xpath("//div[@class='pagenavi']/a/span/text()")[-2]

    for page in range(1, int(img_totalPage) + 1):
        # time.sleep(1)
        down_img(img_url + "/" + str(page), img_title)
    pass

def down_img(root_dir, title):
    html = getHTML(root_dir)

    img_scr = html.xpath("//div[@class='main-image']/p/a/img/@src")[0]

    res = getResponse(img_scr)

    #下载路径
    root_dir = "mzitu_img"
    #文件名
    img_name = img_scr.split("/")[-1]
    # 为了不必要的错误，清除空格
    title = title.replace(" ", "-")

    root_dir = root_dir + "/" + title
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)

    with open(root_dir + "/" + img_name, "wb") as f:
        f.write(res.content)
        print(title + "~~" + img_name + "保存成功~~")

if __name__ == '__main__':
    base_url = "https://www.mzitu.com/"
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
    proxys = ReadProxyTxt.read("proxy.txt")
    for i in range(1, 2):
        mzitu_spider(base_url + "page/{0}/".format(str(i)))