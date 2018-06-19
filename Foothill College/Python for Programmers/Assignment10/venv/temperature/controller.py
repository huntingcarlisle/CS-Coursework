import tkinter
import model
import view

class Controller:

    """
    The CONTROLLER for an app that follows the Model/View/Controller architecture.
    When the user presses a Button on the View, this Controller calls the appropriate methods in the Model.
    The Controller handles all communication between the Model and the View.
    """

    def __init__(self):

        """
        This starts the Tk framework up, instantiates the Model (a Temperature object), instantiates the View (a MyFrame object), and starts the event loop that waits for the user to press a Button on the View.
        """

        root = tkinter.Tk()
        self.view = view.MyFrame(self)
        self.view.mainloop()

    def fahrenheitButtonPressed(self):

        """
        Python calls this method when the user presses the fahrenheitButton in the View.
        """
        self.model = model.Temperature(self.view.temperatureEntry.get())
        self.view.labelForOutput["text"] = self.model.fahrenheitConversion()

    def celsiusButtonPressed(self):
        """
        Python calls this method when the user presses the celsiusButton in the View.
        """
        self.model = model.Temperature(self.view.temperatureEntry.get())
        self.view.labelForOutput["text"] = self.model.celsiusConversion()

if __name__ == "__main__":
    c = Controller()