# This program demonstrates a Listbox with both vertical
# and horizontal scrollbars.
import tkinter

class ScrollbarExample:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create an outer frame to hold the inner frame
        # and the horizontal scrollbar.
        self.outer_frame = tkinter.Frame(self.main_window)
        self.outer_frame.pack(padx=20, pady=20)

        # Create an inner frame for the Listbox and vertical scrollbar.
        self.inner_frame = tkinter.Frame(self.outer_frame)
        self.inner_frame.pack()

        # Create a Listbox widget in the inner_frame.
        self.listbox = tkinter.Listbox(
            self.inner_frame, height=5, width=30)
        self.listbox.pack(side='left')        
        
        # Create a vertical Scrollbar in the inner_frame.
        self.v_scrollbar = tkinter.Scrollbar(
            self.inner_frame, orient=tkinter.VERTICAL)
        self.v_scrollbar.pack(side='right', fill=tkinter.Y)

        # Create a horizontal Scrollbar in the outer_frame.
        self.h_scrollbar = tkinter.Scrollbar(
            self.outer_frame, orient=tkinter.HORIZONTAL)
        self.h_scrollbar.pack(side='bottom', fill=tkinter.X)

        # Configure the Scrollbars and the Listbox to work together.
        self.v_scrollbar.config(command=self.listbox.yview)
        self.h_scrollbar.config(command=self.listbox.xview)
        self.listbox.config(yscrollcommand=self.v_scrollbar.set,
                            xscrollcommand=self.h_scrollbar.set)

        # Create a list.
        data = [
            'The Burj Khalifa building is 2717 feet tall.',
            'The Shanghai Tower is 2073 feet tall.',
            'The Abraj Al-Bait Clock Tower is 1971 feet tall.',
            'The Ping An Finance Center is 1965 feet tall.',
            'The Goldin Finance Building is 1957 feet tall.',
            'The Lotte World Tower is 1819 feet tall.',
            'The One World Trade Center is 1776 feet tall.',]

        # Populate the Listbox with the data.
        for element in data:
            self.listbox.insert(tkinter.END, element)

        # Start the main loop.
        tkinter.mainloop()

# Create an instance of the ScrollbarExample class.
if __name__ == '__main__':
    scrollbar_example = ScrollbarExample()