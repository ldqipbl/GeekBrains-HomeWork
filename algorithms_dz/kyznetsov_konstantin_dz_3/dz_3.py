'''
    В массиве найти максимальный отрицательный элемент. 
    Вывести на экран его значение и позицию в массиве. 
    Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
'''
# -13 < -3 (Чем ближе к 0 тем больше)

from random import randint as rand


SIZE = 10
MIN_ITEM = -5
MAX_ITEM = 5

array = [rand(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array,'\n---------------')


a = MIN_ITEM

for num, el in enumerate(array):
    if 0 > el > a :
        a = el
        num_a = num

print(f'элемент = {a}, позицию в массиве = {num_a}')

