'''
包含所有排序函数
2018-09-14：
    1、创建
    2、创建冒泡排序
'''

class Sort():

    '''
    冒泡排序
    currentList: 需要排序的序列
    sortType: 是正序还是倒序
        正序：1
        倒序：2
    '''
    @staticmethod
    def bubbleSort(currentList, sortType):
        if [1, 2].count(sortType) <= 0:
            print("异常：sortType超出范围", sortType, "\n正序：1\n倒叙：2")
            return None

        print("冒泡排序")
        print("原始序列：", currentList)

        listLen = len(currentList)
        for x in range(0, listLen):
            # 防止index(y + 1)溢出,所以要listLen-x-1
            for y in range(0, listLen - x - 1):
                if sortType == 1:
                    if currentList[y] > currentList[y + 1]:
                        currentList[y], currentList[y + 1] = currentList[y + 1], currentList[y]
                elif sortType == 2:
                    if currentList[y] < currentList[y + 1]:
                        currentList[y], currentList[y + 1] = currentList[y + 1], currentList[y]
        return currentList

    @staticmethod
    def cocktailSort(currentList, sortType):
        if [1, 2].count(sortType) <= 0:
            print("异常：sortType超出范围", sortType, "\n正序：1\n倒叙：2")
            return None

        print("冒泡排序改进：鸡尾酒排序")
        print("原始序列：", currentList)

        listLen = len(currentList)
        start = 0
        end = listLen
        for x in range(start, end):
            pass
# demo
if __name__ == "__main__":
    l = [1, 35, 23, 7, 5, 45, 23, 4, 34, 1111, 34]
    newL = Sort.bubbleSort(l , 2)

    print(newL)