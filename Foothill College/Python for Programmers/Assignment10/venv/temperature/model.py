class Temperature:

    """
    class Counter is the MODEL for a simple program that exemplifies the Model/View/Controller architecture. It just maintains a counter that starts at 0 and is incremented each time the inc() method is called.

    In a real MVC app, the Model would contain all the business logic. Note that the Model never contains a reference to the View.
    """

    def __init__(self, temperature):
        self.temperature = temperature

    def celsiusConversion(self):
        return (5.0 / 9.0) * (int(self.temperature) - 32.0)

    def fahrenheitConversion(self):
        return ((9.0/5.0) * int(self.temperature)) + 32.0

    def __str__(self):
        return str(self.temperature)