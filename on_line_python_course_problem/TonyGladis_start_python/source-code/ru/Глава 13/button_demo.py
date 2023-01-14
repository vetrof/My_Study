# Эта программа демонстрирует виджет Button.
# Когда пользователь нажимает кнопку Button, 
# на экран выводится информационное диалоговое окно.

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Создать виджет главного окна.
        self.main_window = tkinter.Tk()

        # Создать виджет Button widget.  
        # На кнопке должен появиться текст 'Нажми меня!'. 
        # Когда пользователь нажимает кнопку, 
        # должен быть исполнен метод do_something.
        self.my_button = tkinter.Button(self.main_window,
                                        text='Нажми меня!',
                                        command=self.do_something)

        # Упаковать виджет Button.
        self.my_button.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

    # Метод do_something является функцией обратного 
    # вызова для виджета Button.

    def do_something(self):
        # Показать информационное диалоговое окно.
        tkinter.messagebox.showinfo('Реакция',
                                    'Благодарю, что нажали кнопку.')

# Создать экземпляр класса MyGUI.
if __name__ == '__main__':
    my_gui = MyGUI()