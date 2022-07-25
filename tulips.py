#tulips and sets
#Tuples are used to store multiple items in a single variable
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#tuplips can be access using the index number,
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#his example returns the items from the beginning to, but NOT included, "kiwi":
print(thistuple[:4])
#By leaving out the end value, the range will go on to the end of the list:
print(thistuple[2:])


#updating tuplips
#Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)


#Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#Create a new tuple with the value "orange", and add that tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


#Unpacking a tuple:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


#Iterate through the items and print the values:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


#Print all items by referring to their index number:
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


#Join two tuples:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Python has two built-in methods that you can use on tuples.
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

#Return the number of times the value 5 appears in the tuple:
x = thistuple.count(5)
print(x)

#Search for the first occurrence of the value 8, and return its position:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)
