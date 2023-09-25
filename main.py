from turtle import Turtle, Screen
import random

my_scr = Screen()
my_scr.setup(500, 400)
user_bet = my_scr.textinput("На кого ставишь?", "Красная, синяя, желтая и т.д.").lower()
colors = ["red", "green", "blue", "purple", "orange", "violet"]
a = 0
is_race_on = False
turtles = []

for item in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.pen(pendown=False, fillcolor=colors[a])
    new_turtle.goto(x=-my_scr.canvwidth / 2, y=-my_scr.canvheight / 2 + a * 62)
    a += 1
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(0, 5)
        turtle.forward(rand_distance)
        if turtle.xcor() > int(my_scr.canvwidth/2 + 20):
            is_race_on = False
            if turtle.fillcolor() == user_bet:
                print(f"Ты выиграл! Цвет черепахи - {turtle.fillcolor()}")
            else:
                print(f"Ты проиграл, а выиграла вот эта черепаха - {turtle.fillcolor()}")


my_scr.exitonclick()
