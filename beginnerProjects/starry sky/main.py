from turtle import *
from random import *
# bgcolor sets the background. hideturtle hides the arrow. speed 0 sets the drawing to be drawn faster
speed(0)
bgcolor("black")
hideturtle()
# these functions allow us to get the width and height of our screen, the round function allows us to have a whole number aka an integer
height=round(window_height()/2)
width=round(window_width()/2)

# function for drawing star
def draw_star(xpos,ypos):
    size=randrange(4,12)
    penup()
    goto(xpos,ypos)
    pendown()
    dot(size,"white")


for x in range(100):
    xpos=randrange(-width,width)
    ypos=randrange(-height,height)
    draw_star(xpos,ypos)
done()