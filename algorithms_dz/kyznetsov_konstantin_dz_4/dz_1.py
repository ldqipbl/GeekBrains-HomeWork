'''
    1.Выбрать написанную 
    2.Написать еще 2 варианта
    3.timeit и cProfile
    4.Комментарии
    5.выводы
'''
import timeit, cProfile

# 1

def brute_force(user_int, rand_int):
    if user_int == rand_int:
        pass
        #print(f'brute_force Отгадал! Загадоно число {rand_int}')
    else:
        user_int += 1
        brute_force(user_int, rand_int)

print('\nbrute_force')
print(timeit.timeit('brute_force(1, 7)', number=100, globals=globals()))        # 0.0002737500035436824
print(timeit.timeit('brute_force(1, 70)', number=100, globals=globals()))       # 0.003152397010126151
print(timeit.timeit('brute_force(1, 700)', number=100, globals=globals()))      # 0.04714721700293012
# Переполнение стека

cProfile.run('brute_force(1, 7)')           #7/1    0.000    0.000    0.000    0.000 dz_1.py:12(brute_force)
cProfile.run('brute_force(1, 70)')          #70/1    0.000    0.000    0.000    0.000 dz_1.py:12(brute_force)
cProfile.run('brute_force(1, 700)')         #700/1    0.001    0.000    0.001    0.001 dz_1.py:12(brute_force)


# 2

def binary_search(rand_min, rand_max, rand_int):

    for _ in range(100):
        user_int = (rand_min + rand_max) // 2

        if user_int == rand_int:
            #print(f'binary_search Отгадал! Загадоно число {rand_int}')
            break
        elif user_int > rand_int:
            rand_max = user_int - 1
        elif user_int < rand_int:
            rand_min = user_int + 1

        user_int = rand_max

print('\nbinary_search')
print(timeit.timeit('binary_search(0, 100, 7)', number=100, globals=globals()))         # 0.00044775300193578005
print(timeit.timeit('binary_search(0, 100, 70)', number=100, globals=globals()))        # 0.0004437320021679625
print(timeit.timeit('binary_search(0, 100, 700)', number=100, globals=globals()))       # 0.004657098004827276
print(timeit.timeit('binary_search(0, 100, 7000)', number=100, globals=globals()))      # 0.004933898992021568

cProfile.run('binary_search(0, 100, 7)')            #1    0.000    0.000    0.000    0.000 dz_1.py:33(binary_search)
cProfile.run('binary_search(0, 100, 70)')           #1    0.000    0.000    0.000    0.000 dz_1.py:33(binary_search)
cProfile.run('binary_search(0, 100, 700)')          #1    0.000    0.000    0.000    0.000 dz_1.py:33(binary_search)
cProfile.run('binary_search(0, 100, 7000)')         #1    0.000    0.000    0.000    0.000 dz_1.py:33(binary_search)


# 3

def new_brute_force(rand_int, user_int):
    el = len(str(rand_int)) - 1

    while True:
        if user_int == rand_int:
            #print(f'new_brute_force Отгадал! Загадоно число {rand_int}')
            break

        while user_int // (10 ** el) != rand_int // (10 ** el):
            user_int += 10 ** el
            if el != 0:
                el -= 1


print('\nnew_brute_force')
print(timeit.timeit('new_brute_force(7, 1)', number=100, globals=globals()))            # 0.0005840490048285574
print(timeit.timeit('new_brute_force(70, 1)', number=100, globals=globals()))           # 0.0038634179945802316
print(timeit.timeit('new_brute_force(700, 1)', number=100, globals=globals()))          # 0.044088727998314425
print(timeit.timeit('new_brute_force(7000, 1)', number=100, globals=globals()))         # 0.45390143799886573

cProfile.run('new_brute_force(7, 1)')           #1    0.000    0.000    0.000    0.000 dz_1.py:62(new_brute_force)
cProfile.run('new_brute_force(70, 1)')          #1    0.000    0.000    0.000    0.000 dz_1.py:62(new_brute_force)
cProfile.run('new_brute_force(700, 1)')         
#1    0.000    0.000    0.000    0.000 dz_1.py:62(new_brute_force) 
#1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
cProfile.run('new_brute_force(7000, 1)')
#1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#1    0.005    0.005    0.005    0.005 dz_1.py:62(new_brute_force)
#1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}



'''
    Вывод: 

    brute_force = O(n)
    binary_search = O(log n)
    new_brute_force = O(n**2)

    1.Для маленьких значеий(до 10) лучше brute_force т.к. быстрее. 
    2.для юолбших значений binary_search т.к. быстрая, на больших значениях, и нет переполнение стека
'''
