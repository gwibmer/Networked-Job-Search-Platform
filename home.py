from incollege_important_links import incollege_important_links
from friend_list import show_friends
from search_user import search_user
from friends_requests import friends_requests

def home():
    print("Welcome back! Please select an option below.")
    print("1. Explore open positions")
    print("2. Post a job")
    print("3. Learn a new skill")
    print("4. Log out")
    print("5. InCollege Important Links")
    print("6. See Network")
    print("7. Search user")
    print("8. View pending requests")
    print("9. Quit InCollege")
    option = input("Please choose an option above (1-9) :")
    option_list = ["1", "2", "3", "4", "5", "6", "7","8","9"]
    while option not in option_list:
        option = input("Invalid option, please choose again!")
    if option == "1":
        return "find_job"
    if option == "2":
        return "post_job"
    if option == "3":
        return "learn_new_skill"
    if option == "4":
        print("Logged out succesfully!\n")
        return "welcome"
    if option == "5":
        return incollege_important_links()
    if option == "6":
        return show_friends()
    if option == "7":
        return search_user()
    if option == "8":
        return friends_requests()
    if option == "9":
        return 666


#We need a "setting" option to change password, first and last name, and even username, or to delete the account. Ask me if you don't know how to do it.
