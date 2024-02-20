
"""
user
data



#like

#comment
"""
from enum import Enum
from abc import ABC, abstractmethod

# from SocialNetwork import SocialNetwork



# class PostType(Enum):
#     Text = "Text"
#     Image = "Image"
#     Sale = "Sale"


# Factory class

# class PostFactory:
#     @staticmethod
#     def create_post(user, post_type, context , price=None, location=None):
#         if post_type == "Text":
#             return TextPost(user, context)
#         elif post_type == "Image":
#             return ImagePost(user ,context)
#         if post_type == "Sale":
#             return SalePost(user ,context,price,location)
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
    def __init__(self, user, context):
        self.user = user
        self.context = context
        self.like_counter = 0

    def __str__(self):
        return self.context

    def like(self, user):
        if user.online and user.name !=  self.user:
            self.like_counter += 1
            print(user.name + "like post of " + self.user)
            #send notification

    # @abstractmethod
    # def comment(self, user, context):
    #     pass






