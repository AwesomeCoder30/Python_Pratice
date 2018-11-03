import random

Range_1 = input("Enter a number above 1: ")
Range_1 = int(Range_1)
PreNumber1 = 0
PreNumber2 = 1
count=0
result=0
while count< Range_1:
    print(result)
    PreNumber1 = PreNumber2
    PreNumber2 = result
    result = PreNumber1 + PreNumber2
    count = count +1
