'''
这是一个具有翻译功能的程序
通过Spider功能获取网站上翻译结果
鸣谢：百度翻译
'''

from urllib import request, parse
import tkinter
import json
class Translate():
    def __init__(self):
        self.spiderInit()

        self.stageBase = tkinter.Tk()
        self.stageBase.wm_title("简单翻译器")
        self.stageBase.geometry("500x400")
        self.inputLabel = tkinter.Label(self.stageBase, text="请输入要翻译的英文：")
        self.inputLabel.pack()
        self.inputText = tkinter.Entry(self.stageBase, width=200)
        self.inputText.pack()
        self.inputText.bind("<Key>", self.changeRsult)
        self.resultLabel = tkinter.Label(self.stageBase, text="翻译结果：")
        self.resultLabel.pack()
        self.resultText = tkinter.Listbox(self.stageBase, width=200)
        self.resultText.pack()
        self.stageBase.mainloop()

    def spiderInit(self):
        self.url = "https://fanyi.baidu.com/sug"



    def changeRsult(self, *args):
        self.resultText.delete(0, "end")
        data = {
            "kw": self.inputText.get()
        }

        data = parse.urlencode(data)
        data = data.encode()

        req = request.Request(url=self.url, data=data)

        self.rsq = request.urlopen(req)

        html = self.rsq.read().decode()

        # print(html)
        num = 0
        tempStr = ""
        jsonData = json.loads(html)
        for item in jsonData["data"]:
            for key, value in item.items():
                num += 1
                if num % 2 == 1:
                    tempStr = value
                else:
                    tempStr = tempStr + "-------" + str(value)
                    self.resultText.insert("end", tempStr)
                    tempStr = ""
if __name__ == '__main__':
    _translater = Translate()