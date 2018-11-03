courses = ['History', 'Math', 'Physics', 'Spanish']

#print all
print(courses)

#Length of list
print(len(courses))

#print by index
print(courses[0])
print(courses[3])
#print(courses[4])
print(courses[0:2])

#append item to list
courses.append("Art")
print(courses)

#at particular index
courses.insert(0,"Art")
print(courses)
courses.remove("Art")
print(courses)

#for loop retrieve all items one by one from a list
for item in courses:
    print(item)

print("Popped:", courses.pop())
print(courses)