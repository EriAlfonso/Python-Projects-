from turtle import *
speed(0)

move_distance=20
# drawing the background and sea
bgcolor("orange")

penup()
goto(100,500)
pendown()
color("blue")
begin_fill()
goto(500,500)
goto(500,-500)
goto(100,-500)
goto(100,500)
end_fill()

# setting up the turtle character
penup()
goto(-200,0)
color("green")
shape("turtle")

# movement functions

def move_up():
    setheading(90)
    forward(move_distance)
    check_goal()


def move_down():
    setheading(270)
    forward(move_distance)
    check_goal()

def move_left():
    setheading(180)
    forward(move_distance)
    check_goal()

def move_right():
    setheading(0)
    forward(move_distance)
    check_goal()


# function to check if we reached the beach/goal and making it impossible to keep moving, xcor looks for a coordinate in the x axis 
def check_goal():
    if xcor() > 100:
        hideturtle()
        color("white")
        write ("YOU WIN!!", align="center", font=("Arial", 22, "normal"))
        onkey(None,"Up")
        onkey(None,"Down")
        onkey(None,"Left")
        onkey(None,"Right")

# link functions to keys
onkey(move_up,"Up")
onkey(move_down,"Down")
onkey(move_left,"Left")
onkey(move_right,"Right")

listen()
done()