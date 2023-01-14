
#US population
year_start = 1950
years_list = []
max_deviation = [0]
# print(max_deviation)

txt_file = open('data/USPopulation.txt', 'r')                     #open txt file
population_list = [int(i) for i in txt_file.readlines()]          #create list and integer stroke

for i in population_list:                                         #create years list 50' to 90'
    years_list.append(year_start)
    year_start += 1

for i in range(len(population_list)):                             #создаем список с приростом
    if i == 40:
        break
    dev = population_list[i + 1] - population_list[i]
    max_deviation.append(dev)

max_num = max(max_deviation)                                    #вычисляем максимальное изменение
index_max_num = max_deviation.index(max_num)                    #получаем индекс года
year_max_dev = years_list[index_max_num]                        #получаем год максимального прироста




print(max_num)
print(year_max_dev)







