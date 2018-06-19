class Counter:

    """
    class Counter is the MODEL for a simple program that exemplifies the Model/View/Controller architecture. It just maintains a counter that starts at 0 and is incremented each time the inc() method is called.

    In a real MVC app, the Model would contain all the business logic. Note that the Model never contains a reference to the View.
    """

    def __init__(self):
        self.counter = 0

    def inc(self):
        self.counter = self.counter+1

    def dec(self):
        self.counter = self.counter-1

    def __str__(self):
        return str(self.counter)