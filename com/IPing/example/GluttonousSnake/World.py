import tkinter
import queue
import math
from Food import Food
from Snake import Snake
class World():
    def chargeDirection(self, event):
        if self._snake.moveDirection == "Left":
            if event.keysym == "Right":
                self._snake.moveDirection = "Up"
            else:
                self._snake.moveDirection = "Down"
        elif self._snake.moveDirection == "Right":
            if event.keysym == "Right":
                self._snake.moveDirection = "Down"
            else:
                self._snake.moveDirection = "Up"
        elif self._snake.moveDirection == "Up":
            if event.keysym == "Right":
                self._snake.moveDirection = "Right"
            else:
                self._snake.moveDirection = "Left"
        elif self._snake.moveDirection == "Down":
            if event.keysym == "Right":
                self._snake.moveDirection = "Left"
            else:
                self._snake.moveDirection = "Right"

    def __init__(self, queue):
        self.queue = queue
        self.is_gameOver = False
        self.base = tkinter.Tk()
        self.base.geometry("1024x768")
        self.base.update()
        tempW = self.base.winfo_width()
        tempH = self.base.winfo_height()
        self.canvas =tkinter.Canvas(self.base, width=tempW, height=tempH)
        self.canvas.pack()

        self._food = Food(self.canvas)
        self._snake =Snake(self.canvas, self.queue)
        self.base.bind("<Key-Left>", self.chargeDirection)
        self.base.bind("<Key-Right>", self.chargeDirection)
        self.queue_handler()
        self.base.mainloop()

    def game_over(self):
        self.is_gameOver = True
        qb = tkinter.Button(self.base, text="退出", command=self.base.destroy)
        qb.pack()
        qbtn = tkinter.Button(self.base, text="重新开始", command=self.__init__)
        qbtn.pack()
    def verifyCollision(self):
        snakeHeadPos = self._snake.posSnakeHead
        foodPos = (self._food.posX, self._food.posY)
        snakeHeadRadius = self._snake.bodyRadius
        foodRadius = self._food.radius

        distanceX = snakeHeadPos[0] - foodPos[0]
        distanceY = snakeHeadPos[1] - foodPos[1]
        distancePos = math.sqrt(math.pow(distanceX, 2) + math.pow(distanceY, 2))
        if distancePos < snakeHeadRadius + foodRadius:
            self._snake.eatFood(1)
            self._food.newFood()
    def queue_handler(self):
        try:
            while True:
                self.verifyCollision()
                task = self.queue.get(block=False)
                if task.get("game_over"):
                    self.game_over()
        except queue.Empty:
            if not self.is_gameOver:
                self.canvas.after(10, self.queue_handler)
        except Exception as e:
            if not self.is_gameOver:
                self.canvas.after(10, self.queue_handler)

if __name__ == '__main__':
    q = queue.Queue()
    _world = World(q)
