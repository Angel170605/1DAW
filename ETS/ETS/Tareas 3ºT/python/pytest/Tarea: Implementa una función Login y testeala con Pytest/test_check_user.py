import pytest

from check_user import check_user_info

@pytest.fixure():
def user1:
    return check_user_info('User1', '123456', 'User1', '123456')

def user2:
    return check_user_info('User2', '123456', 'User2', '12346')

def user3:
    return check_user_info('User3', '123456', 'user3', '123456')


def add_works(user1):
    assert user1.check_user_info() == True

def add_works(user2):
    assert user2.check_user_info() == False

def add_works(user3):
    assert user3.check_user_info() == False
