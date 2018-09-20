'''
2018-09-19:创建类 实现功能
'''
from com.IPing.example.screenSaver.ScreenBall import ScreenBall
import random
import tkinter
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

        self.canvas.after(200, self.runScreenSaver)
    def closeScreenSaver(self, e):
        self.root.destroy()

if __name__ == '__main__':
    ScreenSaver()
    pass