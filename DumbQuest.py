#   A text based adventure only for the faint hearted

import os
import random
import time


def clear():
    os.system('clear')


def buildenemy():
    e_strength = random.randint(1, 50)
    e_luck = 50 - e_strength
    return e_strength, e_luck


def attackbonus(luckfactor):
    randy = random.random()
    luckystrike = luckfactor * randy
    return int(luckystrike)


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
    points = 50
    clear()

    try:
        print(f"Please enter your characters Strength and Luck using your 50 points; you have {points} left")
        print()
        c_strength = int(input("Please set your characters Strength: "))
        if 0 <= c_strength <= 50:
            points = points - c_strength
            print()
            
        else:
            input("This needs to be a value between 0 - 50, press any key to retry..")
            continue
    except ValueError:
        input("Please enter a valid number between 0 - 50, press any key to retry..")
        continue

    try:
        print(f"Please enter your characters Strength and Luck using your 50 points; you have {points} left")
        print()
        c_luck = int(input("Please set your characters Luck: "))
        if c_luck == points:
            print()
            break
        else:
            input(f"You can only use the {points} points you have left, press any key to retry..")
            continue
    except ValueError:
        input("Please enter a valid number, press any key to retry..")    
        continue

    

# Stat adjusting

c_strength = c_strength + random.randint(1, 25)
c_luck = c_luck + random.randint(1, 25)


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
print("""Confused? You should be. We've added a random number to your stats to make you unique i'm not promising it's going
to help though!""")
print()
input("Press any key to start...")
clear()

# first day

chest = ["Chocolate", "Tin Opener", "Frog Skin"]
invent = []

print("""You're walking through some woods (doesn't get any better than this)... suddenly you trip over... you glance down
expecting a mushroom, but find a CHEST!""")
print()
print("What would you like to do? OPEN the chest or WALK on?")
print()
choice = input("Please type 'open' or 'walk' > ")

while True:

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

            while True:
                
                print()
                print("Please type each item you would like or 'done' when finished")
                print()
                take_item = input("Type the item from the chest to keep >").title()

                if take_item == "Done":
                    break
                    
                elif take_item in chest:
                    chest.remove(take_item)
                    invent.append(take_item)
                    input(f"The item {take_item} was added to your inventory, press a key to continue..")
                else:
                    input("Please type an item that is in the chest or 'done' press any key to continue..")
            clear()
            print("this is your inventory:")
            print(invent)
            print()
            print("this is the chest:")
            print(chest)
            print()
            input("Press any key to continue...")    
            break

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
            break

        elif choice_take == "none":
            print("ready for next chapter")
            break
        else:
            input("Please type 'some', 'all' or 'none', press any key to continue..")

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
print("There's movement up ahead, you're not sure what it is but you know it wants a fight")
print()
print("You've some decisions to make...")
print()
print("""You're not equipped for battle, you can fight anyway or try to run like a coward. Or you can hope to have something
useful in your pocket""")
print()
choice = input("Please type 'fight', 'run' or 'invent' > ")

if choice == "fight":
    # build enemy stats

    e_health = 100
    e_strength, e_luck = buildenemy()

    # create attack scores

    c_attack = c_strength / 2
    e_attack = e_strength / 2

    # compare stats
    clear()
    print(f"""{c_name} here are your stats:
    
    Strength    :   {c_strength}
    Luck        :   {c_luck}
    Attack      :   {c_attack}
    
    Here are the enemy stats:

    Strength    :   {e_strength}
    Luck        :   {e_luck}
    Attack      :   {e_attack}

    """)
    print()
    input("Press any key to start the fight!...")
    clear()

    # start battle

    if c_luck > e_luck:
        # character goes first
        while True:
            power = attackbonus(c_luck)
            print(f"{c_name} goes first and strikes a hit of {c_attack} plus {power}")
            print()
            e_health = e_health - (c_attack + power)
            print(f"Enemy's health is reduced to {e_health}")
            print()
            time.sleep(1)
            power = attackbonus(e_luck)
            print(
                f"Enemy goes next and strikes a hit of {e_attack} plus {power}")
            print()
            health = health - (e_attack + power)
            print(f"{c_name}'s health is reduced to {health}")
            print()
            time.sleep(1)
            clear()
            if health <= 0:
                break
            elif e_health <= 0:
                break

        if health <= 0 or e_health <= 0:
            if health < e_health:
                #character is dead
                clear()
                print("Your dead!")
                print()
                input("Press any key to die...")

            elif health > e_health:
                #enemy is dead
                clear()
                print("You WIN! you've left the enemy looking like mushy peas!")
                print()
                input("Press any key to continue...")

    elif c_luck < e_luck:
        # enemy goes first
        while True:
            power = attackbonus(e_luck)
            print(
                f"Enemy goes first and strikes a hit of {e_attack} plus {power}")
            print()
            health = health - (e_attack + power)
            print(f"{c_name}'s health is reduced to {health}")
            print()
            time.sleep(1)
            power = attackbonus(c_luck)
            print(f"{c_name} goes next and strikes a hit of {c_attack} plus {power}")
            print()
            e_health = e_health - (c_attack + power)
            print(f"Enemy's health is reduced to {e_health}")
            print()
            time.sleep(1)
            clear()
            if health <= 0:
                break
            elif e_health <= 0:
                break

        if health <= 0 or e_health <= 0:
            if health < e_health:
                #character is dead
                clear()
                print("Your dead!")
                print()
                input("Press any key to rot...")

            elif health > e_health:
                #enemy is dead
                clear()
                print("You WIN! you've left the enemy looking like mushy peas!")
                print()
                input("Press any key to continue...")
    else:
        c_combined = c_strength + c_luck
        e_combined = e_strength + e_luck
        if c_combined > e_combined:
            # character goes first
            print()
        else:
            # enemy goes first
            print()
    print()
elif choice == "run":
    if c_luck >= 50:
        clear()
        print("You try your luck and attempt to run...")
        time.sleep(1)
        print()
        print("You manage to escape unharmed well done!")
    else:
        clear()
        print("You try your luck and attempt to run...")
        time.sleep(1)
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
print()
input("Press a key to quit...(We know you'll be back for more!)...")
