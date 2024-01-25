from turtle import *

hideturtle()
# global variables
diameter= 40
pop_diameter=100
# color changer
colors=["red","blue","green","orange"]
color_index=0

def draw_balloon():
    color(colors[color_index])
    dot(diameter)

def inflate_balloon():
    # global is a way to call on global parameters or variables in this case "diameter"
    global diameter, color_index
    diameter= diameter+10
    # pop_diameter isnt called using global because we are not creating a new variable with it
    if diameter>= pop_diameter:
        clear()
        diameter=40
        # we use this code to set up the next color index
        color_index = (color_index + 1) % len(colors)
        write("POP!!")
    draw_balloon()

draw_balloon()
# on key command takes a function and a key
onkey(inflate_balloon,"Up")
# listen is needed for python turtle to listen to a command. without it the onkey command wont work
listen()
done()