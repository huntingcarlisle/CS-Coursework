class Temperature:

    """
    class temperature is the MODEL for the temperature conversion GUI.

    Takes in a user inputted temperature from the controller and converts it to either celsius or fahrenheit

    """

    def __init__(self, temperature):
        self.temperature = temperature


    def fahrenheitConversion(self):
        return ((9.0/5.0) * int(self.temperature)) + 32.0

    def celsiusConversion(self):
        return (5.0 / 9.0) * (int(self.temperature) - 32.0)

    def __str__(self):
        return str(self.temperature)