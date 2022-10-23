from collections import defaultdict

friends = defaultdict(list)


def add_friends(person1, person2):
    friends[person1].append(person2)
    friends[person2].append(person1)
    return "successful"#for test only. it doeesn't matter anyway.


# test = [['John', 'Smith'], ['Smith', 'Sheneska'],
#        ['Smith', 'Jack'], ['RandomGuy', 'otherRandy']]

# for p1, p2 in test:
#   add_friends(p1,p2)

# print(friends) 

# for k, v in friends.items():
#   print(f'here are {k}\'s friends:')
#   for vals in v:
#     print(vals)
#   print()


def show_friends():
    user = input("Confirm username:")
    if user in friends:
        for friend in friends[user]:
            print(friend)
        return "home"
    print("No connections to show.")
    return "home"


def remove_friends():
    user = input("Confirm username:")
    remove_person = input("Who would you like to remove?")
    friends[user].remove(remove_person)
    return "home"
