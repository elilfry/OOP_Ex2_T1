
# from enum import Enum
from abc import ABC, abstractmethod


class Post(ABC):
    def __init__(self, user, content):  # constructor
        self.user = user
        self.content = content
        self.likes = []

    def __str__(self):  # print the post
        return self.content

    def like(self, liker): # like a post
        if self.user.online and liker not in self.likes:
            # check if the user is online and the liker did not like the post already
            self.likes.append(liker)  # add the liker to the likes list
            if self.user.name != liker.name:  # check if the liker is not the user
                self.user.notify(self, "like", liker)

    def comment(self, commenter, content):  # comment a post
        if self.user.online and self.user.name != commenter.name:
            # check if the user is online and the commenter is not the user
            self.user.notify(content, "comment", commenter)
