class Temperature:
    """
<<<<<<< HEAD
    Class Temperature is the MODEL for a program that allows a user to convert between celsius and fahrenheit temperatures.
    One object of class Temperature is a temperature value, either fahrenheit or celsius.
=======
    class temperature is the MODEL for the temperature conversion GUI.

    Takes in a user inputted temperature from the controller and converts it to either celsius or fahrenheit

>>>>>>> 9efdd476a5ccc96bfdc91150865af4d0a45a9a15
    """

    def __init__(self, temperature):
        """
        Initialize a temperature object.
        """
        self.temperature = temperature

<<<<<<< HEAD
=======

>>>>>>> 9efdd476a5ccc96bfdc91150865af4d0a45a9a15
    def fahrenheitConversion(self):
        """
        Return temperature value converted to fahrenheit.
        """
        return ((9.0/5.0) * int(self.temperature)) + 32.0

    def celsiusConversion(self):
<<<<<<< HEAD
        """
        Return temperature value converted to celsius.
        """
=======
>>>>>>> 9efdd476a5ccc96bfdc91150865af4d0a45a9a15
        return (5.0 / 9.0) * (int(self.temperature) - 32.0)

    def __str__(self):
        return str(self.temperature)