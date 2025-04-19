# 6 tortues se positionnent sur une ligne en x:-230, vous devez parier sur celle qui gagnera la course !

import turtle
import random

colors = ("red","orange","yellow","green","blue","purple")
turtles = []
height = -110
is_race_on = False

screen = turtle.Screen()
screen.setup(width=500,height=400)

for color in colors:
    t = turtle.Turtle(shape="turtle")
    t.penup()
    t.color(color)
    t.goto(x=-230,y=height)
    height += 45
    turtles.append(t)

user_bet = screen.textinput(title="Place your bet",prompt=f"Which turtle wins the race ? Enter a color {colors}:").lower()

if user_bet:
    is_race_on = True

while is_race_on:
    for tortoise in turtles:
        tortoise.forward(random.randint(0, 10))
        if tortoise.xcor() >= 230:
            if tortoise.pencolor() != user_bet:
                turtle.write(f"The winner is : {tortoise.pencolor()} !\nYour bet was {user_bet}, you lost...",align="center",font=("Arial", 22, "normal"))
            elif tortoise.pencolor() == user_bet:
                turtle.write(f"The winner is : {tortoise.pencolor()} !\nYour bet was {user_bet}, you won !",align="center",font=("Arial", 22, "normal"))
            is_race_on =False


screen.listen()
screen.exitonclick()