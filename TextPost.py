
from Post import Post


class TextPost(Post):

    # def comment(self):
    #     pass

    def __init__(self, user,  context):
        super().__init__(user, context)


    def __str__(self):
        return f"{self.user.name} published a post:\n{self.context}"  #fix the " "


def __init__(self, context):
    self.context = context