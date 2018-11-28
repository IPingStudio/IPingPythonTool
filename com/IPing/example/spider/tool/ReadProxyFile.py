'''
读取并解析代理
2018-11-28：增加读取解析json文件功能
'''
import json
class ReadProxyFile():
    @staticmethod
    def readTxt(path):
        returnList = []
        with open(path, 'r') as f:
            ips = f.readlines()
        for ipStr in ips:
            tempList = ipStr.strip().split("\t")
            proxy = {}
            proxy[str(tempList[0])] = str(tempList[1] + ":" + tempList[2])
            returnList.append(proxy)
        return returnList

    @staticmethod
    def readJson(path):
        returnList = []
        with open(path, 'r') as f:
            ips = f.read()
            ipsJson = json.loads(ips)
        for ipDic in ipsJson:
            proxy = {}
            proxy[str(ipDic["httpType"])] = str(ipDic["ip"]) + ":" + str(ipDic["host"])
            returnList.append(proxy)
        return returnList


