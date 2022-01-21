from tkinter import *
from random import *

class Apple:
    def __init__(self,canva) -> None:
        self.tabOfCord=[20,40,60,80,100,120,140,160,180,200,220,240,260,280]
        self.x0 = self.tabOfCord[randint(0,len(self.tabOfCord)-1)]
        self.y0 = self.tabOfCord[randint(0,len(self.tabOfCord)-1)]
        self.x1 = self.x0 + 20
        self.y1 = self.y0 + 20
        self.firstApple = canva.create_rectangle(self.x0,self.y0,self.x1,self.y1,outline='', fill="red")
    
    def newApple(self,canva):
        canva.delete(self.firstApple)
        self.x0 = self.tabOfCord[randint(0,len(self.tabOfCord)-1)]
        self.y0 = self.tabOfCord[randint(0,len(self.tabOfCord)-1)]
        self.x1 = self.x0 + 20
        self.y1 = self.y0 + 20
        self.firstApple = canva.create_rectangle(self.x0,self.y0,self.x1,self.y1,outline='', fill="red")
