# This program demonstrates external padding.
import tkinter

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create two Label widgets with solid borders.
        self.label1 = tkinter.Label(self.main_window,
                                    text='Hello World!',
                                    borderwidth=1,
                                    relief='solid')
                                    
        self.label2 = tkinter.Label(self.main_window,
                         text='This is my GUI program.',
                         borderwidth=1,
                         relief='solid')

        # Display the Labels with 20 pixels of horizontal
        # and vertical external padding.
        self.label1.pack(padx=20, pady=20)
        self.label2.pack(padx=20, pady=20)

        # Enter the tkinter main loop.
        tkinter.mainloop()

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()
