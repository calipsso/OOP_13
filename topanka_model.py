class Topanka:
    def __init__(self, male, female, color, size, brand, price, sku):
        self.male = male
        self.female = female
        self.color = color
        self.size = size
        self.brand = brand
        self.price = price
        self.sku = sku


class Topanka_store:
    def __init__(self):
        self.store = []

    def add_topanka(self, udaj):
        self.store.append(udaj)

    def remove_topanka(self, udaj):
        self.store.remove(udaj)

    def get_topanka(self):
        return self.store












