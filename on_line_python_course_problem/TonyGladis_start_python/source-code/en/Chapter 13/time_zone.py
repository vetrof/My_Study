# This program allows the user to see the time zone
# for a selected city.
import tkinter

class TimeZone:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title('Time Zones')

        # Create the widgets.
        self.__build_prompt_label()
        self.__build_listbox()
        self.__build_output_frame()
        self.__build_quit_button()
       
        # Start the main loop.
        tkinter.mainloop()
    
    # This method creates the prompt_label widget.
    def __build_prompt_label(self):
        self.prompt_label = tkinter.Label(
            self.main_window, text='Select a City')
        self.prompt_label.pack(padx=5, pady=5)

    # This method creates and populates the city_listbox widget.
    def __build_listbox(self):
        # Create a list of city names.
        self.__cities = ['Denver', 'Honolulu', 'Minneapolis',
                          'New York', 'San Francisco']
        
        # Create and pack the Listbox.
        self.city_listbox = tkinter.Listbox(
            self.main_window, height=0, width=0)
        self.city_listbox.pack(padx=5, pady=5)

        # Bind a callback function to the Listbox.
        self.city_listbox.bind(
            '<<ListboxSelect>>', self.__display_time_zone)

        # Populate the Listbox.
        for city in self.__cities:
            self.city_listbox.insert(tkinter.END, city)
    
    # This method creates the output_frame and its contents.
    def __build_output_frame(self):
        # Create the frame.
        self.output_frame = tkinter.Frame(self.main_window)
        self.output_frame.pack(padx=5)

        # Create the Label that reads "Time Zone:".
        self.output_description_label = tkinter.Label(
            self.output_frame, text='Time Zone:')
        self.output_description_label.pack(
            side='left', padx=(5, 1), pady=5)

        # Create a StringVar variable to hold the time zone name.
        self.__timezone = tkinter.StringVar()

        # Create the Label that displays the time zone name.
        self.output_label = tkinter.Label(
            self.output_frame, borderwidth=1, relief='solid',
            width=15, textvariable=self.__timezone)
        self.output_label.pack(side='right', padx=(1, 5), pady=5)
    
    # This method creates the Quit button.
    def __build_quit_button(self):
        self.quit_button = tkinter.Button(
            self.main_window, text='Quit',
            command=self.main_window.destroy)
        self.quit_button.pack(padx=5, pady=5)
    
    # Callback function for the city_listbox widget.
    def __display_time_zone(self, event):
        # Get the current selections.
        index = self.city_listbox.curselection()

        # Get the city.
        city = self.city_listbox.get(index[0])

        # Determine the time zone.
        if city == 'Denver':
            self.__timezone.set('Mountain')
        elif city == 'Honolulu':
            self.__timezone.set('Hawaii-Aleutian')
        elif city == 'Minneapolis':
            self.__timezone.set('Central')
        elif city == 'New York':
            self.__timezone.set('Eastern')
        elif city == 'San Francisco':
            self.__timezone.set('Pacific')

# Create an instance of the TimeZoneclass.
if __name__ == '__main__':
    time_zone = TimeZone()