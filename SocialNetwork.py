"""
singelton
name
users

function:
 sign up v
log_out v
log_in v
"""
from User import User


class SocialNetwork:
    def __init__(self, name):
        self.name = name
        self.__users = []

    def sign_up(self, name, password):
        if self.valid_password and self.valid_name:
            new_user = User(name, password, True)
            self.__users.append(new_user)

    def log_in(self, name, password):
        user = self.get_user(name)
        if user and user.password == password:
            self.get_user(name).online = True

    def log_out(self, name):
        self.get_user(name).online = False

    def get_user(self, name):
        for user in self.__users:
            if user.name == name:
                return user

    def valid_name(self, name):
        for user in self.__users:
            if user.name == name:
                return False
        return True

    def valid_password(self, password):
        if 4 <= password.len <= 8:
            return True
        return False
