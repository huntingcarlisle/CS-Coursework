import tkinter
import model
import view


class Controller:
    """
    Class Temperature is the CONTROLLER for a program that allows a user to convert between celsius and fahrenheit temperatures.
    Serves as an interface between MODEL (a Temperature object) and VIEW (a MyFrame object)
    """

    def __init__(self):
        """
        Starts the Tk framework, instantiates the View (a MyFrame object),
        and starts the event loop that waits for the user to press a Button on the View.
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
        self.view.labelForOutput["text"] = str(self.view.temperatureEntry.get()) + " degrees celsius is " + str(self.model.fahrenheitConversion()) + " degrees fahrenheit."

    def celsiusButtonPressed(self):
        """
        Instantiate the Model (a Temperature object), and convert to celsius.
        """
        self.model = model.Temperature(self.view.temperatureEntry.get())
        self.view.labelForOutput["text"] = str(self.view.temperatureEntry.get()) + " degrees fahrenheit is " + str(self.model.celsiusConversion()) + " degrees celsius."


if __name__ == "__main__":
    c = Controller()