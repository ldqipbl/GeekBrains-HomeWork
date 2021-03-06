'''
    Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). 
    Выведите на экран исходный и отсортированный массивы.
     
    Примечания:
    ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
    ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. 
        Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
'''
from random import randint as rand


array = [rand(0, 100) for el in range(10)]

def dz_1(arr):
    for idx in range(1, len(arr)):
        for el in range(len(arr) - idx):
            if arr[el] < arr[el + 1]:
                 arr[el], arr[el + 1] = arr[el + 1], arr[el]

        print(arr)
    return arr

print(f'{array} исходный массив \n{dz_1(array)} отсортированный массив')
