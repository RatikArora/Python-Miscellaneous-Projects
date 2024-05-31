print("WELCOME TO THE TREASURE GAME \nYOUR MISSION IS TO FIND THE TREASURE")
a = input("You walk a mile and you are at a cross road now. Where do you want to go now? 'left' or 'right' :-")
if a == 'left':
    b = input("You walk half a mile and you see a lake? would to like to swim 'swim' or wait for the boat 'wait' :-")
    if b == 'wait':
        print("You crossed the lake cogratulations!")
        c = input("You see a house having 3 doors of all different color red, blue or yellow :-")
        if c == 'red':
            print("There was fire in the room and you were burnt alive lol. \nGAME OVER!")
        elif c == 'blue':
            print("The room was filled with the blue poison dart frog and you died by poisonous stung. \nGAME OVER!") 
        else :
            print("You won the game. either hide and spend it or give government 33 percent of it. lol X 2.")
            
    else : print("You were eaten by the anaconda from the oiginal anaconda movie not anacoda 3 that movie was a lie. \nGAME OVER SMART WET ASS!")

    
else :print("Uh oh you lost in the endless woods. Died because a tree fell on you while you were asleep. \nGAME OVER!")