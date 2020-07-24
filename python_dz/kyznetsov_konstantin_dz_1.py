#1
print('Создать несколько переменных, запросите у пользователя несколько строк и чисел, выведите на экран')
print('')


first_variable = 1
second_variable = '2'
third_variable = True

first_str_user_variable = input('Введите строку №1: ')
second_str_user_variable = input('Введите строку №2: ')

first_int_user_variable = int(input('Введите число №1: '))
second_int_user_variable = int(input('Введите число №2: '))


print(f'Первая переменная = {first_variable}, Вторая переменная = {second_variable}, Третья переменная = {third_variable}')
print(f'Первая строка = {first_str_user_variable}, Вторая строка = {second_str_user_variable}, Первое число = {first_int_user_variable}, Второе число = {second_int_user_variable}')
print('')


#2
print('Пользователь вводит число в секундах. Перевести в дни:часы:минуты:секунды')
print('')


sec_in_min = 60
min_in_hour = 60
hour_in_day = 24


seconds_all = int(input('Введите время в секундах\n>'))
seconds = seconds_all % sec_in_min

minutes_all = seconds_all // sec_in_min
minutes = minutes_all % min_in_hour

hour_all = minutes_all // min_in_hour
hour = hour_all % hour_in_day

day = hour_all // hour_in_day


print(f'{day}:{hour}:{minutes}:{seconds}')
print('')


#3
print('узнайте у пользователя число n. Найдите сумму n + nn + nnn.')
print('')


user_number = input('Введите число\n>')


first_number = int(user_number)
second_number = int(user_number + user_number)
# second_number = int(user_number * 2) альтернативный вариант
last_number = int(user_number + user_number + user_number)
# last_number = int(user_number * 3) альтернативный вариант

sum_of_numbers = first_number + second_number + last_number


print(sum_of_numbers)
print('')


#4
print('Найдите самую большую цыфру в числе')
print('')


user_number = input('Введите целое положительное число\n>')

max_number = user_number
i = 0


while i < len(user_number):
    if user_number[i] > max_number:
        max_number = user_number[i]
    i += 1


print(max_number)
print('')


#5
print('Определить финансовый результат работы фирмы, выведите на экран. Если фирма отработола с прибылью, вычислите рентабельность выручки. Запросите число сотрудников. Определите прибыль фирмы в расчёте на одного сотрудника')
print('')


revenue = int(input('Введите выручку фирмы\n>'))
cost = int(input('Введите издержки фирмы\n>'))


profit = revenue - cost
profitability = profit / revenue  
# по условию вычеслить рентабельность нужно, есле финансовый результат работ == прибыль, но если вычислить здест читаться код будет лучше


if revenue > cost:
    print('Прибыль')
    print('Рентабельность выручки', profitability)
elif revenue < cost:
    print('Убыток')
else:
    print('Они равны')


number_of_staff = int(input('Введите число сотрудников\n>'))


profit_per_person = profit / number_of_staff


print('Прибыль фирмы в расчёте на одного сотрудника', profit_per_person)
print('')


#6
print('Определить номер дня на который результат составит указанное количество километров')
print('')


first_day = int(input('Введите результат первого деня в километрах: '))
desired_result = int(input('Введите сколько километров хотите пробегать: '))
progress = first_day
day = 0


while progress <= desired_result:
    progress = progress / 100 * 10 + progress
    day += 1


print(day)
