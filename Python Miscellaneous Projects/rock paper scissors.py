import random 
print("___________________________________________________\n")
print("Welcome to the rock paper scissors game!")
print("___________________________________________________\n")

mine = int(input("What would you like to choose rock(0), paper(1), scissors(2)\n"))
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''


scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock,paper,scissors]



print("you chose")
if mine == 0 : print(rock)
elif mine == 1 : print(paper)
elif mine == 2 : print(scissors)

print("computer chose")
comp = random.randint(0,2)
# print(comp)
print(images[comp])


print("___________________________________________________")

if mine == comp:
    print("its a draw")
else :
    if comp == 0:
        if mine == 1:
            print("you won")
        else :
            print("you lost")

    elif comp == 1:
        if mine == 0:
            print("you lost")
        else : 
            print("you won")

    elif comp == 2:
        if mine == 0:
            print("you won")
        else :
            print("you lost")










