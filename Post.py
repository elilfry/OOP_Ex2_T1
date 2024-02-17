"""
user
data



#like

#comment
"""
from enum import Enum
from abc import ABC, abstractmethod
from SocialNetwork import SocialNetwork

# Enum to represent Post types
class PostType(Enum):
    Text = "Text"
    Image = "Image"
    Sale = "Sale"


# Factory class
class PostFactory:
    def create_post(self, post_type, context):
        if post_type == PostType.Text:
            return TextPost(context)
        elif post_type == PostType.Image:
            return ImagePost(context)
        else:
            raise ValueError("Invalid post type")

    def create_post(self, post_type, objectForSale, price, location):
        if post_type == PostType.Sale:
            return SalePost(objectForSale,price,location)
        else:
            raise ValueError("Invalid post type")


# Post interface
class Post(ABC):
    
    owner =

    @abstractmethod
    def like(self, user):
        if not user.online and user.name !=  self.owner




    @abstractmethod
    def comment(self, user, context):
        pass


