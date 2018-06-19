"""
This main program creates a MyFrame object that contains two Buttons and a Label.
"""
import tkinter
import MyFrame                # contains class MyFrame
if __name__ == "__main__":
    root = tkinter.Tk()
    view = MyFrame.MyFrame()  # puts the Frame onto the user's screen
    view.mainloop()
