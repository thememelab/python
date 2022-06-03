
#Persisting data

user_name = input("Enter your name: ")
add_user  = open("user_file,txt","a")
add_user.write(user_name + "\n")
add_user.close()


read_user  = open("user_file,txt","r")
user_list = read_user.read()
read_user .close()
print("The previous users of this program were:")
print(user_list)
