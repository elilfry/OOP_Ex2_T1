"""
user
data



#like

#comment
"""
# from enum import Enum
from abc import ABC, abstractmethod


# from SocialNetwork import SocialNetwork


# class PostType(Enum):
#     Text = "Text"
#     Image = "Image"
#     Sale = "Sale"


# Factory class

# class PostFactory:
#     @staticmethod
#     def create_post(user, post_type, content , price=None, location=None):
#         if post_type == "Text":
#             return TextPost(user, content)
#         elif post_type == "Image":
#             return ImagePost(user ,content)
#         if post_type == "Sale":
#             return SalePost(user ,content,price,location)
#         else:
#             return None
# raise ValueError("Invalid post type")

# def create_post(self, post_type, objectForSale, price, location):
#     if post_type == PostType.Sale:
#         return SalePost(objectForSale,price,location)
#     else:
#         raise ValueError("Invalid post type")


# Post interface
class Post(ABC):
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.like_counter = 0

    def __str__(self):
        return self.content

    def like(self, liker):
        if self.user.online and self.user.name != liker.name:
            self.like_counter += 1
            # print(liker.name + " like post of " + self.user.name)
            # send notification


    def comment(self, user, content):
        pass
        # p3.comment(u2, "Can you give me your phone number?")