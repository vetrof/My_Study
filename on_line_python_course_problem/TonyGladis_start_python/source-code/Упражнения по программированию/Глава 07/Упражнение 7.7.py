# Упражнение по программированию 7.7

# Экзамен на получение водительских прав

# Программа исходит из того, что решения испытуемого перечислены  
# построчно, т. е. каждая строка содержит ответ испытуемого на вопрос,
# но без предваряющего ответ номера вопроса. Предполагается, что   
# ответы испытуемого расположены в порядке следования вопросов.

def main():
    # Определить переменные
    solution = ['A', 'C', 'A', 'A', 'D',
                'B', 'C', 'A', 'C', 'B',
                'A', 'D', 'C', 'A', 'D',
                'C', 'B', 'B', 'D', 'A']
    correct_count = 0
    incorrect_count = 0
    incorrect_questions = []
    counter = 0
    
    try:
        # Открыть файл для чтения.
		# Файл находится в подпапке data
        input_file = open(r'data\student_solution.txt', 'r')
        
        # Прочитать все строки из файла в список.
        student_solutions = input_file.readlines()
        
        # Отсечь замыкающий символ '\n' у всех элементов списка.
        for i in range(len(student_solutions)):
            student_solutions[i] = student_solutions[i].rstrip('\n')

        # Сравнить решение испытуемого с правильным решением и
        # обновить соответствующие счетчики.
        for i in range(len(student_solutions)):
            if student_solutions[i] == solution[i]:
                correct_count += 1
            else:
                incorrect_count += 1
                incorrect_questions.append(str(i + 1))

        # Определить, прошел ли испытуемый экзамен, и показать результат.
        if correct_count >= 15:
            print('Поздравляем!! Вы прошли экзамен.')
        else:
            print('Сожалеем, но Вы не прошли экзамен.')

        # Показать подробную информацию об экзамене.
        print('Число вопросов, на которые Вы ответили правильно:', \
              correct_count)
        print('Число вопросов, на которые Вы ответили не правильно:', \
              incorrect_count)
        
        # Определить, ответил ли испытуемый хоть один раз неправильно.
        if incorrect_count > 0:
            # Показать номера вопросов, на которые испытуемый не ответил.
            print('Вопросы, на которые Вы ответили неправильно:', end='')
            while counter < incorrect_count:
                print(incorrect_questions[counter], end='')
                if counter + 1 < incorrect_count:
                    print (', ', end='')
                counter += 1
                
    # Обработать любые ошибки, которые могут произойти.
    except IOError:
        print('Файл не найден')
    except IndexError:
        print('Ошибка индексации')
    except:
        print('Произошла ошибка')

# Вызвать главную функцию.
main()