class Package:
    def __init__(self, id, pickup, dropoff, weight):
        self.id = id
        self.pickup = pickup
        self.dropoff = dropoff
        self.weight = weight

    def __str__(self):
        return f"{self.id}, {self.pickup}, {self.dropoff}, {self.weight}"
