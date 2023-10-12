import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color (red, yellow, green, blue, or purple): ")
colors = ['red', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

x_coord = -230
y_coord = -70
position = 1
name = 'turtle' + str(position)

for color in colors:
    name = Turtle(shape='turtle')
    name.penup()
    name.color(color)
    name.goto(x=x_coord, y=y_coord)
    y_coord += 30
    position += 1
    all_turtles.append(name)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle was the winner1")
            else:
                print(f"You've lost! The {winning_color} turtle was the winner!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()