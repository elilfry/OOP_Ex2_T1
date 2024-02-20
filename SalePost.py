"""
price
location


set sold
discount
etc
"""

from Post import Post


class SalePost(Post):

    # def comment(self):
    #     pass

    def __init__(self, user,  context, price, location):
        super().__init__(user, context)
        self.price = price
        self.location =location

    def discount(self):
        pass

    def sold(self):
        pass