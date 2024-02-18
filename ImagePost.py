from Post import Post


class ImagePost(Post):
    def __init__(self, user,  context):
        super().__init__(user, context)