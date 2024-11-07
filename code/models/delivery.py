class Delivery:
    def __init__(self, id, sender, recipient, package):
        self.id = id
        self.sender = sender
        self.recipient = recipient
        self.package = package

    def __str__(self):
        return f"{self.id}, {self.sender}, {self.recipient}, {self.recipient}, {self.package}"
