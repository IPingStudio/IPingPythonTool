
class ReadProxyTxt():
    @staticmethod
    def read(path):
        returnList = []
        with open(path, 'r') as f:
            ips = f.readlines()
        for ipStr in ips:
            tempList = ipStr.strip().split("\t")
            proxy = {}
            proxy[str(tempList[0])] = str(tempList[1] + ":" + tempList[2])
            returnList.append(proxy)
        return returnList