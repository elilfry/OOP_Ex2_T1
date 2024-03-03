
from Post import Post


class SalePost(Post):

    # def comment(self):
    #     pass

    def __init__(self, user,  content, price, location):  # constructor
        super().__init__(user, content)  # call the parent constructor
        self.price = price
        self.location = location
        self.available = "For sale!"
        print(self.__str__())

    def __str__(self):  # print the sale post
        return f"{self.user.get_name()} posted a product for sale:\n{self.available} {self.content}, price: {self.price}, pickup from: {self.location}\n"

    def discount(self, discount, password):  # discount a product
        # check if the pass is correct and the user is online
        if password == self.user.get_password() and self.user.get_online():
            self.price = (self.price * (1-(discount/100)))
            print(f"Discount on {self.user.get_name()} product! the new price is: {self.price}")

    def sold(self, password):  # sell a product
        # check if the pass is correct and the user is online
        if password == self.user.get_password() and self.user.get_online():
            self.available = "Sold!"
            print(f"{self.user.get_name}'s product is sold")
