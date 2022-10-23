def find_member():
    user_first_last = input("Enter your contact's first and last name: ")
    user_list = open("userInfo.txt", "r")
    for line in user_list:
        count = 0
        target_name = ""
        for word in line.split():
            count += 1
            if count == 3:
                target_name = target_name + word + " "
            if count == 4:
                target_name = target_name + word
        if target_name == user_first_last:
            print("They are in the system")
            return "welcome"
    print("They are not in the system yet!")
    return "welcome"
    