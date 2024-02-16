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
    def add_follower(self, usr):
        self.followers.append(usr)

    # remove follower
    def remove_follower(self, usr):
        self.followers.remove(usr)



    """
     #function

      #follow
      
      #unfollow
      
      
      
      

     #publish_post

      

     #notification


     #to string

     #print all notification the user had
"""