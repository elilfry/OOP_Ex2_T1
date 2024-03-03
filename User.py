from abc import ABC, abstractmethod

import Post
from ImagePost import ImagePost
from SalePost import SalePost

from TextPost import TextPost


class Member(ABC):  # Observer interface (Member) - Observer pattern
    @abstractmethod
    def update(self, push, string, commenter_liker=None):  # update method
        pass


class User(Member):
    def update(self, post, string, commenter_liker=None):
        if string == "post":
            # print(f"notification to {self.name}:")
            self.__notification.append(post.user.get_name() + " has a new post")
            # add a new post to the notification list
        elif string == "like":
            # print a notification
            print(f"notification to {self.get_name()}: {commenter_liker.get_name()} liked your post") 
            self.__notification.append(f"{commenter_liker.get_name()} liked your post")
        elif string == "comment":
            print(f"notification to {self.get_name()}: {commenter_liker.get_name()} commented on your post: {post}")
            self.__notification.append(f"{commenter_liker.get_name()} commented on your post")

    def __init__(self, name, password):  # constructor
        self.__name = name
        self.__password = password
        self.__online = True
        self.__followers = []
        self.__post_counter = 0
        self.__notification = []

    def __str__(self):  # print the user
        return f"User name: {self.get_name()}, Number of posts: {self.__post_counter}, Number of followers: {len(self.get_followers())}"

    # new follower
    def follow(self, usr):  # follow a user
        # check if the user is online and not already following the user
        if self.get_online() and self not in usr.get_followers():
            usr.get_followers().append(self)  # add the user to the followers list
            print(self.get_name() + " started following " + usr.get_name())

    # remove follower
    def unfollow(self, usr):  # unfollow a user
        if self.get_online() and self in usr.get_followers():  # check if the user is online and following the user
            usr.get_followers().remove(self)
            print(self.get_name() + " unfollowed " + usr.get_name())

    # def publish_post(self, post_type, context ,):
    #     PostFactory.create_post(post_type, context)

    def publish_post(self, post_type, context, price=None, location=None):  # publish a post
        if self.get_online():
            post = self.PostFactory.create_post(self, post_type, context, price, location)
            self.__post_counter += 1
            self.notify(post, "post")  # notify the followers
            return post
        else:
            return False

    def notify(self, post, string, commenter_liker=None):
        if string == "post":
            for follower in self.get_followers():
                follower.update(post, string)
        elif string == "like":
            self.update(post, string, commenter_liker)
        elif string == "comment":
            self.update(post, string, commenter_liker)

    def print_notifications(self):  # print the notifications
        print(f"{self.get_name()}'s notifications:")
        for i in self.__notification:
            print(i)
    
    def get_name(self):
        return self.__name

    def get_followers(self):    # get the followers list
        return self.__followers

    def get_password(self):
        return self.__password

    def get_online(self):
        return self.__online

    def set_online(self, status):
        self.__online = status

    class PostFactory:  # Factory class for creating posts
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
