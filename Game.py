from tkinter import *  
from random import *
from Snake import Snake
from Apple import Apple
WINDOWS_WIDTH = 300
WINDOWS_HEIGHT = 300

# Root windows
root = Tk()
root['bg']="black"
root.title("Snake")
root.geometry("+500+100")

# Play area
canvaJeu = Canvas(root,width=WINDOWS_WIDTH,height=WINDOWS_HEIGHT)
canvaJeu['bg']="black"
canvaJeu.pack()

# Variables initialization

snake = Snake(canvaJeu)
apple = Apple(canvaJeu)


# Play fonction
def play():
    snake.move(canvaJeu)
    snake.eat(canvaJeu,apple)
    root.after(80,play) # Speed of game, actually 80ms

def moveWithKey(e):
    snake.changeDirection(e)

# Main functions

play()
root.bind("<KeyPress>", moveWithKey)
root.mainloop()