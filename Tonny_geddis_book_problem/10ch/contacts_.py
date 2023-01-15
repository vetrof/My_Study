from objects import contacts

def main():

    contacts1 = contacts.Contacts('vitalik', 'astana', 42, 777)
    contacts2 = contacts.Contacts('nastya', 'astana', 38, 999)
    contacts3 = contacts.Contacts('misha', 'astana', 1, 0)

    display_info(contacts1)
    display_info(contacts2)
    display_info(contacts3)


def display_info(person):
    print(person.get_name())
    print(person.get_adress())
    print(person.get_age())
    print(person.get_phone())
    print()







if __name__ == '__main__':
    main()