print("***Welcome to the tip calculator***")
bill = int(input("What is he amount of the bill? \n$"))
tip = int(input("What is the percentage of tip you wanna include? \n"))
split = int(input("how many people are you ? \n"))
bill = bill + bill*(tip/100)
bill = bill / split
bill = float(round(bill,2))
bill = "{:.2f}".format(bill) #to make decimal till 2 places even after you get omly one after it 
print(f"Each person should pay \n${bill} ")


