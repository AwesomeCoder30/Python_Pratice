import random

range2 = input("Enter a number above 1: ")
range2 = int(range2)

for number in range(1, range2+1):
    Oddnumber = number%2
    if Oddnumber != 0:
        print("Odd:", number)
    else:
        print("Even:", number)

