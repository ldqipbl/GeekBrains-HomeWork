'''
    В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

from random import randint as rand


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [rand(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_elem = array[0]
min_elem = array[0]

print(array,'\n---------------')

for num, elem in enumerate(array):
    if max_elem < elem:
        max_elem = elem
        num_max_elem = num
    elif min_elem > elem:
        min_elem = elem
        num_min_elem = num

print(f'max elem = {max_elem} num max elem {num_max_elem}\nmin elem = {min_elem} num min elem {num_min_elem}\n---------------')

array[num_max_elem], array[num_min_elem] = array[num_min_elem], array[num_max_elem]


print(array)
