class Transfer(object):
    """
    One object of class Transfer is a representation of a bank funds transfer
    """

    def __init__(self, sender, receiver, amount):
        """
        Initialize a Transfer object with a sender, receiver, and an amount to send.
        """
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.status = "pending"

    def get_sender(self):
        return self.sender

    def set_sender(self, sender):
        self.sender = sender

    def get_receiver(self):
        return self.receiver

    def set_receiver(self, receiver):
        self.receiver = receiver

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def is_valid(self):
        return self.sender.is_valid() and self.receiver.is_valid()

    def execute_transaction(self):
        if self.sender.get_balance() > self.get_amount():
            if not (self.get_status() == "complete"):
                self.sender.set_balance(self.sender.get_balance() - self.get_amount())
                self.receiver.set_balance(self.receiver.get_balance() + self.get_amount())
                self.set_status("complete")
        else:
            self.set_status("rejected")
            return "Transaction rejected. Please check your account balance."

    def reverse_transaction(self):
        if self.get_status() == "complete":
            self.set_status("reversed")
            reversal = Transfer(self.get_receiver(), self.get_sender(), self.get_amount())
            reversal.execute_transaction()