#Question 5

MultipleX = input("Enter number X: ")
PowerY = input("Enter number Y: ")

MultipleX = int(MultipleX)
PowerY = int(PowerY)

result = 1
for number in range(1, PowerY+1):
    result = MultipleX * result
print(result)