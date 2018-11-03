#Question 1
import datetime
now = datetime.datetime.now()
print(now)
age = input("How old are you?: ")
age = int(age)
YearofBirth = now.year - age
print(YearofBirth)

