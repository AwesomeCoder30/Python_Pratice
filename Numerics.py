# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2

intNum = 3
floatNum = 3.14
print(type(intNum))
print(type(floatNum))

print(3+2)
print(3-2)
print(3*2)
print(3/2)
#Floor divistion - want to drop decimal values
print(3//2)
#Exponent
print(3**2)
#Modulus - reminder after the division
print(3 % 2)

num =3
#num = num +3
num +=3
print(num)

num=3
#num = num*10
num *=10
print(num)



#abs value
print(abs(-3))

#print round value
print(round(3.56))
print(round((3.25)))
#round to first digit after decimal
print(round(3.56,1))
print(round(3.25,1))

#convert string to int
num_1 = '100'
num_2 = '200'

print(num_1 + num_2)

num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)