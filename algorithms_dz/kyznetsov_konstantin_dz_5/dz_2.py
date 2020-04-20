'''
    Написать программу сложения и умножения двух шестнадцатеричных чисел.
    При этом каждое число представляется как коллекция, элементы которой — цифры числа.

    Например, пользователь ввёл A2 и C4F.
    Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
    Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''
from collections import defaultdict


num_sum = 0
enswer = []

d = defaultdict(list)

array_lit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']


ints_user = [input(f'введите {el + 1} шестнадцатеричное число ') for el in range(2)]

for elem in ints_user:
    elem = elem[::-1]
    d[elem].append(list(elem))
    for idx, el in enumerate(*d[elem]):
        if el in array_lit:
            num_sum += array_lit.index(el) * 16 ** idx
        else:
            num_sum += int(el) * 16 ** idx

while num_sum > 0:
    enswer.append(num_sum % 16)
    num_sum //= 16

enswer_lit = [array_lit[el] for el in enswer]


print(*enswer_lit[::-1])

