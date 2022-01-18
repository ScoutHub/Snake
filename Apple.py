from tkinter import *
from random import *

class Apple:
    def __init__(self,canva) -> None:
        self.tabOfCord=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280]
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
