from turtle import Turtle,Screen
import random 

screen= Screen()
bet = screen.textinput(title='Make your bet\n',prompt='Which turtle will wn the race? Enter your choice : ')

screen.setup(width=1000,height=500)

color = ['red','orange','green','yellow','blue','purple']

# this function gives a value to run the turtle
def randommovement():
    value = int(random.randrange(0,10))
    return value


# alloting the name and color to each turtle that is being created
name = ['tim','tom','toy','top','tes','tqs']
y=-200
for a in range(0,6):
    print(name[a])
    name[a]=Turtle(shape='turtle')
    name[a].color(color[a])
    name[a].penup()
    name[a].goto(-450,y)
    y+=80

def check():
    for a in range(0,6):
        # print(a)
        if name[a].xcor() >= 400:
            print(color[a], "turtle won the game")
            if bet == color[a]:
                print("you won the bet ")
            else :
                print("you lost the bet ")
            return 0
        
while check() != 0:
        for a in range(0,6):
            name[a].forward(randommovement())
    # print(1)

screen.exitonclick()