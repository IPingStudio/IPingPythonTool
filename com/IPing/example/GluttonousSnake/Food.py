import tkinter
import random
'''
游戏食物
'''
class Food():
    def __init__(self, canvas):
        self.canvas = canvas
        self.radius = 10 # 半径

        self.__drawFood()
    def __drawFood(self):
        self.posX = random.randrange( 50, 1024 - 50, self.radius * 2)
        self.posY = random.randrange( 50, 768 - 50, self.radius * 2)
        x1 = self.posX - self.radius
        y1 = self.posY - self.radius
        x2 = self.posX + self.radius
        y2 = self.posY + self.radius
        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill="#0000FF", outline="#0000FF")

    def newFood(self):
        newX = random.randrange( 50, 1024 - 50, self.radius * 2)
        newY = random.randrange( 50, 768 - 50, self.radius * 2)
        chargeX = newX - self.posX
        chargeY = newY - self.posY
        self.canvas.move(self.item, chargeX, chargeY)
        self.posX = newX
        self.posY = newY
