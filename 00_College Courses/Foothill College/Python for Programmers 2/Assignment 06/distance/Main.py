import tkinter

class Distance:
    """
    Class Distance is the MODEL for a program that allows a user to convert between kilometers and miles.
    One object of class Distance is a distance value in kilometers.
    """

    def __init__(self, distance):
        """
        Initialize a temperature object.
        """
        self.distance = distance

    def mile_conversion(self):
        """
        Return kilometer value converted to miles.
        """
        return int(self.distance) * 0.6213711922373

    def __str__(self):
        return str(self.distance)


class MyFrame(tkinter.Frame):
    """
    Class MyFrame is the VIEW for a program that allows a user to convert between kilometer and mile distances.
    One object of this class is a tkinter frame that contains a text Entry Field, two Buttons and an output Label:
    - The text entry field takes user input distance.
    - The convert button converts the inputted value to miles.
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

        self.distance_entry = tkinter.Entry()
        self.distance_entry.insert(0, "enter a distance")
        self.distance_entry.pack({"side": "left"})

        self.distance_button = tkinter.Button(self)
        self.distance_button["text"] = "Convert"
        self.distance_button["command"] = self.controller.button_pressed
        self.distance_button.pack({"side": "left"})

        self.quit_button = tkinter.Button(self)
        self.quit_button["text"] = "Quit"
        self.quit_button["command"] = self.quit
        self.quit_button.pack({"side": "left"})

        self.output_label = tkinter.Label(self)
        self.output_label["text"] = 0
        self.output_label.pack({"side": "left"})


class Controller:
    """
    Class Controller is the CONTROLLER for a program that allows a user to convert between kilometer and mile distances.
    Serves as an interface between MODEL (a Temperature object) and VIEW (a MyFrame object)
    """

    def __init__(self):
        """
        Starts the Tk framework, instantiates the View (a MyFrame object),
        and starts the event loop that waits for the user to press a Button on the View.
        """
        root = tkinter.Tk()
        self.model = Distance(0)
        self.view = MyFrame(self)
        self.view.mainloop()

    def button_pressed(self):
        """
        Instantiate the Model (a Distance object), and convert to miles.
        """
        self.model = Distance(self.view.distance_entry.get())
        self.view.output_label["text"] = str(self.view.distance_entry.get()) + " kilometers is " + str(self.model.mile_conversion()) + " miles."


if __name__ == "__main__":
    c = Controller()