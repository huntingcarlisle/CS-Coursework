class BankAccount(object):
    """
    One object of class BankAccount is a representation of one account holder
    """
    def __init__(self, name):
        """
        Initialize a BankAccount object with a name, balance of 1000, and status of open.
        """
        self.name = name
        self.balance = 1000.0
        self.status = "open"

    def get_name(self):
        """Safely access self.name outside of the class"""
        return self.name

    def get_balance(self):
        """Safely access self.balance outside of the class"""
        return self.balance

    def get_status(self):
        """Safely access self.status outside of the class"""
        return self.status

    def set_balance(self, balance):
        """Set self.balance outside of the class"""
        self.balance = balance

    def set_status(self, status):
        """Set self.status outside of the class"""
        self.status = status

    def deposit(self, amount):
        """Deposit money into the account"""
        self.balance += amount

    def display_balance(self):
        """Returns string containing balance information"""
        return f'Your balance is {self.get_balance()}.'

    def is_valid(self):
        """Account is open and has a balance greater than 0"""
        return self.status == "open" and self.balance > 0

    def close_account(self):
        """Close account"""
        self.status = "closed"