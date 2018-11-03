Usernumber = input("Enter any number: ")
Usernumber = int(Usernumber)

sumOdd = 0
sumEven = 0
for number in range(1, Usernumber+1):
    rem2 = number%2
    if rem2 != 0:
        sumOdd = number + sumOdd
    else:
        sumEven = number + sumEven
print("This is the sum of all odd numbers: ",sumOdd)
print("This is the sum of all even numbers: ",sumEven)