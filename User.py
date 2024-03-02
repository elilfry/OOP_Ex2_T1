from abc import ABC, abstractmethod

import Post
from ImagePost import ImagePost
from SalePost import SalePost

from TextPost import TextPost


class Member(ABC):
    @abstractmethod
    def update(self, push, string, commenter_liker=None):
        pass


class User(Member):
    def update(self, post, string, commenter_liker=None):
        if string == "post":
            # print(f"notification to {self.name}:")
            self.notification.append(post.user.name + " has a new post")
        elif string == "like":
            print(f"notification to {self.name}: {commenter_liker.name} liked your post")
            self.notification.append(f"{commenter_liker.name} liked your post")
        elif string == "comment":
            print(f"notification to {self.name}: {commenter_liker.name} commented on your post: {post}")
            self.notification.append(f"{commenter_liker.name} commented on your post")

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.online = True
        self.followers = []
        self.post_counter = 0
        self.notification = []

    def __str__(self):
        return f"User name: {self.name}, Number of posts: {self.post_counter}, Number of followers: {len(self.followers)}"

    # new follower
    def follow(self, usr):
        if self.online and self not in usr.followers:
            usr.followers.append(self)
            print(self.name + " started following " + usr.name)

    # remove follower
    def unfollow(self, usr):
        if self.online and self in usr.followers:
            usr.followers.remove(self)
            print(self.name + " unfollowed " + usr.name)

    # def publish_post(self, post_type, context ,):
    #     PostFactory.create_post(post_type, context)

    def publish_post(self, post_type, context, price=None, location=None):
        if self.online:
            post = self.PostFactory.create_post(self, post_type, context, price, location)
            self.post_counter += 1
            self.notify(post, "post")
            return post
        else:
            return False

    def notify(self, post, string, commenter_liker=None):
        if string == "post":
            for follower in self.followers:
                follower.update(post, string)
        elif string == "like":
            self.update(post, string, commenter_liker)
        elif string == "comment":
            self.update(post, string, commenter_liker)

    def print_notifications(self):
        print(f"{self.name}'s notifications:")
        for i in self.notification:
            print(i)

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
