from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def forward():
    tim.forward(10)

def backward():
    tim.backward(10)

def right():
    tim.right(5)

def left():
    tim.left(5)

def clear():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()

screen.listen()
screen.onkeypress(key='w',fun=forward)
screen.onkeypress(key='s',fun=backward)
screen.onkeypress(key='a',fun=left)
screen.onkeypress(key='d',fun=right)
screen.onkey(key='c',fun=clear)

screen.exitonclick()