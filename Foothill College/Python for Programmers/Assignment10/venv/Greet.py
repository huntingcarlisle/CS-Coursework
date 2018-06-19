import tkinter

""" sets up a gui that accepts the user's name and greets her when 
    a button is pressed
"""


class MyFrame(tkinter.Frame):
    def __init__(self):
        """ Initializes the Frame by putting the widgets on it """
        tkinter.Frame.__init__(self)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        """ Instantiates all of the widgets and places them onto
            the frame
        """
        self.nameEntry = tkinter.Entry()
        self.nameEntry.insert(0, "your name here")
        self.nameEntry.pack({"side": "left"})

        self.quitButton = tkinter.Button(self)
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] = self.quit
        self.quitButton.pack({"side": "left"})

        self.hiButton = tkinter.Button(self)
        self.hiButton["text"] = "Hello",
        self.hiButton["command"] = self.sayHi
        self.hiButton.pack({"side": "left"})

        self.greeting = tkinter.Label(self)
        self.greeting.pack({"side": "left"})

    def sayHi(self):
        """ greets the user by taking text from the nameEntry widget
            and putting it into the greeting widget
        """
        self.greeting["text"] = "Hello " + self.nameEntry.get()


if __name__ == "__main__":
    root = tkinter.Tk()
    app = MyFrame()
    app.mainloop()