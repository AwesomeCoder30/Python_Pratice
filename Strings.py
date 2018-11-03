#singleLine
message = "Hello World"
print(message)

#multiline
message ="""

Hello World
next line hello world
bye"""
print(message)


message = "Hello World"
#Length of string
print("Length of string:", len(message))

#print based on index
print(message[0])
print(message[10])
print(message[0:5])
print(message[:5])
print(message[6:])

#print lower/upper case
print(message.lower())
print(message.upper())

#count letter/word
print(message.count("l"))
print(message.count("World"))

#find index letter/word
print(message.find("World"))
print(message.find("l"))


#replace
message = "Hello World"
print(message.replace("World","Parth"))
print(message)
message = message.replace("World","Parth")
print(message)

#concatenate
message = "Hello"
name = "Parth"
result = message + ", " + name;
print(result)
