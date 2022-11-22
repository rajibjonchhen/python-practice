
# simple login
print("--- Enter your username and password to create new user ---")

newUserName = input("enter your user name : ")
while len(newUserName) <= 5:
    print("username must be longer than 5")
    newUserName = input("enter your user name : ")

newUserPass = input("enter your password : ")
while len(newUserPass) <= 5:
    print("password must be longer than 5")
    newUserPass = input("enter your password : ")

print("the user has been created successfully")

loginUsername = input("enter your user name : ")
loginPassword = input("enter your password : ")


print("--- Enter your username and password to log in ---")
while newUserName != loginUsername and newUserPass != loginPassword:
    loginUsername = input("enter your username : ")
    loginPassword = input("enter your password : ")

print("the user successfully logged in")


