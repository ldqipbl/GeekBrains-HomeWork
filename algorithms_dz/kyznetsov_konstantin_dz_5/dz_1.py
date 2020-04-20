'''
    Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия. 
    Программа должна определить среднюю прибыль (за год для всех предприятий) 
        и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
'''
from collections import namedtuple as ndt


name_obj = []
all_sum = 0

NewObj = ndt('NewObj', 'name, summa')
count_obj = int(input('количестве предприятий '))


for _ in range(count_obj):
    name = input('наименования предприятий ')
    obj_sum = int(input(f'прибыль за 1 квартал ')) + \
              int(input(f'прибыль за 2 квартал ')) + \
              int(input(f'прибыль за 3 квартал ')) + \
              int(input(f'прибыль за 4 квартал '))

    el = NewObj(name, obj_sum)

    name_obj.append(el)

    all_sum += obj_sum

else:
    mid_sum = all_sum // count_obj


print(f'\nсредняя прибыль {mid_sum}\n')


for el in name_obj:
    if el.summa > mid_sum:
        print(f'прибыль выше среднего {el.name}')
    elif el.summa < mid_sum:
        print(f'прибыль ниже среднего {el.name}')

