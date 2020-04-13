'''
    В одномерном массиве целых чисел определить два наименьших элемента.
    Они могут быть как равны между собой (оба являться минимальными), так и различаться. 
'''

from random import randint as rand


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100

array = [rand(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


for el in range(2):
    min_elem = 0

    print(array)

    for num, elem in enumerate(array):
        if min_elem > elem:
            min_elem = elem
            num_min_elem = num

    array[num_min_elem] = False


    print(f'min elem = {min_elem}, num min elem = {num_min_elem}\n-----------')

