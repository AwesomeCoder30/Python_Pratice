import random

target = random.randint(1,100)
print(target)

Guess = 0
difference = 0
Predifference = 0
while Guess != target:
    Guess = input("Enter a number between 1-100: ")
    Guess = int(Guess)
    difference = abs(Guess - target)
    if Guess == target:
        print("You won the game.")
        break
    if difference >= 50:
        print("Very Freezing !!.")
    elif difference >= 40:
        print("Freezing !!.")
    elif difference >= 30:
        print("Melting !!")
    elif difference >= 20:
        print("Cold !! ")
    elif difference >= 10:
        print("Normal !!")
    elif difference >= 5:
        print("Hot !!")
    elif difference >= 2:
        print("Very Hot !!")
    elif difference < 2:
        print("Boiling !!")
    Predifference = difference


