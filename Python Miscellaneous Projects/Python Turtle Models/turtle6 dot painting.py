from turtle import Turtle,Screen
import random

timmy = Turtle()
screen = Screen()
# screen.bgcolor("black")
screen.colormode(255)

timmy.shape("arrow")
timmy.color("red")
timmy.speed(100)

y=-350
while y != 400:

    timmy.penup()
    timmy.setposition(-700,y)
    timmy.pendown()
    
    for i in range(0,15):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        color = (r,g,b)
        timmy.dot(22,color)
        timmy.penup()
        timmy.forward(100)
        timmy.pendown()
        
    y=y+50

screen.exitonclick()

