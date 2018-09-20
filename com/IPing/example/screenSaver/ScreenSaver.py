'''
2018-09-19:创建类 实现功能
2018-09-20:
    1、实现屏保功能
    2、使小球碰撞改变x，y的移动方向
    3、修改更新频率、速度 使运动更圆润
'''
from com.IPing.example.screenSaver.ScreenBall import ScreenBall
import random
import tkinter
import math
class ScreenSaver():
    '''
        屏幕保护系统
    '''
    ballNum = 30
    ballList = []
    def __init__(self):
        self.root = tkinter.Tk()
        # 取消边框
        self.root.overrideredirect(1)
        # 鼠标移动退出屏保
        self.root.bind('<Motion>', self.closeScreenSaver)
        # 获取屏幕宽高
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        # 创建画布 归属、规格
        self.canvas = tkinter.Canvas(self.root, width=w, height=h)
        self.canvas.pack()

        for i in range(self.ballNum):
            tempBall = ScreenBall(self.canvas, w, h)
            self.ballList.append(tempBall)

        self.runScreenSaver()
        self.root.mainloop()

    def runScreenSaver(self):
        for ball in self.ballList:
            ball.moveBall()
            for crash in self.ballList:
                if ball != crash:
                    distanceX = math.pow(int(ball.posX) - int(crash.posX), 2)
                    distanceY = math.pow(int(ball.posY) - int(crash.posY), 2)
                    if  math.sqrt(distanceX + distanceY) < ball.radios + crash.radios:
                        ball.changeDirection(crash.posX, crash.posY)
                        crash.changeDirection(ball.posX, ball.posY)
        ballPosDic = self.getBallPos(self.ballList)


        self.canvas.after(10, self.runScreenSaver)

    def getBallPos(self, list):
        returnList = []
        for item in list:
            tempDic = {"pos":[item.posX, item.posY], "radios":item.radios}
            returnList.append(tempDic)
        return returnList
    def closeScreenSaver(self, e):
        self.root.destroy()

if __name__ == '__main__':
    ScreenSaver()
    pass