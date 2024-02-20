#from SocialNetwork import SocialNetwork
from Post import PostFactory
"""
data

# name
# password
# set followers
#connected or not binary
"""


class User:
    def __init__(self, name, password, online):
        self.name = name
        self.password = password
        self.online = True
        self.followers = []
        self.post_counter = 0

    def __str__(self):
        return f"User name: {self.name}, Number of posts: {self.post_counter} , Number of followers: {len(self.followers)}"

    # new follower
    def follow(self, usr):
        self.followers.append(usr)
        # print(SocialNetwork.get_name(usr) + " started following " + SocialNetwork.get_name(self))
        print(self.name + " started following " + usr.name)

    # remove follower
    def unfollow(self, usr):
        self.followers.remove(usr)
        print(self.name + " unfollowed " + usr.name)

    # def publish_post(self, post_type, context ,):
    #     PostFactory.create_post(post_type, context)

    def publish_post(self, post_type, context, price=None, location=None):
        post = self.PostFactory.create_post(self, post_type, context, price, location)
        self.post_counter +=1
        return post

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

