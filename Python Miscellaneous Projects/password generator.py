#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("____________________________________________________________________\n")
print("Welcome to the PyPassword Generator!")
print("____________________________________________________________________\n")

num_letters= int(input("How many letters would you like in your password?\n")) 
num_numbers = int(input(f"How many numbers would you like?\n"))
num_symbols = int(input(f"How many symbols would you like?\n"))

#easy level  ___________________________________________________________________________


# password = ""
# for char in range(0,num_letters) :
#     rand = random.choice(letters)
#     password = password + rand

# # print(password)

# for nums in range(0,num_numbers):
#     rand1 = random.choice(numbers)
#     password = password + rand1

# # print(password)

# for syms in range(0,num_symbols):
#     rand2 = random.choice(symbols)
#     password = password + rand2


# print("____________________________________________________________________\n")
# print(password)


# hard level________________________________________________________________________________

password = []
for char in range(0,num_letters) :
    password.append(random.choice(letters))
    



for nums in range(0,num_numbers):
    password.append(random.choice(numbers))
    



for syms in range(0,num_symbols):
    password.append(random.choice(symbols))


# print(password)
random.shuffle(password)
# print(password)

password1 = ""
for char in password:
    password1 += char


print("____________________________________________________________________\n")

print(f"your random password is {password1}\n")

