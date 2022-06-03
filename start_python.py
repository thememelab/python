# import of modules
from datetime import date

# python variable print statments
print ("this is python")
# variables and data types  and structures
#intergers
velocity = 100
accelerate = 300
#foating point
gravity = 5.0
#strings
phrase = "here prints strings types"

#operation
speed = velocity * accelerate
braking = accelerate - velocity
take_off = accelerate / gravity
start_speed = velocity + accelerate

#getting inpute fron  user
user_name = input("Enter your name: ")

# take input from user
useryear = input("Enter your year of birth: ")
# type cast into integer
user_birthyear = int(useryear)

# user_age and message
current_year = date.today().year
user_age = current_year - user_birthyear
user_msg =   F"Hello, {user_name} You are {user_age} years old"

print(user_msg)

# print user data

#print statments

#print variable
print (velocity)
print (accelerate)
print ( phrase)

#print types
print(type(velocity))
print(type(gravity))
print(type(phrase))

#print operations
print(speed)
print(braking)
print(take_off)
print(start_speed)

#print user date
