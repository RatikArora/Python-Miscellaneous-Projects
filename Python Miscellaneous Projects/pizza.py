# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
cost = 0
if size == 'S':
    cost = 15 
    if add_pepperoni == 'Y':
        cost = cost + 2
if size == 'M':
    cost = 20
if size == 'L' :
    cost = 25
if size == 'M' or 'L' and add_pepperoni == 'Y':
    cost = cost + 3

if extra_cheese == 'Y':
    cost = cost + 1

print(f"Your final bill is : ${cost}")
