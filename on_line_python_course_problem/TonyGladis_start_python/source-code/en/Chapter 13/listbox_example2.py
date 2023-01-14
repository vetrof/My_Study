# This program demonstrates a simple Listbox.
import tkinter

class ListboxExample:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create a Listbox widget.
        self.listbox = tkinter.Listbox(
            self.main_window, height=0, width=0)
        self.listbox.pack(padx=10, pady=10)

        # Create a list with the days of the week.
        days = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 
                'Sunday']

        # Populate the Listbox with the data.
        for day in days:
            self.listbox.insert(tkinter.END, day)

        # Start the main loop.
        tkinter.mainloop()

# Create an instance of the ListboxExample class.
if __name__ == '__main__':
    listbox_example = ListboxExample()