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
        self.online = online
        self.followers = []

    # new follower
    def follow(self, usr):
        self.followers.append(usr)
        # print(SocialNetwork.get_name(usr) + " started following " + SocialNetwork.get_name(self))
        print(usr.name + " started following " + self.name)

    # remove follower
    def unfollow(self, usr):
        self.followers.remove(usr)
        print(usr.name + " unfollowed " + self.name)

    def publish_post(self, post_type, context):
        PostFactory.create_post(post_type, context)

    def publish_post(self, post_type, objectForSale, price, location):
        PostFactory.create_post(post_type, objectForSale, price, location)


    """
     #function

      #follow
      
      #unfollow
      
      
      
      

     #publish_post

      

     #notification


     #to string

     #print all notification the user had
"""