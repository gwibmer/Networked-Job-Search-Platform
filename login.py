def login():  #i can add the return option later, it's trivial
    username = input("Please type in your username: ")
    password = input("Please type in your password: ")
   # university = input("Please enter your university:")
    
    while not check_credential(username, password):
        print("Incorrect username or password.")
        username = input("Please type in your username: ")
        password = input("Please type in your password: ")
    print("Log in successful!")
    return ("home")


def check_credential(username, password):
    username = "u:" + username
    password = "p:" + password
    credential = username + " " + password
    user_file = open("userInfo.txt", "r")
    for line in user_file:
        if credential in line:
            user_file.close()
            return True
    user_file.close()
    return False
