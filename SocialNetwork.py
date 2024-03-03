"""

name
users

function:
 sign up v
log_out v
log_in v
"""
from User import User


class SocialNetwork:
    __instance = None

    def __new__(cls, name):
        # If an instance does not exist, create one
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        cls.__instance.name = name
        cls.__instance.__users = []

        # print("The social network " + name + " was created!")

        return cls.__instance

    def __init__(self, name):
        self.name = name
        self.__users = []

        print("The social network " + name + " was created!")

    def sign_up(self, name, password):
        if self.valid_password(password) and self.valid_name(name):
            new_user = User(name, password)
            self.__users.append(new_user)

            return new_user  # return the new user

    def __str__(self):
        users_info = "\n".join(f"{users}" for users in self.__users)
        return f"Twitter social network:\n{users_info}"

    def log_in(self, name, password):
        user = self.get_user(name)
        if user and user.password == password:
            self.get_user(name).online = True
        print(name + " connected")

    def log_out(self, name):
        self.get_user(name).online = False
        print(name + " disconnected")

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
        if 4 <= len(password) <= 8:
            return True
        return False

    def get_name(self):
        return self.name
