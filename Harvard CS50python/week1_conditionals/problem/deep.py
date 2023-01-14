# Ответ на Великий Вопрос Жизни, Вселенной и Вообще

print("What is the Answer to the Great Question of Life, "
      "the Universe, and Everything?", end='')

usr_input = input(' ').strip().lower()

match usr_input:
    case "42" | "forty two" | "forty-two":
        print("Yes")

    case _:
        print("No")
