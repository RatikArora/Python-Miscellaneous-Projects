menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report(dict):
    for key, value in dict.items():
        print(key, " : ", value)
    return 0 

def latte():
    if resources["water"] < menu['latte']['ingredients']['water']:
        print('not enought water')
        return

    elif resources["coffee"] < menu['latte']['ingredients']['coffee']:
        print('not enought coffee')
        return

    elif resources["milk"] < menu['latte']['ingredients']['milk']:
        print('not enought milk')
        return
    else:

        resources["water"] = resources["water"] - \
            menu['latte']['ingredients']['water']
        resources["coffee"] = resources["coffee"] - \
            menu['latte']['ingredients']['coffee']
        resources["milk"] = resources["milk"] - \
            menu['latte']['ingredients']['milk']
        print('your latte is ready')
        # return resources

def coins(menu,choice):
    # penny = 0.01
    # dime = 0.10
    # nickel = 0.05
    # quarter = 0.25
    print("\n----<< Enter the Coins >>----")
    penny = int(input("enter the number of pennies : "))
    nickel = int(input("enter the number of nickels : "))
    dime = int(input("enter the number of dimes : "))
    quarter = int(input("enter the number of quarters : "))
    total = penny*0.01 + nickel*0.05 + dime*0.10 + quarter*0.25
    final = total
    
    # print(total)
    
    if menu[choice]['cost'] <= total:
        final = total - menu[choice]['cost']
        print('\nYou gave $',round(total,2),'The coffee costed $',menu[choice]['cost'],'Have your change $',round(final,2),'\n') 
        return 1
    else:
        print('\nInsufficient fund\nRefunding the change $',total,'\n')
        return 0 


def check(menu,choice):
        if resources['water'] >= menu[choice]['ingredients']['water']:
            if resources['milk'] >= menu[choice]['ingredients']['milk']:
                if resources['coffee'] >= menu[choice]['ingredients']['coffee']:
                    return 1
                else :
                    return 0
            else:
                return 0 
        else :
            return 0 
while 1:
    go = 0
    checked = 0

    choice = input("\n<<-- GET A COFFEE -->> \n1. Espresso\n2. Latte\n3. Cappuccino\nenter your choice : ")

    if choice == 'report':
        print('\n--------REPORT--------')
        report(resources)

    if choice != 'report' and check(menu,choice) == 1:
        checked = 1

    if choice != 'report' and checked == 0 :
        print("\n---<< Cant provide you the coffee due to item shortment >>--- \n")
        print("---<< RUN AGAIN >>---")
        break

    if choice != 'report' and coins(menu,choice) == 1 :
        go = 1

    if go == 1 and checked == 1:
        if choice == "latte" or choice == "cappuccino":
            resources['water'] = resources['water'] - menu[choice]['ingredients']['water']
            resources['milk'] = resources['milk'] - menu[choice]['ingredients']['milk']
            resources['coffee'] = resources['coffee'] - menu[choice]['ingredients']['coffee']
        elif choice == "espresso":
            resources['water'] = resources['water'] - menu[choice]['ingredients']['water']
            resources['coffee'] = resources['coffee'] - menu[choice]['ingredients']['coffee']
        print("Have your Coffee \nHappy to serve you :) \n")
        
    