import datetime

now = datetime.datetime.now()

""" print now.year, now.month, now.day, now.hour, now.minute, now.second """

name = raw_input("Enter your name:\n")

age = int(input("Enter your age: \n"))

years = int(input("Enter years:\n"))

rem = years - age

year = now.year + rem

print "Your name is ", name
print "You will turn ", years ," years on year", year