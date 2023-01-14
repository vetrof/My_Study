from objects import eployee

def main():

    man1 = eployee.Employee('suzan', 47899, 'buhgalter', 'vice president')
    man2 = eployee.Employee('mark', 39119, 'it', 'programist')
    man3 = eployee.Employee('joy', 81774, 'create', 'ingener')

    display_info(man1)
    display_info(man2)
    display_info(man3)

def display_info(man):
    print('name:', man.get_name())
    print('id:  ', man.get_id())
    print('dept:', man.get_dept())
    print('job: ', man.get_job())
    print()








if __name__ == '__main__':
    main()