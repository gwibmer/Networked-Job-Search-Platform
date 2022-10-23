#importing replit database
from replit import db


#Let the user to post a job and save it on replit databse
def post_job():
    keys = db.keys()
    count = 0
    #going through the database to get number of jobs
    for i in keys:
        count = count + 1
    #check if capacity is full
    if count >= 5:
        print("Job capacity is full")

    else:
        userName = input("Username:")
        print("Enter job:")
        title_in = input("Title:")
        description_in = input("Description:")
        employer_in = input("Employer:")
        location_in = input("Location: ")
        salary_in = input("salary:")
        db[userName] = {
            "title": title_in,
            "description": description_in,
            "employer": employer_in,
            "location": location_in,
            "salary": salary_in
        }

    #print(db.keys())
    #print(db["ggg"])
    return "home"
