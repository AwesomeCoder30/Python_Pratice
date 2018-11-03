# Question 4

Lowerinput = input("Enter any number: ")
Upperinput = input("Enter any number greater than last input: ")
multiple1 = input("Enter the first multiple from above range: ")
multiple2 = input("Enter the second multiple from above range: ")

multiple1 = int(multiple1)
multiple2 = int(multiple2)
Upperinput = int(Upperinput)
Lowerinput = int(Lowerinput)

for number in range(Lowerinput, Upperinput+1):
    rem5 = number%multiple1
    rem7 = number%multiple2
    if rem5 == 0 and rem7 == 0:
        print(number)