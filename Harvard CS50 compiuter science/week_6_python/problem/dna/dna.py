import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("not correct argv")

    # Read database csv file into a variable
    # извлекаем пути к файлам и аргументов запуска
    csv_path = sys.argv[1]
    seq_path = sys.argv[2]

    # создаем пустой словарь для пары {субсеквенция: макс повторений}
    subseq_dict = {}  # словарь с названиями последовательностей srt
    nme_dict_csv = []  # этот список со словарями нужен для финального матчинга

    # открываем csv файл и извлекаем субсеквенции
    with open(csv_path, 'r') as csv_file:
        csv_file = csv.reader(csv_file)

        # добавляем из csv файла srt последовательности и количество
        # повторений у человека из списка
        for i in csv_file:
            for n in range(len(i) - 1):
                subseq_dict[i[n+1]] = 0
            break

    # добавляем словари в список nme_dict_csv (имена и количество повторений srt)
    with open(csv_path, 'r') as csv_file:
        name_dict = csv.DictReader(csv_file)
        for i in name_dict:
            nme_dict_csv.append(i)

    # Read DNA sequence file into a variable
    # создаем и наполняем стринг переменную dna_seq данными из файла днк
    dna_seq = ''
    with open(seq_path, 'r') as txt_file:
        for i in txt_file:
            dna_seq += i

    # Find longest match of each STR in DNA sequence
    # получаем максимальную длину повторений для каждой последовательности
    # и записываем результат в словарик subseq_dict
    for i in subseq_dict:
        # maximum = 0
        maximum = longest_match(dna_seq, i)
        subseq_dict[i] = maximum

    # Check database for matching profiles
    # создаем словарик и заполняем его названиями последовательноей
    # и нулевыми значениями ключей
    score = {}
    for i in nme_dict_csv:
        score[i['name']] = 0

    # проверяем совпадения из файла csv и колва повторений в файле днк
    for i in subseq_dict:
        for n in nme_dict_csv:

            # если есть совпадение, то добавляем каунтер
            if int(subseq_dict[i]) == int(n[i]):
                score[n['name']] += 1

    for i in score:

        # если есть человек с количеством совпадений по количеству str,
        # то объявляем совпадение
        if score[i] == len(subseq_dict):
            print('matched: ', i)
            break

    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
