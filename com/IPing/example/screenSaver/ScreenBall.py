'''
2018-09-19:创建类 实现功能
'''
import random
import tkinter
class ScreenBall():
    def __init__(self, canvas, scrnWidth, scrnHeight, radios=20, velocity=10):
        '''
        创建球
        :param convans: 画板
        :param scrnWidth: 画板宽度
        :param scrnHeight: 画板高度
        :param radios: 半径
        :param velocity: 速度
        '''
        self.canvas = canvas
        self.posX = random.randint(int(radios), int(scrnWidth) - int(radios))
        self.posY = random.randint(int(radios), int(scrnWidth) - int(radios))
        self.scrnWidth = scrnWidth
        self.scrnHeight = scrnHeight
        self.radios = radios
        self.velocityX = random.randint(-int(velocity), int(velocity))
        self.velocityY = random.randint(-int(velocity), int(velocity))

        self.drawBall()
    def drawBall(self):
        '''
        初始化
        :return:
        '''
        c = lambda: random.randint(0, 255)
        self.color = '#%02x%02x%02x'%(c(), c(), c())

        x1 = self.posX - self.radios
        y1 = self.posY - self.radios
        x2 = self.posX + self.radios
        y2 = self.posY + self.radios

        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def moveBall(self):
        '''
        移动球
        :return:
        '''
        if self.posX + self.radios > self.scrnWidth or self.posX + self.radios < 0:
            self.velocityX *= -1
        if self.posY + self.radios > self.scrnHeight or self.posY + self.radios < 0:
            self.velocityY *= -1

        self.posX += self.velocityX
        self.posY += self.velocityY

        self.canvas.move(self.item, self.velocityX, self.velocityY)
        pass