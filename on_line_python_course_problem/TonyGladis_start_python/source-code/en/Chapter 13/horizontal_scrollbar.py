# This program demonstrates a Listbox with a horizontal scrollbar.
import tkinter

class HorizontalScrollbarExample:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create a frame for the Listbox and vertical scrollbar.
        self.listbox_frame = tkinter.Frame(self.main_window)
        self.listbox_frame.pack(padx=20, pady=20)

        # Create a Listbox widget in the listbox_frame.
        self.listbox = tkinter.Listbox(
            self.listbox_frame, height=0, width=30)
        self.listbox.pack(side='top')
        
        # Create a horizontal Scrollbar in the listbox_frame.
        self.scrollbar = tkinter.Scrollbar(
            self.listbox_frame, orient=tkinter.HORIZONTAL)
        self.scrollbar.pack(side='bottom', fill=tkinter.X)

        # Configure the Scrollbar and Listbox to work together.
        self.scrollbar.config(command=self.listbox.xview)
        self.listbox.config(xscrollcommand=self.scrollbar.set)

        # Create a list.
        data = [
            'The Burj Khalifa building is 2717 feet tall.',
            'The Shanghai Tower is 2073 feet tall.',
            'The Abraj Al-Bait Clock Tower is 1971 feet tall.',
            'The Ping An Finance Center is 1965 feet tall.']

        # Populate the Listbox with the data.
        for element in data:
            self.listbox.insert(tkinter.END, element)

        # Start the main loop.
        tkinter.mainloop()

# Create an instance of the HorizontalScrollbarExample class.
if __name__ == '__main__':
    scrollbar_example = HorizontalScrollbarExample()