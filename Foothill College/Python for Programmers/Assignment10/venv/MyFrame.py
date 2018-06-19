import tkinter


class MyFrame(tkinter.Frame):

    """
    class MyFrame is a tkinter.Frame that contains two Buttons and a Label. One Button increments a counter that is displayed on the Label and the other Button quits the application.
    """

    def __init__(self):
        tkinter.Frame.__init__(self)
        self.pack()
        self.counter = 0   # i) initialize the counter

        self.incrementButton = tkinter.Button(self)
        self.incrementButton["text"] = "Increment"
        self.incrementButton["command"] = self.addOne
        # ii) the statement above attaches the event handler addOne() to the incrementButton
        self.incrementButton.pack({"side": "left"})

        self.labelForOutput = tkinter.Label(self)
        self.labelForOutput["text"] = 0
        self.labelForOutput.pack({"side": "left"})

        self.quitButton = tkinter.Button(self)
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] =  self.quit
        # iii) the statement above attaches the event handler self.quit() to the incrementButton
        self.quitButton.pack({"side": "left"})

    """ 
    Python calls this method when the user clicks the incrementButton.
    This is called an event handler or a callback.
    """
    def addOne(self):
        self.counter = self.counter +1
        self.labelForOutput["text"] = self.counter