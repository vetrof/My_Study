# This program displays a label with a border.
import tkinter

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create a Label widget.
        self.label = tkinter.Label(self.main_window,
                                   text='Hello World!',
                                   borderwidth=4,
                                   relief='solid')

        # Call the Label widget's pack method.
        self.label.pack(padx=20, pady=20)

        # Enter the tkinter main loop.
        tkinter.mainloop()

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()