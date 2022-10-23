from valid_major_list import valid_major_list


def find_job():
    #type_of_job, major, visa_sponsor, relocation
    print("What type of job are you looking for?")
    print("1. Entry-level")
    print("2. Internship")
    print(
        "3. Full-Time"
    )  # bro, both entry-level and internships are full time. full time is not a type of job
    #print("3. Both entry-level and internship") #we don't entertain people who lie to get jobs, and they can also do the search 2 times
    #why? because if we use SQL we should specify SQL queries from here instead of creating 3 more functions
    #if this app is not for CSE students only, we need to collect their majors too
    #and a bunch of other stuff, so that we can narrow down the search query and only return useful informations
    option = input()
    option_list = ["1", "2", "3"]
    while option not in option_list:
        option = input("Invalid option, please choose again")
    if option == "1":
        type_of_job = "Entry-level"
    if option == "2":
        type_of_job = "Internship"
    if option == "3":
        type_of_job = "Full Time"
    major = input("What is your major?")
    check_valid_major_list = valid_major_list()
    while major not in check_valid_major_list:
        major = input(
            "We could not verify your major, please try again, or choose a different major: "
        )
    relocation = input(
        "Are you willing to relocation if required by the company? Please type in \"Yes\" or \"No\": "
    )
    relocation_option = ["Yes", "No"]
    while relocation not in relocation_option:
        relocation = input(
            "Invalid choice, please type in \"Yes\" or \"No\": ")
    #all info collected. time to send a query to the DB for info
    print("Thank you, here are all relevant job posts we found: ")
    print("No job postings were found that match your criteria.")

    print("Page still under construction.")
    return "home"
