import tkinter
import model
import view


class Controller:
    """
<<<<<<< HEAD
    Class Temperature is the CONTROLLER for a program that allows a user to convert between celsius and fahrenheit temperatures.
    Serves as an interface between MODEL (a Temperature object) and VIEW (a MyFrame object)
=======
    When the user presses a Button on the View, this Controller calls the appropriate methods in the Model.
>>>>>>> 9efdd476a5ccc96bfdc91150865af4d0a45a9a15
    """

    def __init__(self):
        """
<<<<<<< HEAD
        Starts the Tk framework, instantiates the View (a MyFrame object),
        and starts the event loop that waits for the user to press a Button on the View.
=======
        This starts the Tk framework up, instantiates the Model (a Temperature object),
            instantiates the View (a MyFrame object),
            and starts the event loop that waits for the user to press a Button on the View.
>>>>>>> 9efdd476a5ccc96bfdc91150865af4d0a45a9a15
        """
        root = tkinter.Tk()
        self.model = model.Temperature(0)
        self.view = view.MyFrame(self)
        self.view.mainloop()

    def fahrenheitButtonPressed(self):
        """
        Instantiate the Model (a Temperature object), and convert to fahrenheit.
        """
        self.model = model.Temperature(self.view.temperatureEntry.get())
<<<<<<< HEAD
        self.view.labelForOutput["text"] = str(self.view.temperatureEntry.get()) + " degrees celsius is " + str(self.model.fahrenheitConversion()) + " degrees fahrenheit."
=======
        self.view.labelForOutput["text"] = str(self.view.temperatureEntry.get()) + "\N{DEGREE SIGN} celsius is " + str(self.model.fahrenheitConversion()) + "\N{DEGREE SIGN} fahrenheit."
>>>>>>> 9efdd476a5ccc96bfdc91150865af4d0a45a9a15

    def celsiusButtonPressed(self):
        """
        Instantiate the Model (a Temperature object), and convert to celsius.
        """
        self.model = model.Temperature(self.view.temperatureEntry.get())
<<<<<<< HEAD
        self.view.labelForOutput["text"] = str(self.view.temperatureEntry.get()) + " degrees fahrenheit is " + str(self.model.celsiusConversion()) + " degrees celsius."

=======
        self.view.labelForOutput["text"] = str(self.view.temperatureEntry.get()) + "\N{DEGREE SIGN} fahrenheit is " + str(self.model.celsiusConversion()) + "\N{DEGREE SIGN} celsius."
>>>>>>> 9efdd476a5ccc96bfdc91150865af4d0a45a9a15

if __name__ == "__main__":
    c = Controller()