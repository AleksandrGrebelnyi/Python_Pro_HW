class CartIter:

    def __init__(self, cart):
        self.cart = cart
        self.index = 0

    def __next__(self):
        if self.index < len(self.cart):
            self.index += 1
            return self.cart[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self