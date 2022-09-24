#   A text based adventure only for the faint hearted

import os
import random
import time


def clear():
    os.system('cls')

# welcome screen


clear()
print("*" * 100)
print("*" * 100)
print("**"+" " * 96 + "**")
print("**"+" " * 41 + "The Dumb Quest" + " " * 41 + "**")
print("**"+" " * 96 + "**")
print("*" * 100)
print("*" * 100)
print()
print()
print("Welcome Warrior, if thats what you claim to be. You're about to start your quest... Good Luck!")
print()
print("Lets get going and create your character...")
print()
input("Press any key to continue...")
clear()

# Character creation

points = int(50)
health = 100

print("Please enter your characters name")
c_name = input("> ")

while points != 0:
    clear()
    print(
        f"Please enter your characters Strengh and Luck using your 50 points; you have {points} left")
    print()
    c_strength = input("Please set your characters Strength: ")
    points = points - int(c_strength)
    clear()
    print(
        f"Please enter your characters Strengh and Luck using your 50 points; you have {points} left")
    print()
    c_luck = input("Please set your characters Luck: ")
    points = points - int(c_luck)

    if points < 50 and points > 0:
        print()
        print(f"You still have {points} points left please restart")
        print()
        input("Press any key to continue...")
        points = 50

# Stat adjusting

c_strength = int(c_strength) + random.randint(1, 25)
c_luck = int(c_luck) + random.randint(1, 25)


clear()
print("You're looking really tough, i mean i'm intimidated...")
print()
print(f"Here's a summary of your stats {c_name}")
print()
print(f"Name:       {c_name}")
print()
print(f"Strength:   {c_strength}")
print()
print(f"Luck:       {c_luck}")
print()
print("Confused? You should be. We've added a random number to your stats to make you unique i'm not promissing it's going to help though!")
print()
input("Press any key to start...")
clear()

# first day

chest = ["Chocolate", "Tin Opener", "Frog Skin"]
invent = []

print("Your walking though some woods (does'nt get any better then this)... suddenly you trip over... you gance down expecting a mushroom, but find a CHEST!")
print()
print("What would you like to do? OPEN the chest or WALK on?")
print()
choice = input("Please type 'open' or 'walk' > ")

while choice != "open" or "walk":

    if choice == "open":
        clear()
        print("Here are the contents of the chest:")
        print()
        print(chest)
        print()
        print("Would you like to take these items?")
        print()
        choice_take = input("Please type 'some', 'all' or 'none' > ")
        if choice_take == "some":
            print()
            print("Please type each item you would like or 'done' when finished")
            print()
            take_item = input("Type the item from the chest to keep >")
            if take_item != "done":
                for take_item in chest:
                    chest.remove(take_item)
                    invent.append(take_item)
                    print()
                    print("Item added to Inventory")
                    print()
                    print(
                        "Please type each item you would like or 'done' when finished")
                    print()
                    take_item = input("Type the item from the chest to keep >")
                    if take_item == "done":
                        clear()
                        print("this is your inventory:")
                        print(invent)
                        print()
                        print("this is the chest:")
                        print(chest)
                        print()
                        input("Press any key to continue...")
                        break
            elif take_item == "done":
                print("ready for next chapter")
                print()
                input("Please press a key to continue")
        elif choice_take == "all":
            clear()
            invent = [item for item in chest]
            chest.clear()
            print("this is your inventory:")
            print(invent)
            print()
            print("this is the chest:")
            print(chest)
            print()
            input("Press any key to continue...")

        elif choice_take == "none":
            print("ready for next chapter")
            break
        else:
            choice_take = input("Please type 'some', 'all' or 'none' > ")

    elif choice == "walk":
        clear()
        print("You walk on... ")
        print()
        input("Press any key to continue...")

        break

    else:
        print()
        choice = input("Please type 'open' or 'walk' > ")

clear()
print("A New Day...")
print()
print("You continue on your epic quest, with excitement around every corner you take a turn...")
print()
input("Press any key if you dare...")
clear()
print("Theres movement up ahead, your not sure what it is but you know it wants a fight")
print()
print("You've some decisions to make...")
print()
print("Your not equiped for battle, you can fight anyway or try to run like a coward. Or you can hope to have something usefull in your pocket")
print()
choice = input("Please type 'fight', 'run' or 'invent' > ")

if choice == "fight":
    print()
elif choice == "run":
    if c_luck >= 50:
        clear()
        print("You try your luck and attempt to run...")
        time.sleep(3)
        print()
        print("You manage to escape unharmed well done!")
    else:
        clear()
        print("You try your luck and attempt to run...")
        time.sleep(3)
        print()
        print("You escaped but not without harm")
        print()
        hit = random.randint(1, 100)
        health = health - hit

        print(f"You took a hit of -{hit} your health is now {health}")

        if health <= 0:
            clear()
            print("Well that's great, your dead...")
            print()
            input("Press any key to continue...")
        else:
            print()
            print("You hobble away and look pathetic...")
            print()
            input("Press any key to continue...")


elif choice == "invent":
    print()
else:
    choice = input("Please type 'fight', 'run' or 'invent' > ")

clear()
print("END CREDITS")
