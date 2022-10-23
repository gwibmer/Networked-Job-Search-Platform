import pytest
#from register import new_password_check
from welcome import welcome
from io import StringIO
from register import new_password_check
from register import number_of_account_check
from valid_major_list import valid_major_list
from collections import defaultdict
from help_center import help_center
from about import about
from press import press
from blog import blog
from careers import careers
from developers import developers
from browse_incollege import browse_incollege
from business_solutions import business_solutions
from directories import directories
from guest_controls import guest_controls
from search_user import search_user
from search_user import last_name
from friend_list import add_friends
import unittest.mock as mock


@pytest.yield_fixture
def fake_input():
    with mock.patch('input') as m:
        yield m


def test_displayLoginMenu(capsys):
    with mock.patch('builtins.input', return_value='1'):
        welcome()


def test_new_password_check():
    Valid_Pwds = ["Test123@", "Testing1234@"]
    for pwd in Valid_Pwds:
        assert new_password_check(pwd) == True

    Invalid_Pwds = ["Test123", "test123@", "Test@One"]
    for pwd in Invalid_Pwds:
        assert new_password_check(pwd) == False


def test_number_of_account_check():
    count = 0
    Num_Users = open("userInfo.txt", "r")
    for user in Num_Users:
        count += 1
    if count < 10:
        assert number_of_account_check(Num_Users) == True


def test_valid_major_list():
    Valid_Majors = [
        "Computer Science", "Computer Engineering", "Political Science",
        "Biochemistry", "Biomedical Engineering", "Sports Management"
    ]
    assert valid_major_list() == Valid_Majors
    Invalid_Majors = [
        "Marketing", "Communications", "Music", "Health Sciences"
    ]
    assert valid_major_list() != Invalid_Majors


def test_helpCenter(capsys):
    with mock.patch('builtins.input', return_value='1'):
        help_center()


def test_about(capsys):
    with mock.patch('builtins.input', return_value='1'):
        about()


def test_press(capsys):
    with mock.patch('builtins.input', return_value='1'):
        press()


#def test_guestControls (capsys):
#with mock.patch('builtins.input', return_value='1'):
#cursor = capsys
#assert cursor.execute('SELECT * FROM guest_table') == "off"

#def test_search_user(capsys):
#with mock.patch('builtins.input', return_value='1'):
#search_user()


def test_add_friends():
    person1 = "juan"
    person2 = "pedro"
    assert add_friends(person1, person2) == "successful"

def  test_remove_friends():
    person1 = "juan"
    person2 = "pedro"
    friends = defaultdict(list)
    friends[person1].append(person2)
    friends[person2].append(person1)
    friends[person1].remove(person2)
    assert friends == {'juan': [], 'pedro': ['juan']}


