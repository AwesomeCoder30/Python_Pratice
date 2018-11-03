# Ouestion 6

def addition(val1, val2):
    return val1 + val2

def multiplication(val1, val2):
    return val1 * val2

def subtraction(val1, val2):
    return val1 - val2

def division(val1, val2):
    return val1 / val2


value1 = input("Enter any number: ")
value2 = input("Enter any number: ")
operation = input("Enter an operation, Add, Subtract, Multiply, or Divide: ")
value1 = float(value1)
value2 = float(value2)

operation = operation.lower()
result = 0
if operation == "add":
    result = addition(value1, value2)
elif operation == "subtract":
    result = subtraction(value1, value2)
elif operation == "multiply":
    result = multiplication(value1, value2)
elif operation == "divide":
    result = division(value1, value2)
print(result)

