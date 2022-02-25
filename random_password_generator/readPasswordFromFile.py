openFile = open("password.txt")
password = openFile.read()

# print("Enter your password: ")
inputPassword = input("Enter your password: ")
if password == inputPassword:
    print("You've entered correct password")
else:
    print("You've entered incorrect password")