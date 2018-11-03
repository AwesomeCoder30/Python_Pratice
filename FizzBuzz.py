import random

range1 = input("Enter a number above 1: ")
range1 = int(range1)
for number in range(1, range1 +1):
    rem3 = number % 3
    rem5 = number % 5
    rem15 = number % 15
    if rem15 == 0:
        print("FizzBuzz")
    elif rem3 == 0:
        print("Fizz")
    elif rem5 == 0:
        print("Buzz")
    else:
        print(number)
