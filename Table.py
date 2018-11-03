# Question 7

for table in range(1, 11):
    sum = ' '
    for number in range(1, 11):
        result = table * number
        result = str(result)
        sum = sum + result + '  '
    print("This is the sum of the range: ",sum)