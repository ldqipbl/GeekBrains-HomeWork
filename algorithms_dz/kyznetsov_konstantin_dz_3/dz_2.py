'''
    Определить, какое число в массиве встречается чаще всего.
'''
from random import randint as rand


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 5

array = [rand(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_count_elem = 0
max_name_elem = 0

print(array,'\n---------------')


for el in range(SIZE):
    name_elem = array[el]
    count_elem = 0
    for el in array:
        if name_elem == el:
            count_elem += 1
    if max_count_elem < count_elem > 1:
        max_count_elem = count_elem
        max_name_elem = name_elem
    
print(f'repit = {max_count_elem}\nname = {max_name_elem}')

