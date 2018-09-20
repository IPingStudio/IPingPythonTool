'''
2018-09-19:创建类 实现功能
'''
import random
import math
import tkinter
class ScreenBall():
    def __init__(self, canvas, scrnWidth, scrnHeight, radios=40, velocity=2):
        '''
        创建球
        :param convans: 画板
        :param scrnWidth: 画板宽度
        :param scrnHeight: 画板高度
        :param radios: 半径
        :param velocity: 速度
        '''
        self.canvas = canvas
        self.posX = random.randint(int(radios) * 2, int(scrnWidth) - int(radios) * 5)
        self.posY = random.randint(int(radios) * 2, int(scrnHeight) - int(radios) * 5)
        self.scrnWidth = scrnWidth
        self.scrnHeight = scrnHeight
        self.radios = radios
        self.velocityX = random.randint(-int(velocity), int(velocity))
        self.velocityY = random.randint(-int(velocity), int(velocity))
        self.velocity = math.sqrt(math.pow(self.velocityX, 2) + math.pow(self.velocityY, 2))

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
        if self.posX + self.radios > self.scrnWidth or self.posX + self.radios < 100:
            self.velocityX *= -1
        if self.posY + self.radios > self.scrnHeight or self.posY + self.radios < 100:
            self.velocityY *= -1

        self.posX += self.velocityX
        self.posY += self.velocityY

        self.canvas.move(self.item, self.velocityX, self.velocityY)

    def changeDirection(self, directionPosX, directionPosY):
        if self.posX > directionPosX:
            self.velocityX = math.fabs(self.velocityX)
        elif self.posX < directionPosX:
            self.velocityX = -math.fabs(self.velocityX)
        if self.posY > directionPosY:
            self.velocityY = math.fabs(self.velocityY)
        elif self.posY < directionPosY:
            self.velocityY = -math.fabs(self.velocityY)