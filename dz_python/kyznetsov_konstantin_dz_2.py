# 1
def question_1():
    array_el = [1, 'два', True, [2, 'три']]

    for el in array_el:
        print(type(el))


# 2
def question_2():
    user_array_el = []
    enswer_array_el = []


    while True:
        user_el = input('Введите елемент. Пустой элемент (" ") выход\n')
        if user_el == ' ':
            break
        user_array_el.append(user_el)


    for i in range(1, len(user_array_el), 2):
        enswer_array_el.append(user_array_el[i])

        i -= 1
        enswer_array_el.append(user_array_el[i])
    else:
       if len(user_array_el) % 2 != 0:
           enswer_array_el.append(user_array_el[-1])


    print(enswer_array_el)


# 3
def question_3():
    months = int(input('months: '))

    array_list = ['Зима', 'Весна', 'Лето', 'Осень']
    array_dict = {0 : 'Зима', 1 : 'Весна', 2 : 'Лето', 3 : 'Осень'}


    if 1 > months or months > 12:
        print('Нет такого месяца')
        exit()
    else:
        pass


    months = months // 3

    if months == 4:
        months = 0
    else:
        pass


    print('list', array_list[months])
    print('dict', array_dict[months])


# 4
def question_4():
    print('Введите несколько слов через пробел')

    text = input().split()

    for i in range(len(text)):
        if len(text[i]) > 10:
            new_text = text[i]
            new_text = new_text[:10]
            print(new_text)
        else:
            print(text[i])


# 5
def question_5():
    my_list = [7, 5, 3, 3, 2]
    elem = 1


    while elem > 0:
        my_list.sort(reverse = True)
        print(my_list)

        elem = int(input('Введите число '))
        my_list.append(elem)



# 6
def question_6():
    products = []
    product = ()
    number_product = len(product) + 1
    exit = 0

    while not exit == 'y' or exit == 'yes' or exit == 'д' or exit == 'да':

        name = input('name product ')
        price = input('price ')
        quantity = input('quantity ')
        units = input('units ')


        product_description = {'название': name, 'цена': price, 'количество': quantity, 'eд': units}
        product = (number_product, product_description)
        products.append(product)

        number_product += 1


        exit = input('exit (y/n) ')


    print(*products, sep='\n')


# 7
def question_7():
    name_list = []
    price_list = []
    quantity_list = []
    units_list = []

    enswer_dict = {}

    products = [
        (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
        (2, {'название': 'принтер', 'цена': 60000, 'количество': 2, 'eд': 'шт.'}),
        (3, {'название': 'сканер', 'цена': 20000, 'количество': 7, 'eд': 'шт.'}),

    ]

    key_list = ['название', 'цена', 'количество', 'eд']


    for product in products:
        get_dict = product[1]

        for elem in get_dict:
            if elem == 'название':
                name_list.append(get_dict[elem])
            elif elem == 'цена':
                price_list.append(get_dict[elem])
            elif elem == 'количество':
                quantity_list.append(get_dict[elem])
            elif elem == 'eд':
                units_list.append(get_dict[elem])

    for key_elem in key_list:
        if key_elem == 'название':
            enswer_dict[key_elem] = name_list
        elif key_elem == 'цена':
            enswer_dict[key_elem] = price_list
        elif key_elem == 'количество':
            enswer_dict[key_elem] = quantity_list
        elif key_elem == 'eд':
            units_list = set(units_list)
            enswer_dict[key_elem] = units_list


    print(enswer_dict)





question_1()
question_2()
question_3()
question_4()
question_5()
question_6()
question_7()


