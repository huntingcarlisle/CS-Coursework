import tkinter

class MyFrame(tkinter.Frame):

    """
    class View is the VIEW for a simple program that exemplifies the Model/View/Controller architecture.
    This View class is a tkinter.
    Frame that contains three Buttons, a text entry field and a Label.
    The text entry field inputs a user temperature.
    One Button converts inputted temperature to fahrenheit, one button converts to celsius, and one button quits
    The Label displays the converted value of the inputted temperature.
    """

    def __init__(self, controller):
        tkinter.Frame.__init__(self)
        self.pack()
        self.controller = controller

        self.temperatureEntry = tkinter.Entry()
        self.temperatureEntry.insert(0, "Enter a temperature")
        self.temperatureEntry.pack({"side": "left"})

        self.fahrenheitButton = tkinter.Button(self)
        self.fahrenheitButton["text"] = "Convert to Fahrenheit"
        self.fahrenheitButton["command"] = self.controller.fahrenheitButtonPressed
        self.fahrenheitButton.pack({"side": "left"})

        self.celsiusButton = tkinter.Button(self)
        self.celsiusButton["text"] = "Convert to Celsius"
        self.celsiusButton["command"] = self.controller.celsiusButtonPressed
        self.celsiusButton.pack({"side": "left"})

        self.quitButton = tkinter.Button(self)
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] =  self.quit
        self.quitButton.pack({"side": "left"})

        self.labelForOutput = tkinter.Label(self)
        self.labelForOutput["text"] = 0
        self.labelForOutput.pack({"side": "left"})

