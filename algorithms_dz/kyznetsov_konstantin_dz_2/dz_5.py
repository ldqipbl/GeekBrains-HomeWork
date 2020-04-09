'''
    Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. 
    Вывести на экран это число и сумму его цифр.
'''
max_sum = 0

while True:
    integer = int(input('Введите натуральные числа '))

    if integer == 0:
        print()
        print(answer)
        break

    repit = len(str(integer))
    summa = 0

    while repit > 0:
        n = 10 ** repit
        a = 10 ** (repit - 1)
        summa += (integer % n) // a
        repit -= 1

    if max_sum < summa:
        max_sum = summa
        answer = f'Число с большей суммой чисел = {integer}\nСумма чисел равна = {max_sum}'
