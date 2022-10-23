#username and password should also get hashed in the DB for searching convenience
#why, because it looks like we are not going to use SQL in this project. Not that we shouldn't, but everyone should have fundamental knowledge of SQL, which umm, idk if yall wanna do that.
#so, we can keep storing data in text files and optimize the searching functions for such purposes.
#for example, we can concatenate "u-" to the front of all usernames and "p-" to the front of all passwords. Then for all searching queries we concat the input once more to search for things in the db
#however, I must say that I personally think that we should adapt SQL in some forms because the further we get into development, the more inconvenient text file storing style will be. #quang

import sqlite3
connection = sqlite3.connect("my_database")
from valid_major_list import valid_major_list

def register():
    #CHECK IF THERE ARE ALREADY 5 ACCOUNTS
    if not number_of_account_check():
        print(
            "We ran out of slots for new members. Please log in or come back later!"
        )
        return "welcome"
    print(
        "Welcome to InCollege. Please choose your username. A valid username must be fewer than 32 characters and must not be empty: "
    )
    #username and password register & validation
    new_username = input()
    while not new_username_check(new_username):
        new_username = input()
    new_password = input(
        "Please choose a password. A valid password must be between 8 and 32 characters, containing at least 1 number, 1 uppercase character, and 1 special character: "
    )
    while not new_password_check(new_password):
        new_password = input()
    
    #first and last name typed in
    new_first_name = input("Type in your first name: ")
    new_last_name = input("Type in your last name: ")

    #other personal info
    university = input("Type in your university: ")
    major = input("Type in your major: ")
    # while major not in valid_major_list:
    #     major = input("Invalid major. Please try again: ")
    # lang = input("Choose your language preference (English or Spanish): ")
    # while lang != "English" or lang != "Spanish":
    #   lang = input("Invalid choice. Please choose again (Type English or Spanish): ")
    
    #database input
    insert_command = "INSERT INTO user_info (username, password, first_name, last_name, university, major, lang) VALUES (" + "'" + new_username + "', '" + new_password + "', '" + new_first_name + "', '" + new_last_name + "', '" + university + "', '" + major + "', '" +"')" #+ lang
  
    connection.execute(insert_command)
    connection.commit()

    #NEW VARANARA
    print(
        "Registration successful! You will be required to log in using your new username and password."
    )
    return ("login")


def new_password_check(new_password):
    upper_check = False
    special_check = False
    number_check = False
    special_list = "!@#$%^&*?+_(){}|\`~<>"
    plen = len(new_password)
    if plen > 32:
        print("Password too long. Please try again!")
        return False
    elif plen < 8:
        print("Password too short. Please try again!")
        return False
    for i in new_password:
        if i.isupper():
            upper_check = True
        if i in special_list:
            special_check = True
        if i.isnumeric():
            number_check = True
    if not upper_check:
        print("Password must have at least one uppercase character.")
        return False
    if not number_check:
        print("Password must have at least one number.")
        return False
    if not special_check:
        print("Password must have at least one special character.")
        return False
    return True


def new_username_check(new_username):
    if len(new_username) > 32:
        print("Username too long!")
        return False
    if new_username.isspace():
        print("Username must not be empty!")
        return False
    if not check_username_existence(new_username):
        print(
            "Username already existed, please log in or choose another username!"
        )
        return False
    return True


def check_username_existence(username):
    new_command = "SELECT username FROM user_info WHERE username = " + "'" + username + "'"
    result_table = connection.execute(new_command)
    print(result_table.fetchall())
    if username in result_table:
        return False
    return True
    #SQL Commands will now do the job
    return 0


def number_of_account_check():
    new_command = "SELECT COUNT(username) FROM user_info"
    if new_command == 10:
        return False
    return True
    #SQL Commands will now do the job


#OLD VARANARA
#new_username = "u:" + new_username
#new_password = "p:" + new_password
#user_list = open("userInfo.txt", "a")
#user_list.write(new_username)
#user_list.write(" ")
#user_list.write(new_password)
#user_list.write(" ")
#user_list.write(new_first_name)
#user_list.write(" ")
#user_list.write(new_last_name)
#user_list.write("\n")
#user_list.close()

#user_list = open("userInfo.txt", "r")
#    hashed_username = "u:" + username
#    if hashed_username in user_list:
#        user_list.close()
#        return False
#    user_list.close()
#    return True