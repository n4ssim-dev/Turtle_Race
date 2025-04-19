# Curseur qui bouge selon

import turtle

t = turtle.Turtle()
screen = turtle.Screen()
new_heading = t.heading() + 0

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def move_left():
    global new_heading
    new_heading = t.heading() - 10
    t.setheading(new_heading)

def move_right():
    global new_heading
    new_heading = t.heading() + 10
    t.setheading(new_heading)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.onkeypress(key="z", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="d", fun=move_left)
screen.onkeypress(key="q", fun=move_right)
screen.onkeypress(key="c", fun=clear)

screen.listen()

screen.exitonclick()
