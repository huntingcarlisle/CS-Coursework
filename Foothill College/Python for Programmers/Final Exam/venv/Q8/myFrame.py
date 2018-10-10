import tkinter

class MyFrame(tkinter.Frame):
    """
    class MyFrame is the View for a simple program that exemplifies the Model/View/Controller
    architecture. This View class is a tkinter.Frame that contains two Buttons and a Label. One Button
    notifies the Controller when it is pressed, and the other Button quits the app. The Label displays
    the current value of the counter. Notice that the View never contains a reference to the Model,
    but it does contain a reference to the Controller.
    """
    def __init__(self, controller):
        tkinter.Frame.__init__(self)
        self.pack()
        self.controller = controller    # saves a reference to the controller so that we can call methods
                                        # on the controller object when the user generates events
        self.incrementButton = tkinter.Button(self)
        self.incrementButton["text"] = "Increment"
        self.incrementButton["command"] = self.controller.buttonPressed
        self.incrementButton.pack({"side": "left"})

        self.labelForOutput = tkinter.Label(self)
        self.labelForOutput["text"] = 0
        self.labelForOutput.pack({"side": "left"})

        self.quitButton = tkinter.Button(self)
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] =  self.quit
        self.quitButton.pack({"side": "left"})
