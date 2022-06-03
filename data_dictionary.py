#data Structure
#dictionaryies
userDetails = {
"user1":"password2","user2":"password2"
}
#dictioanary can access by key value pairs
print(userDetails["user1"])

item_catelog = {
"Blank Cd":7.66,
"Usb Tick": 4.99,
"Keyborad":19.43,
"Mouse":3.88,
"Sd card":12.99
}

#infomation for user
print("here re a list of item in our catelog")

#print all items in the actelog
#the key alone give the item
for x in item_catelog:
    print(x)

# dictioanary[key] give the values related to the key
#for x in item_catelog:
    #print(item_catelog[x])


# fucntion to check is items in dictioanary
def exits_in(D,name):
    results = False
    for x in D:
        if x == name:
            results = True
    return results

#altnative way of writing the above function
    # if name in D.keys():
    #     results = True
    #     print(results)
    # else:
    #     print(results)
    # return results

#while loop fucntion with a  break
exit_var = False
while exit_var == False:
    input_var = input("Enter a product name to look up the price or type x exit the program: ")
    if exits_in(item_catelog,input_var):
        print("the pice of this item is:")
        print(item_catelog[input_var])

    if exits_in(item_catelog,input_var) == False and input_var != "x":
        print("the item you have etered does not exixt in our catelog")
    if input_var == "x":
        exit_var = True
