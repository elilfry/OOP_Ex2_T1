from matplotlib import image as mpimg

from Post import Post
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
#
import matplotlib.pyplot as plt
from PIL import Image


class ImagePost(Post):
    def __init__(self, user,  content):
        super().__init__(user, content)
        print(self.__str__())

    def __str__(self):
        return f"{self.user.name} posted a picture\n"

    def display(self):

        img = mpimg.imread(self.content)
        plt.imshow(img)
        plt.axis('off')  # Hide axis
        plt.show()
        print("Shows picture")


        # image_path = r"C:\Users\nnbbj\PycharmProjects\OOP_Ex2_T1\picT1.jpg"
        # image = Image.open(image_path)
        #
        # # Display the image
        # plt.imshow(image)
        # plt.axis('off')  # Hide axis
        # plt.show()
        # print("Shows picture")

    """""
    from matplotlib import image as mpimg
    from Post import Post
    import matplotlib.pyplot as plt


    class ImagePost(Post):

        def __init__(self, owner, picture_path):
            super().__init__(owner, picture_path)

        def display(self):
            img = mpimg.imread(self._content)
            plt.imshow(img)
            plt.show()
            print("Shows picture")

        def __str__(self):
            return self._owner.username + " posted a picture" + "\n"
    """""