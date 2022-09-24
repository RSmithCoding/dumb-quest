#   A text based adventure only for the faint hearted

import os
import random


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
        print()
        print(chest)
        print()
        input("Press any key to continue...")

    elif choice == "walk":
        print()
        print("You walk on... ")
        print()
        input("Press any key to continue...")
    else:
        print()
        choice = input("Please type 'open' or 'walk '> ")
