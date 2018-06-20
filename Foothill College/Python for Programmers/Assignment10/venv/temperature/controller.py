import tkinter
import model
import view

class Controller:

    """
    When the user presses a Button on the View, this Controller calls the appropriate methods in the Model.
    """

    def __init__(self):

        """
        This starts the Tk framework up, instantiates the Model (a Temperature object),
            instantiates the View (a MyFrame object),
            and starts the event loop that waits for the user to press a Button on the View.
        """

        root = tkinter.Tk()
        self.view = view.MyFrame(self)
        self.view.mainloop()

    def fahrenheitButtonPressed(self):

        """
        Python calls this method when the user presses the fahrenheitButton in the View.
        """
        self.model = model.Temperature(self.view.temperatureEntry.get())
        self.view.labelForOutput["text"] = str(self.view.temperatureEntry.get()) + "\N{DEGREE SIGN} celsius is " + str(self.model.fahrenheitConversion()) + "\N{DEGREE SIGN} fahrenheit."

    def celsiusButtonPressed(self):
        """
        Python calls this method when the user presses the celsiusButton in the View.
        """
        self.model = model.Temperature(self.view.temperatureEntry.get())
        self.view.labelForOutput["text"] = str(self.view.temperatureEntry.get()) + "\N{DEGREE SIGN} fahrenheit is " + str(self.model.celsiusConversion()) + "\N{DEGREE SIGN} celsius."

if __name__ == "__main__":
    c = Controller()