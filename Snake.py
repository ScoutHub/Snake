from tkinter import *
from Apple import *
class Snake:
    def __init__(self, canva) -> None:
        self.snakeList = []
        self.coordX = 100
        self.coordY = 100
        self.size = 20
        self.firstSnake = canva.create_rectangle(self.coordX,self.coordY,self.coordX+self.size,self.coordY+self.size,outline='', fill="yellow")
        self.snakeList.append(self.firstSnake)
        self.dx = 10
        self.dy = 0

    # Function to move
    def move(self,canva):
        if(self.dx == 10):
            self.coordX+=10
            j=len(self.snakeList)-1
            while(j>=0):
                if(j==0):
                    canva.coords(self.firstSnake,self.coordX,self.coordY,self.coordX+self.size,self.coordY+self.size)
                else:
                    canva.coords(self.snakeList[j],canva.coords(self.snakeList[j-1])[0],canva.coords(self.snakeList[j-1])[1],canva.coords(self.snakeList[j-1])[2],canva.coords(self.snakeList[j-1])[3])
                j-=1

        if(self.dx == -10):
            self.coordX-=10
            j=len(self.snakeList)-1
            while(j>=0):
                if(j==0):
                    canva.coords(self.firstSnake,self.coordX,self.coordY,self.coordX+self.size,self.coordY+self.size)
                else:
                    canva.coords(self.snakeList[j],canva.coords(self.snakeList[j-1])[0],canva.coords(self.snakeList[j-1])[1],canva.coords(self.snakeList[j-1])[2],canva.coords(self.snakeList[j-1])[3])
                j-=1

        if(self.dy == 10):
            self.coordY+=10
            j=len(self.snakeList)-1
            while(j>=0):
                if(j==0):
                    canva.coords(self.firstSnake,self.coordX,self.coordY,self.coordX+self.size,self.coordY+self.size)
                else:
                    canva.coords(self.snakeList[j],canva.coords(self.snakeList[j-1])[0],canva.coords(self.snakeList[j-1])[1],canva.coords(self.snakeList[j-1])[2],canva.coords(self.snakeList[j-1])[3])
                j-=1

        if(self.dy == -10):
            self.coordY-=10
            j=len(self.snakeList)-1
            while(j>=0):
                if(j==0):
                    canva.coords(self.firstSnake,self.coordX,self.coordY,self.coordX+self.size,self.coordY+self.size)
                else:
                    canva.coords(self.snakeList[j],canva.coords(self.snakeList[j-1])[0],canva.coords(self.snakeList[j-1])[1],canva.coords(self.snakeList[j-1])[2],canva.coords(self.snakeList[j-1])[3])
                j-=1

        # When it overflow from right
        if(canva.coords(self.firstSnake)[2] > 320):
            self.coordX=-20
            canva.coords(self.firstSnake,self.coordX,self.coordY,self.coordX+self.size,self.coordY)
        # From bottom
        elif(canva.coords(self.firstSnake)[3] > 320):
            self.coordY=-20
            canva.coords(self.firstSnake,self.coordX,self.coordY,self.coordX,self.coordY+self.size)
        # From left
        elif(canva.coords(self.firstSnake)[0] < -20):
            self.coordX=310
            canva.coords(self.firstSnake,self.coordX,self.coordY,self.coordX+self.size,self.coordY)
        # From top
        elif(canva.coords(self.firstSnake)[1] < -20):
            self.coordY=310
            canva.coords(self.firstSnake,self.coordX,self.coordY,self.coordX,self.coordY+self.size)

    # Function to change direction
    def changeDirection(self,e):
        if(e.keysym == "Up" and (self.dy != 10) ):
            self.dx,self.dy=0,-10
        elif(e.keysym == "Right" and (self.dx != -10) ):
            self.dx,self.dy=10,0
        elif(e.keysym == "Down" and (self.dy != -10) ):
            self.dx,self.dy=0,10
        elif(e.keysym == "Left" and (self.dx != 10) ):
            self.dx,self.dy=-10,0

    # Function when snake eat
    def eat(self,canva,apple):
        j = len(self.snakeList)-1
        if((self.coordX==apple.x0)and(self.coordY==apple.y0)):
            #print("ate")
            apple.newApple(canva)
            self.snakeList.append(canva.create_rectangle(canva.coords(self.snakeList[j-1])[0],canva.coords(self.snakeList[j-1])[1],canva.coords(self.snakeList[j-1])[2],canva.coords(self.snakeList[j-1])[3],outline='', fill="green"))