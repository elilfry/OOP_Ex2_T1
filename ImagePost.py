from Post import Post


class ImagePost(Post):
    def __init__(self, user,  context):
        super().__init__(user, context)
        print(self.__str__())

    def __str__(self):
        return f"{self.user.name} posted a picture\n"

    def display(self):
        pass
