'''
    Закодируйте любую строку из трех слов по алгоритму Хаффмана.
'''
from collections import Counter, deque


text = input('Введите текст ')
text = Counter(text).most_common()

# переворачиваем массив
min_idx, max_idx = 0, len(text)
while min_idx < max_idx:
    text[min_idx], text[max_idx - 1] = text[max_idx - 1], text[min_idx]
    min_idx += 1
    max_idx -= 1

# описываем сортировку
def dz_1(arr):
    for idx in range(1, len(arr)):
        for el in range(len(arr) - idx):
            if arr[el][1] > arr[el + 1][1]:
                 arr[el], arr[el + 1] = arr[el + 1], arr[el]
    return arr

text = deque(text)  # для скорости. Много перемещений в края массива
print(text)

# Нечетные [1] хронят количество букв в узле или элементе, [0] хронят узлы или листья. Четные [] выбор узла
while 1 < len(text):
    sum_el = text[0][1] + text[1][1]
    text.append(((text[0], text[1]), sum_el))   # если взять (text[0][0], text[1][0]) получатя только буквы и узлы, без нечетных [] значений. 
                                                # Но как разархивировать незня колличество букв в слове?
    del text[0]
    del text[0]

    dz_1(text)

    print(text)

text = text[0]
print(text)
print(text[0][0][0][1][0])                      # если взять (text[0][0], text[1][0]) вывод будет print(text[0][1]) = 'e' (если строка 'beep boop beer!')

