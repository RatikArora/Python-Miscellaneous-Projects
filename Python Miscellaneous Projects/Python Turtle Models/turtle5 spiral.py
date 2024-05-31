from turtle import Turtle,Screen
import random

tim = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.colormode(255)
tim.speed(100)

# angle3= 10
# for i in range(int(360/angle3)):
#     # r = random.randint(0,255)
#     # g = random.randint(0,255)
#     # b = random.randint(0,255)
#     # tim.pencolor(r,g,b)
#     tim.pencolor('white')
#     tim.circle(100)
#     tim.right(angle3)

# angle2 = 8
# for i in range(int(360/angle2)):
#     # r = random.randint(0,255)
#     # g = random.randint(0,255)
#     # b = random.randint(0,255)
#     # tim.pencolor(r,g,b)
#     tim.pencolor('white')
#     tim.circle(150)
#     tim.right(angle2)

angle = 4
for i in range(int(360/angle)):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tim.pencolor(r,g,b)
    
    # tim.pencolor('white')
    tim.circle(200)
    tim.right(angle)
 
screen.exitonclick()