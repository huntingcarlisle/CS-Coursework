"""
Hunter Carlisle | Foothill College Fall 2018 | Lab Six

This program converts distances in kilometers to miles.

"""

from tkinter import Tk, BOTH, RIGHT
from tkinter.ttk import Frame, Label, Entry, Button


class KilometerToMile(Frame):
    def __init__(self):
        """ Starts the Tk framework and instantiates the view. """
        super().__init__()

        self.master.title("Kilometer to Miles Converter")
        self.km_entry = Entry()
        self.km_entry.insert(0, "Enter a distance in Kilometers.")
        self.km_entry.pack(fill=BOTH, padx=5, expand=True)
        self.conversion_lbl = Label(self, borderwidth=1)
        self.conversion_lbl.pack(fill=BOTH, padx=5, expand=True)
        self.pack(fill=BOTH, expand=True)
        self.quit_btn = Button(self, text="Quit", command=self.quit)
        self.quit_btn.pack(side=RIGHT, padx=5, pady=5)
        self.convert_btn = Button(self, text="Convert",
                                  command=self.button_pressed)
        self.convert_btn.pack(side=RIGHT)

    def button_pressed(self):
        """ Validates input kilometer and prints result. """
        try:
            kilo_value = float(self.km_entry.get())
            if kilo_value >= 0:
                mile_value = self.to_mile(kilo_value)
                self.conversion_lbl["text"] = \
                    self.display(kilo_value, mile_value)
            else:
                raise Exception
        except:
            self.conversion_lbl["text"] = "Invalid input. Please try again."

    @staticmethod
    def to_mile(kilo_value):
        """ Return kilometer value converted to miles. """
        return kilo_value * 0.6213711922373

    def display(self, kilo_value, mile_value):
        """ Returns conversion result as a pretty string. """
        kilo_value = self.format_float(kilo_value)
        mile_value = self.format_float(mile_value)
        return str(kilo_value) + " kilometers is " + str(mile_value) + " miles."

    @staticmethod
    def format_float(value):
        """ Formats floating point to 2 decimal places. """
        return float("{0:.2f}".format(value))


def main():
    root = Tk()
    root.geometry("400x100")
    ui = KilometerToMile()
    root.mainloop()


if __name__ == '__main__':
    main()
