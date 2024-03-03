from matplotlib import image as mpimg

from Post import Post
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
#
import matplotlib.pyplot as plt
from PIL import Image


class ImagePost(Post):
    def __init__(self, user,  content):  # constructor
        super().__init__(user, content)  # call the parent constructor
        print(self.__str__())

    def __str__(self): # print the picture
        return f"{self.user.name} posted a picture\n"

    def display(self):  # display the picture

        img = mpimg.imread(self.content)  # read the image
        plt.imshow(img)  # Display the image
        plt.axis('off')  # Hide axis
        plt.show()
        print("Shows picture")

