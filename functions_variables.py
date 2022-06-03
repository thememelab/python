
#function and variables
#scoping local and global variables

#global variable x
x = 10

#fucntion defination
def calculate():
    print(x/10)

#fucntions with parameters
def tri_area(base,height):
    #local variable area
    area  = (base*height)/2
    return area

#calling functions with variables
print(tri_area(23,16))
print(tri_area(15,4))
print(tri_area(x,5))
calculate()

#conditional statements
#boolean expressions
user_num = input("Enter your guessing number here:")
user_num = int(user_num)

if user_num == 12:
    print("Wow! you guessed the magic number right")
elif user_num < 20 and user_num != 12:
    print("your number is less than 20")
else:
    print("your number is greater than 20")

#functions with conditioanl statements
def fomula(a,b):
    if b == 0:
        print("the number you have netered can not be used in operation")
    else:
        result = (a+b)/b
        return result

#calling functions with variables
print(fomula(x,user_num))
#loops

# while loops
i = 1
while i < 10:
  print(i)
  i += 1

#for loops
fruits = ["apple", "banana", "cherry"]
for i in fruits:
  print(i)

#looping through string
for i in "banana":
  print(i)

#function with while loops
def factorial(number):
    result = 1
    while number > 0:
      result = result*number
      number = number-1
    print(result)
#call factorial functions
factorial(user_num)

# break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
