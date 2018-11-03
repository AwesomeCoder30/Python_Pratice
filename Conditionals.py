# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

if True:
    print("Condition was True")

if False:
    print("Condition was False")


language = 'Python'
student = "Parth"
if language == 'Python':
    print("Language is Python")
elif language == 'Java':
    print("Language is Java")
else:
    print("No Match")

language = input("enter language: ")
student = input("enter student: ")
#and statement in if condition
if language == 'Python' and student == 'Parth':
    print("Language is Python and student is Parth")
elif language == 'Java' and student == 'ABC':
    print("Language is Java")
else:
    print("No Match")

#or condition in if condition
if language == 'Python' or student == 'Parth':
    print("Language is Python and student is Parth")
elif language == 'Java' or student == 'ABC':
    print("Language is Java and student is ABC")
else:
    print("No Match")




