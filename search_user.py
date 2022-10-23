from register import register
#from home import home
import sqlite3
import uuid
connection = sqlite3.connect("my_database")


def search_user():
    search_user = print(
        "Enter 1.to search by contact's last name,2. university 3. major: ")
    option = input()
    option_list = ["1", "2", "3"]

    if option == "1":
        last_name()
    if option == "2":
        university()
    if option == "3":
        major()
    return ("home")


def last_name():
    user_last = input("Enter your contact's last name: ")
    new_command = "SELECT username,first_name,last_name,friend_request FROM user_info WHERE last_name = ?"
   
    result_table = connection.execute(new_command, (user_last, ))
    #print(result_table.fetchall())
    a=result_table.fetchall()
    #print(a[1]) 
    
    for i in range(len(a)):
     print(i+1, '. ', a[i])
    
    friend_request=input("who would you like to send a friend request to?Please enter the username : ")

    your_username = input("Your username: ")
    addRequest = "INSERT INTO pending_request (user_name, friendRequest) VALUES ('" + your_username + "','" + friend_request + "')"
    connection.execute(addRequest)
    connection.commit()


def university():
    uni = input("Enter your uni's name: ")
    new_command = "SELECT username,first_name,last_name,friend_request FROM user_info WHERE university = ?"
   
    result_table = connection.execute(new_command, (uni, ))
    #print(result_table.fetchall())
    a=result_table.fetchall()
    #print(a[1]) 
    
    for i in range(len(a)):
     print(i+1, '. ', a[i])
    
    friend_request=input("who would you like to send a friend request to? Please enter the username : ")

    your_username = input("Your username: ")
    addRequest = "INSERT INTO pending_request (user_name, friendRequest) VALUES ('" + your_username + "','" + friend_request + "')"
    connection.execute(addRequest)
    connection.commit()


def major():
    
    major = input("Enter your major's name: ")
    new_command = "SELECT username,first_name,last_name,friend_request FROM user_info WHERE major = ?"
   
    result_table = connection.execute(new_command, (major, ))
    #print(result_table.fetchall())
    a=result_table.fetchall()
    #print(a[1]) 
    
    for i in range(len(a)):
     print(i+1, '. ', a[i])
    
    friend_request=input("who would you like to send a friend request to?Please enter the username : ")


    your_username = input("Your username: ")
    addRequest = "INSERT INTO pending_request (user_name, friendRequest) VALUES ('" + your_username + "','" + friend_request + "')"
    connection.execute(addRequest)
    connection.commit()

