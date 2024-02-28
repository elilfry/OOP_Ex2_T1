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

    def __init__(self, user,  content, price, location):
        super().__init__(user, content)
        self.price = price
        self.location = location
        self.available = "For sale!"
        print(self.__str__())

    def __str__(self):
        return f"{self.user.name} posted a product for sale:\n{self.available} {self.content}, price: {self.price}, pickup from: {self.location}\n"

    def discount(self, discount, password):
        if password == self.user.password:
            self.price = (self.price * (1-(discount/100)))
            print(f"Discount on {self.user.name} product! the new price is: {self.price}")

    def sold(self, password):
        if password == self.user.password:
            self.available = "Sold!"
            print(f"{self.user.name}'s product is sold")
