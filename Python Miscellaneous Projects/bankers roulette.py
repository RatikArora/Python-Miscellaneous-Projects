import random 
names_str = input("Give me everybody's names, separated by a comma. ")
names = names_str.split(", ")
# print(names)
x = int(len(names))
# print(x)
a = int(random.randint(0,x-1))
print(f"{names[a]} is going to buy the meal today!")