'''
    Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
'''

num = int(input('введите целое трехзначное число '))

a = num % 10
b = (num % 100 - a) // 10
c = (num - b - a) // 100

summa = a + b + c
compos = a * b * c

print(f'сумму = {summa}, произведение = {compos}')
