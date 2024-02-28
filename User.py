from abc import ABC, abstractmethod

from ImagePost import ImagePost
from SalePost import SalePost

from TextPost import TextPost

"""
data

# name
# password
# set followers
#connected or not binary
"""


class Member(ABC):
    @abstractmethod
    def update(self, push):
        pass


class User(Member):
    def update(self, push):
        print(f"notification to {self.name}:")
        # if it is a post notification
        pass

    online = None

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.online = True
        self.followers = []
        self.post_counter = 0

    def __str__(self):
        return f"User name: {self.name}, Number of posts: {self.post_counter} , Number of followers: {len(self.followers)}"

    # new follower
    def follow(self, usr):
        usr.followers.append(self)
        print(self.name + " started following " + usr.name)

    # remove follower
    def unfollow(self, usr):
        usr.followers.remove(self)
        print(self.name + " unfollowed " + usr.name)

    # def publish_post(self, post_type, context ,):
    #     PostFactory.create_post(post_type, context)

    def publish_post(self, post_type, context, price=None, location=None):
        post = self.PostFactory.create_post(self, post_type, context, price, location)
        self.post_counter += 1
        self.notify(post)
        return post

    def notify(self, post):
        for follower in self.followers:
            follower.update(post)

    class PostFactory:
        @staticmethod
        def create_post(user, post_type, context, price=None, location=None):
            if post_type == "Text":
                return TextPost(user, context)
            elif post_type == "Image":
                return ImagePost(user, context)
            if post_type == "Sale":
                return SalePost(user, context, price, location)
            else:
                return None

# Observer interface
# class Member(ABC):
#     @abstractmethod def update(self, push):
#             pass

# Concrete implementation of Observer (Member)
# class follower(Member):
#
#     def __init__(self, name):
#         self._name = name
#
#     def update(self, push):
#         print(f"{self._name} received newsletter: {push}")
