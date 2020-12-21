"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import csv
import chardet


def get_data():

    # Берем кодировку

    with open('info_1.txt', 'rb') as t_f:
        cont_byts = t_f.read()

    encoding = chardet.detect(cont_byts)['encoding']


    # Взять зачения из файлов и добавить в list

    list_info = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    # os_prod_list = []
    # os_name_list = []
    # os_code_list = []
    # os_type_list = []

    info_list = [[], [], []]


    def seach_and_append(key_word, array):
        if el[:len(key_word)] == key_word:
                value = el[34:]
                array.append(value)


    for idx, info in enumerate(list_info):
        with open(info, encoding=encoding) as t_f:
            info_temp = t_f.read().split('\n')

        for el in info_temp:
            seach_and_append('Изготовитель системы', info_list[idx])  # os_prod_list,
            seach_and_append('Название ОС', info_list[idx])           # os_name_list,
            seach_and_append('Код продукта', info_list[idx])          # os_code_list,
            seach_and_append('Тип системы', info_list[idx])           # os_type_list,


    # создать главный список отчета

    main_data = [["Изготовитель системы", "Код продукта", "Название ОС", "Тип системы"], *info_list] # [os_prod_list, os_name_list, os_code_list, os_type_list,]

    return main_data


print(get_data())

def write_to_csv():
    data = get_data()

    with open('lesson_2_dz.csv', 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in data:
            f_n_writer.writerow(row)


    with open('lesson_2_dz.csv') as f_n:
        print(f_n.read())


write_to_csv()
