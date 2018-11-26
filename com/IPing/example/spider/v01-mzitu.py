from lxml import etree
import requests
import random
import os, time

def getHTML(baseUrl):
    headers = dict()
    headers["User-Agent"] = random.sample(userAgents, 1)
    req = requests.get(baseUrl, headers)
    html = etree.HTML(req.text)
    return html

def getResponse(baseUrl):
    headers = dict()
    headers["User-Agent"] = random.sample(userAgents, 1)
    req = requests.get(baseUrl, headers)
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
        time.sleep(1)
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

    userAgents = ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
                  "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
                  "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
                  "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
                  "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
                  "User-Agent:Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
                  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"]

    for i in range(1, 2):
        mzitu_spider(base_url + "page/{0}/".format(str(i)))