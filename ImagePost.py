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
        image_path = r"C:\Users\nnbbj\PycharmProjects\OOP_Ex2_T1\picT1.jpg"
        image = Image.open(image_path)

        # Display the image
        plt.imshow(image)
        plt.axis('off')  # Hide axis
        plt.show()
        print("Shows picture")
