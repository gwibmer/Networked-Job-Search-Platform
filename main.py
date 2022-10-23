import pytest
import sqlite3
#from replit import db
from driver import driver

pytest.main
#to be used for assertations in pytest
passwordCorrect = False
userNameCorrect = False
loginSuccess = False
maxUser = False

connection = sqlite3.connect("my_database")
connection.execute("CREATE TABLE IF NOT EXISTS user_info (username TEXT PRIMARY KEY, password TEXT, first_name TEXT, last_name TEXT, university TEXT, major TEXT, lang TEXT,friend_request TEXT);")
connection.commit()
print_current_user_info = "SELECT * FROM user_info;"
current_user_info = connection.execute(print_current_user_info)
#print(current_user_info.fetchall())

connection.execute("CREATE TABLE IF NOT EXISTS pending_request (user_name TEXT, friendRequest TEXT, PRIMARY KEY(user_name, friendRequest));")
#connection.execute("CREATE TABLE IF NOT EXISTS pending_request (user_name TEXT, friendRequest TEXT);")

connection.execute("CREATE TABLE IF NOT EXISTS friends (user_name TEXT, friend_name TEXT, PRIMARY KEY(user_name, friend_name));")

connection.execute("ALTER TABLE user_info ADD COLUMN Education VARCHAR(100);")

connection.commit()
print_current_user_info = "SELECT * FROM pending_request;"
current_user_info = connection.execute(print_current_user_info)
#print(current_user_info.fetchall())









#starts program
#displayLoginMenu()
if __name__ == "__main__":
    driver()

#questions? go to mapper.py to read my notes first, probably