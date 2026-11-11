# The Dumb Quest

A tongue-in-cheek text adventure game for the command line. Create a character, decide what to do with a mysterious chest in the woods, then fight or flee from an unknown enemy, with luck and a bit of randomness deciding how it goes.

## Features

- Character creation: name your hero and split 50 points between Strength and Luck, then get a random bonus to make each character unique
- Choices that change the story: open the chest or walk on, take some, all or none of the items, then fight or run
- Pick items from the chest by name, in any combination of capitals (`frog skin`, `Frog Skin`, `FROG SKIN`)
- Checks input during character creation and at the chest, so typos or invalid point totals ask again instead of crashing
- Inventory system for items picked up along the way
- Turn-based combat against a randomly generated enemy:
  - whoever has more Luck strikes first
  - each hit is based on Strength plus a random luck bonus
  - the fight continues until one side's health runs out
- Running away depends on your Luck: escape unharmed, or take a random hit on the way

## Built with

- Python 3
- `random` for enemy stats, attack bonuses and character bonuses
- `time` for pacing the fight

## Running it

You need Python 3. No extra packages are required.

```
python3 DumbQuest.py
```

Follow the on-screen prompts and type your choices when asked.

## Example

A real fight from the game:

```
Lewis here are your stats:

    Strength    :   48
    Luck        :   32
    Attack      :   24.0

    Here are the enemy stats:

    Strength    :   27
    Luck        :   23
    Attack      :   13.5

Lewis goes first and strikes a hit of 24.0 plus 31

Enemy's health is reduced to 45.0

Enemy goes next and strikes a hit of 13.5 plus 2

Lewis's health is reduced to 84.5
```

## Project status

This was an early project (September 2022), written with a bit of humour as a fun way to practise Python basics. The first chapter is playable from start to finish, but the story stops after the first encounter, and the `invent` option in the fight isn't built yet.

## What I learned

- Using `while` loops and `if`/`elif`/`else` to handle player choices
- Generating random numbers with the `random` module to make each game different
- Working with lists to move items between the chest and the inventory
- Writing small functions (`buildenemy`, `attackbonus`) to reuse logic
- Revisiting old code in 2026 to fix bugs in the chest and character creation, and add input checks

## Ideas for improvement

- Add more chapters and let the player use inventory items in a fight
- Handle the case where the player and enemy have equal Luck, as the fight currently doesn't start
- Move repeated code (such as the two fight loops) into functions