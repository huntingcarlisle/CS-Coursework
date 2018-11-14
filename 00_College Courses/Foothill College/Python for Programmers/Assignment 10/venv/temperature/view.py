import tkinter


class MyFrame(tkinter.Frame):
    """
    Class MyFrame is the VIEW for a program that allows a user to convert between celsius and fahrenheit temperatures.
    One object of this class is a tkinter frame that contains a text Entry Field, three Buttons and an output Label:
    - The text entry field takes user input temperature.
    - The convert to fahrenheit and celsius buttons convert the inputted value, respectively.
    - The quit button exits the program
    - The Label displays the converted value
    """

    def __init__(self, controller):
        """
        Initialize a MyFrame object with a reference to the controller object
        """
        tkinter.Frame.__init__(self)
        self.pack()
        self.controller = controller

        self.temperatureEntry = tkinter.Entry()
        self.temperatureEntry.insert(0, "enter a temperature")
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

