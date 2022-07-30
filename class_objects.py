#class and objects


#supper class
#Class constructor with a variables

class vehicle():
    wheels = 4
    def __init__(self):
        print("vehicle")
    def calcVelocity(self,x):
        return 3*x+10

#sub  class inherits from a supperclass
class Car(vehicle):
    def __init__(self):
        self.speed = 10


#create an instance of the car class from vehicle
lightyear = Car()
#inheritance mena the car has properties if the parent class
print(lightyear.speed)
print(lightyear.calcVelocity(20))
print(lightyear.wheels)



# SyntaxError: invalid syntax
#Eg if (1==1)

#exceptions
# error in  the code logic eg.
val1 = int(input("Enter your first number here:"))
val2 = int(input("Enter your second number here:"))

# if ether number is 0 ther will be an exception thrown
# thus To prevent this you can use try and except clasue
try:
    print(val1/val2)
except ZeroDivisionError:
    print("values can not devided by zero")
