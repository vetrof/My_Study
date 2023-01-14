# This program gets the user's selection from a Listbox.
import tkinter
import tkinter.messagebox

class ListBoxSelection:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create a Listbox widget.
        self.dog_listbox = tkinter.Listbox(
            self.main_window, width=0, height=0)
        self.dog_listbox.pack(padx=10, pady=5)

        # Create a list with the names of dog breeds.
        dogs = ['Labrador', 'Poodle', 'Great Dane', 'Terrier']

        # Populate the Listbox with the list contents.
        for dog in dogs:
            self.dog_listbox.insert(tkinter.END, dog)
        
        # Create a button to get the selected item.
        self.get_button = tkinter.Button(
            self.main_window, text='Get Item',
            command=self.__retrieve_dog)
        self.get_button.pack(padx=10, pady=5)

        # Start the main loop.
        tkinter.mainloop()
    
    def __retrieve_dog(self):
        # Get the index of the selected item.
        indexes = self.dog_listbox.curselection()

        # If an item is selected, display it.
        if (len(indexes) > 0):
            tkinter.messagebox.showinfo(
                message=self.dog_listbox.get(indexes[0]))
        else:
            tkinter.messagebox.showinfo(
                message='No item selected.')
    
# Create an instance of the ListBoxSelection class.
if __name__ == '__main__':
    listbox_selection = ListBoxSelection()