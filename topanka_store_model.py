class topanka_store:
    def __init__(self):
        self.store = []

    def add_topanka(self, udaj):
        self.store.append(udaj)
    def remove_topanka(self, udaj):
        self.store.remove(udaj)
    def get_topanka(self):
        return self.store

    


