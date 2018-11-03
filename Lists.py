L = ['yellow', 'red', 'blue', 'green', 'black']
print(L)
print(L[1])
print(L[4])
print(L[:2])
print(L[2:])
print(L[1:4])

#Length
print(len(L))

# sorting
print(sorted(L))


#Append item
L.append("pink")
print(L)

#insert Item
L.insert(1,"white")
print(L)

#remove item
L.remove("white")
print(L)


#reverse item
L.reverse()
print(L)

#for loop retrieve all items one by one from a list
for item in L:
    print(item)

#Keyword "in" - can be used to test if an item is in a list
if 'red' in L:
    print("list contains", 'red')