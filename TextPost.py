
from Post import Post


class TextPost(Post):

    # def comment(self):
    #     pass

    def __init__(self, user,  content):
        super().__init__(user, content)
        print(self.__str__())

    def __str__(self):
        return f"{self.user.get_name()} published a post:\n\"{self.content}\"\n"


