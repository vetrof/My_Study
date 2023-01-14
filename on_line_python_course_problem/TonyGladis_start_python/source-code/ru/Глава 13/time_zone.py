# Эта программа позволяет пользователю увидеть 
# часовой пояс выбранного города.
import tkinter

class TimeZone:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()
        self.main_window.title('Часовые пояса')

        # Создать виджеты.
        self.__build_prompt_label()
        self.__build_listbox()
        self.__build_output_frame()
        self.__build_quit_button()

        # Запустить главный цикл.
        tkinter.mainloop()

    # Этот метод создает виджет prompt_label с надписью.
    def __build_prompt_label(self):
        self.prompt_label = tkinter.Label(
        self.main_window, text='Выберите город')
        self.prompt_label.pack(padx=5, pady=5)

    # Этот метод создает и заполняет виджет city_listbox городами.
    def __build_listbox(self):
        # Создать список названий городов.
        self.__cities = ['Денвер', 'Гонолулу', 'Миннеаполис',
                        'Нью-Йорк', 'Сан-Франциско']

        # Создать и упаковать виджет Listbox.
        self.city_listbox = tkinter.Listbox(
            self.main_window, height=0, width=0)
        self.city_listbox.pack(padx=5, pady=5)

        # Привязать функцию обратного вызова к виджету Listbox.
        self.city_listbox.bind(
            '<<ListboxSelect>>', self.__display_time_zone)

        # Заполнить виджет Listbox.
        for city in self.__cities:
            self.city_listbox.insert(tkinter.END, city)

    # Этот метод создает рамку output_frame и ее содержимое.
    def __build_output_frame(self):
        # Создать рамку.
        self.output_frame = tkinter.Frame(self.main_window)
        self.output_frame.pack(padx=5)

        # Создать  виджет Label с надписью "Часовой пояс:".
        self.output_description_label = tkinter.Label(
            self.output_frame, text='Часовой пояс:')
        self.output_description_label.pack(
            side='left', padx=(5, 1), pady=5)

        # Создать переменную StringVar для хранения имени часового пояса.
        self.__timezone = tkinter.StringVar()

        # Создать метку Label, которая выводит имя часового пояса.
        self.output_label = tkinter.Label(
            self.output_frame, borderwidth=1, relief='solid',
            width=15, textvariable=self.__timezone)
        self.output_label.pack(side='right', padx=(1, 5), pady=5)

    # Этот метод создает кнопку 'Выйти'.
    def __build_quit_button(self):
        self.quit_button = tkinter.Button(
            self.main_window, text='Выйти',
            command=self.main_window.destroy)
        self.quit_button.pack(padx=5, pady=5)
		
    # Функция обратного вызова для виджета city_listbox.
    def __display_time_zone(self, event):
        # Получить текущие варианты выбора.
        index = self.city_listbox.curselection()

        # Получить город.
        city = self.city_listbox.get(index[0])

        # Определить веременной пояс.
        if city == 'Денвер':
            self.__timezone.set('Горный')
        elif city == 'Гонолулу':
            self.__timezone.set('Гавайско-алеутский')
        elif city == 'Миннеаполис':
            self.__timezone.set('Центральный')
        elif city == 'Нью-Йорк':
            self.__timezone.set('Восточный')
        elif city == 'Сан-Франциско':
            self.__timezone.set('Тихоокеанский')

# Создать экземпляр класса TimeZone
if __name__ == '__main__':
    time_zone = TimeZone()