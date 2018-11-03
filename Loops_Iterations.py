numbers = [1,2,3,4,5]

for num in numbers:
    print(num)

print("""

Break Loop""")
#break loop
for num in numbers:
    if num==3:
        print("Found 3")
        break
    print(num)


print("""

Continue Loop""")
#Continue loop
for num in numbers:
    if num==3:
        print("Found 3")
        continue
    print(num)


print("""

Inner Loop""")
#inner loop
for num in numbers:
    for letter in 'abc':
        print(num,letter)

print("""

Range Loop""")
#range loop
for num in range(10):
    print(num)

#range loop
for num in range(1,11):
    print(num)

print("""

While Loop""")
#while loop
x = 0

while x < 10:
    print(x)
    x = x +1

print("""

While break Loop""")
#while loop
x = 0
while x < 10:
    if x==5:
        break
    print(x)
    x = x +1

print("""

While true break Loop""")
# while loop
x = 0
while True:
    if x==5:
        break
    print(x)
    x = x +1
