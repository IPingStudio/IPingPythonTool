import tkinter
'''
游戏 蛇
'''
class Snake():
    def __init__(self, canvas, queue):
        self.queue = queue
        self.canvas = canvas
        self.is_gameOver = False
        self.is_eatting = False
        self.score = 0
        # 移动方向 "left", "right", "up", "down"
        self.moveDirection = "Right"
        self.bodyPosList = []
        self.bodyRadius = 10 # 蛇身半径
        self.moveSpeed = 10
        self.bodyNum = 10 #初始数量
        for i in range(self.bodyNum):
            if i == 0: # 蛇头
                self.posSnakeHead = (100, 100)
                self.bodyPosList.append(self.posSnakeHead)
            self.bodyPosList.append((100 - i*self.moveSpeed, 100))

        self._drawSnake()
    def _drawSnake(self):
        self.bodyList = []
        for i in self.bodyPosList:
            x1 = i[0] - self.bodyRadius
            y1 = i[1] - self.bodyRadius
            x2 = i[0] + self.bodyRadius
            y2 = i[1] + self.bodyRadius
            item = self.canvas.create_oval(x1, y1, x2, y2, fill="#FF0000", outline="#FF0000")
            self.bodyList.append(item)
        self.moveSnake()
    def moveSnake(self):
        '''
        让贪吃蛇动起来
        1、先确认当前移动方向，计算蛇头下一个位置
        2、整理蛇body位置列表
        3、每一个蛇身移动到上一个蛇身位置
        4、清理最后一个蛇身位置
        5、判断蛇头出界，游戏结束
        :return:
        '''
        if self.is_gameOver:
            return None
        if self.moveDirection == "Left":
            newposSnakeHead = (self.posSnakeHead[0] - self.moveSpeed, self.posSnakeHead[1])
        elif self.moveDirection == "Right":
            newposSnakeHead = (self.posSnakeHead[0] + self.moveSpeed, self.posSnakeHead[1])
        elif self.moveDirection == "Up":
            newposSnakeHead = (self.posSnakeHead[0], self.posSnakeHead[1] - self.moveSpeed)
        elif self.moveDirection == "Down":
            newposSnakeHead = (self.posSnakeHead[0], self.posSnakeHead[1] + self.moveSpeed)
        self.bodyPosList.insert(0, newposSnakeHead)
        # 移动至上一个蛇身位置
        for item in self.bodyList:
            _currentIndex = self.bodyList.index(item)
            chargeX = self.bodyPosList[_currentIndex][0] - self.bodyPosList[_currentIndex + 1][0]
            chargeY = self.bodyPosList[_currentIndex][1] - self.bodyPosList[_currentIndex + 1][1]
            self.canvas.move(item, chargeX, chargeY)
        self.posSnakeHead = newposSnakeHead
        # 吃到食物，增加蛇身长度
        if self.is_eatting:
            if self.score > 0:
                endItem = self.bodyPosList[len(self.bodyPosList) - 1]
                x1 = endItem[0] - self.bodyRadius
                y1 = endItem[1] - self.bodyRadius
                x2 = endItem[0] + self.bodyRadius
                y2 = endItem[1] + self.bodyRadius
                item = self.canvas.create_oval(x1, y1, x2, y2, fill="#FF0000", outline="#FF0000")
                self.bodyList.append(item)
                self.score -= 1
                # 减1之后 就会变成0
                if self.score == 0:
                    self.is_eatting = False
        else:
            self.bodyPosList.pop()

        # 蛇头出界，游戏结束
        if self.posSnakeHead[0] < 0 - self.bodyRadius or self.posSnakeHead[0] > 1024 - self.bodyRadius:
            self.is_gameOver = True
            self.queue.put({"game_over":True})
        elif self.posSnakeHead[1] < 0 - self.bodyRadius or self.posSnakeHead[1] > 768 - self.bodyRadius:
            self.is_gameOver = True
            self.queue.put({"game_over": True})

        self.canvas.after(100, self.moveSnake)

    def eatFood(self, score):
        self.is_eatting = True
        self.score = score




