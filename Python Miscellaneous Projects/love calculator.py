print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

a = name1.count("t")
b = name2.count("t")
c = name1.count("r")
d = name2.count("r")
e = name1.count("u")
f = name2.count("u")
g = name1.count("e")
h = name2.count("e")

final1 = a+b+c+d+e+f+g+h

a = name1.count("l")
b = name2.count("l")
c = name1.count("o")
d = name2.count("o")
e = name1.count("v")
f = name2.count("v")
g = name1.count("e")
h = name2.count("e") 

final2 = a+b+c+d+e+f+g+h

final = str(final1)+str(final2)

final = int(final)
 
if final < 10 or final > 90:
    print(f"Your score is {final}, you go together like coke and mentos.")

elif final > 40 and final < 50:
    print(f"Your score is {final}, you are alright together.")
    

else :
    print(f"Your score is {final}.")


