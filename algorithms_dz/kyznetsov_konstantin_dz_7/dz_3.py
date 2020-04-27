'''
    Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. 
    Найдите в массиве медиану. 
    Медианой называется элемент ряда, делящий его на две равные части: 
        в одной находятся элементы, которые не меньше медианы, 
        в другой — не больше медианы.

    Примечание:
    задачу можно решить без сортировки исходного массива. 
    Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
'''

from random import randint as rand


m = 3

array = [rand(0, 100) for el in range(2 * m + 1)]

def gnome(array):
    i, size = 1, len(array)
    while i < size:
        if array[i - 1] <= array[i]:
    	    i += 1
        else:
            array[i], array[i - 1] = array[i - 1], array[i]
            if i > 1:
                i -= 1
    return array

def nlogn_median(array):
    array = gnome(array)
    if len(array) % 2 == 1:
        return array[len(array) // 2]
    else:
        return 0.5 * (array[len(array) // 2 - 1] + array[len(array) // 2])

print(f'{array} исходный массив \n{gnome(array)} отсортированный массив')
print(nlogn_median(array))
