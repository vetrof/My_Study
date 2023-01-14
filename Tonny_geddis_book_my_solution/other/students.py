import os

def main():

    name_for_delete = input('name for delete - ')

    file_orig = open('students.txt', 'r')
    file_temp = open('students_tmp.txt', 'w')
    name_on_file = file_orig.readline().rstrip('\n')
    rate_on_file = file_orig.readline().rstrip('\n')

    while name_on_file != '':
        if name_for_delete != name_on_file:
            file_temp.write(name_on_file + '\n')
            file_temp.write(rate_on_file + '\n')
        name_on_file = file_orig.readline().rstrip('\n')
        rate_on_file = file_orig.readline().rstrip('\n')

    file_orig.close()
    file_temp.close()

    os.remove('students.txt')
    os.rename('students_tmp.txt', 'students.txt')

    print('дело сделано')


if __name__ == '__main__':
    main()
