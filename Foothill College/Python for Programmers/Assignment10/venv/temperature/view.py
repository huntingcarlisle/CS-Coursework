import tkinter

class MyFrame(tkinter.Frame):

    """
    class View is the VIEW for a simple program that exemplifies the Model/View/Controller architecture.
    This View class is a tkinter.
    Frame that contains two Buttons and a Label.
    One Button increments a counter and the other Button quits.
    The Label displays the current value of the counter.
    Notice that the View never contains a reference to the Model, but it does contain a reference to the Controller.
    """

    def __init__(self, controller):
        tkinter.Frame.__init__(self)
        self.pack()
        self.controller = controller    # saves a reference to the controller so that we can call methods
                                        # on the controller object when the user generates events

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

