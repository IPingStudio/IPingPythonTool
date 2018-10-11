'''
包含所有排序函数
2018-09-14：
    1、创建
    2、创建冒泡排序
2018-09-17:
    1、添加执行次数显示
    2、创建鸡尾酒排序
'''

class Sort():
    '''
    所有排序算法集
    '''
    @staticmethod
    def bubbleSort(currentList, sortType):
        '''
        冒泡排序
            平均情况：O（n平方）、最好情况：O（n）、最差情况：O（n平方)
        :param currentList: 当前需要排序的序列
        :param sortType: 是正序还是倒序
                            正序：1
                            倒序：2
        :return: 排序后的序列
        '''
        if [1, 2].count(sortType) <= 0:
            print("异常：sortType超出范围", sortType, "\n正序：1\n倒叙：2")
            return None

        print("*" * 5, "冒泡排序", "*" * 5)
        print("原始序列：", currentList)

        listLen = len(currentList)
        swapNum = 0
        for x in range(0, listLen):
            # 防止index(y + 1)溢出,所以要listLen-x-1
            for y in range(0, listLen - x - 1):
                if sortType == 1:
                    swapNum += 1
                    if currentList[y] > currentList[y + 1]:
                        currentList[y], currentList[y + 1] = currentList[y + 1], currentList[y]
                elif sortType == 2:
                    swapNum += 1
                    if currentList[y] < currentList[y + 1]:
                        currentList[y], currentList[y + 1] = currentList[y + 1], currentList[y]
        print("交换执行次数：", swapNum)
        print("排序后序列：", currentList)
        return currentList

    @staticmethod
    def cocktailSort(currentList, sortType):
        '''
        鸡尾酒排序：冒泡排序的改进版
        :param currentList: 当前需要排序的序列
        :param sortType: 是正序还是倒序
                            正序：1
                            倒序：2
        :return: 排序后的序列
        '''
        if [1, 2].count(sortType) <= 0:
            print("异常：sortType超出范围", sortType, "\n正序：1\n倒叙：2")
            return None

        print("*" * 5, "冒泡排序改进：鸡尾酒排序", "*" * 5)
        print("原始序列：", currentList)

        listLen = len(currentList)
        swapNum = 0
        start = 0
        end = listLen

        while start < end:
            for i in range(start, end - 1):
                if sortType == 1:
                    swapNum += 1
                    if currentList[i] > currentList[i + 1]:
                        currentList[i], currentList[i + 1] = currentList[i + 1], currentList[i]
                elif sortType == 2:
                    swapNum += 1
                    if currentList[i] < currentList[i + 1]:
                        currentList[i], currentList[i + 1] = currentList[i + 1], currentList[i]
            end -= 1

            for i in range(end - 1, start, -1):
                if sortType == 1:
                    swapNum += 1
                    if currentList[i] < currentList[i - 1]:
                        currentList[i], currentList[i - 1] = currentList[i - 1], currentList[i]
                elif sortType == 2:
                    swapNum += 1
                    if currentList[i] > currentList[i - 1]:
                        currentList[i], currentList[i - 1] = currentList[i - 1], currentList[i]
            start += 1
        print("交换执行次数：", swapNum)
        print("排序后序列：", currentList)
        return currentList

    @staticmethod
    def selectionSort(currentList, sortType):
        '''
        选择排序
            平均情况：O（n平方）、最好情况：O（n平方）、最差情况：O（n平方)
        :param currentList: 当前需要排序的序列
        :param sortType: 是正序还是倒序
                            正序：1
                            倒序：2
        :return: 排序后的序列
        '''
        if [1, 2].count(sortType) <= 0:
            print("异常：sortType超出范围", sortType, "\n正序：1\n倒叙：2")
            return None

        print("*" * 5, "选择排序", "*" * 5)
        print("原始序列：", currentList)

        swapNum = 0
        listLen = len(currentList)
        for i in range(0, listLen - 2):
            min = i
            for j in range(i + 1, listLen - 1):
                tListI = currentList[i]
                tListJ = currentList[j]
                swapNum += 1
                if currentList[min] > currentList[j]:
                    min = j
            if min != i:
                currentList[i], currentList[min] = currentList[min], currentList[i]
        print("交换执行次数：", swapNum)
        print("排序后序列：", currentList)
        return currentList
# demo
if __name__ == "__main__":
    # 冒泡demo
    # l = [1, 35, 23, 7, 5, 45, 23, 4, 34, 1111, 34]
    # Sort.bubbleSort(l , 2)
    #
    # # 鸡尾酒demo
    # l = [1, 35, 23, 7, 5, 45, 23, 4, 34, 1111, 34]
    # Sort.cocktailSort(l, 1)

    # 选择排序demo
    # l = [1, 35, 23, 7, 5, 45, 23, 4, 34, 1111, 34]
    # Sort.selectionSort(l, 1)
    pass