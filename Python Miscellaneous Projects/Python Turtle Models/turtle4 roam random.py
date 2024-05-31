from turtle import Turtle
from turtle import Screen
import random

tim = Turtle()
screen = Screen()
screen.bgcolor("black")

tim.hideturtle()
tim.pensize(5)
tim.speed(9)
screen.colormode(255)
angles = [0,90,180,270]
while 1:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tim.pencolor(r,g,b)
    tim.forward(20)
    tim.setheading(random.choice(angles))
screen.exitonclick()

