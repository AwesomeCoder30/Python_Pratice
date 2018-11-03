import random

RANGE5 = input("Enter a number greater than 1: ")
RANGE5 = int(RANGE5)

for number in range(1, RANGE5+ 1):
    rem2 = number % 2
    rem7 = number % 7
    rem14 = number % 14
    rem5 = number % 5
    rem10 = number % 10
    if rem14 == 0:
        print("FizzBuzz")
    elif rem10 == 0:
        print("Warriors")
    elif rem2 == 0:
        print("Fizz")
    elif rem7 == 0:
        print("Buzz")
    elif rem5 == 0:
        print("StephenCurry51Points")
    else:
        print(number)