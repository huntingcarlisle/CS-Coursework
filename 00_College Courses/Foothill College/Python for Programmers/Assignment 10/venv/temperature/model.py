class Temperature:
    """
    Class Temperature is the MODEL for a program that allows a user to convert between celsius and fahrenheit temperatures.
    One object of class Temperature is a temperature value, either fahrenheit or celsius.
    """

    def __init__(self, temperature):
        """
        Initialize a temperature object.
        """
        self.temperature = temperature

    def fahrenheitConversion(self):
        """
        Return temperature value converted to fahrenheit.
        """
        return ((9.0/5.0) * int(self.temperature)) + 32.0

    def celsiusConversion(self):
        """
        Return temperature value converted to celsius.
        """
        return (5.0 / 9.0) * (int(self.temperature) - 32.0)

    def __str__(self):
        return str(self.temperature)