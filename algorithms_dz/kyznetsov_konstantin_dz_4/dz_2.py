'''
    Написать два алгоритма нахождения i-го по счёту простого числа. 
    Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. 
    Проанализировать скорость и сложность алгоритмов.
'''
import timeit, cProfile


num = 128

def fun_1(num_arg):
    num = num_arg
    num_in_lst = num + 1
    lst = []
    for el_1 in range(2, num * 10):
        for el_2 in lst:
            if el_1 % el_2 == 0:
                break
        else:
            lst.append(el_1)

    num -= 1
    #print(lst[num])

fun_1(num)

print('\nfun_1(')
print(timeit.timeit('fun_1(5)', number=100, globals=globals()))          #0.0034216499989270233
print(timeit.timeit('fun_1(50)', number=100, globals=globals()))         #0.0730295670000487
print(timeit.timeit('fun_1(500)', number=100, globals=globals()))        #3.8573024469988013
print(timeit.timeit('fun_1(5000)', number=100, globals=globals()))       #253.85665495899957

cProfile.run('fun_1(5)')
cProfile.run('fun_1(50)')
cProfile.run('fun_1(500)')
cProfile.run('fun_1(5000)')
'''
         19 function calls in 0.000 seconds

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       15    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}


         99 function calls in 0.001 seconds

        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 dz_2.py:11(fun_1)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
       95    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}


         673 function calls in 0.039 seconds

        1    0.000    0.000    0.039    0.039 <string>:1(<module>)
        1    0.039    0.039    0.039    0.039 dz_2.py:11(fun_1)
        1    0.000    0.000    0.039    0.039 {built-in method builtins.exec}
      669    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}


         5137 function calls in 2.546 seconds

        1    0.000    0.000    2.546    2.546 <string>:1(<module>)
        1    2.544    2.544    2.545    2.545 dz_2.py:11(fun_1)
        1    0.000    0.000    2.546    2.546 {built-in method builtins.exec}
     5133    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}

'''


# 2

def fun_2(num_arg):
    num = num_arg
    array = [el for el in range(num * 10)]
    lst = []

    i = 2
    while len(lst) <= num:
        if array[i] != 0:
            lst.append(array[i])
            for j in range(i, len(array), i):
                array[j] = 0
        i += 1

    num -= 1
    #print(lst[num])
    
fun_2(num)


print('\nfun_2()')
print(timeit.timeit('fun_2(5)', number=100, globals=globals()))         #0.0029136389966879506
print(timeit.timeit('fun_2(50)', number=100, globals=globals()))         #0.03515210899786325
print(timeit.timeit('fun_2(500)', number=100, globals=globals()))         #0.5164078800007701
print(timeit.timeit('fun_2(5000)', number=100, globals=globals()))         #6.163582813998801

cProfile.run('fun_2(5)')
cProfile.run('fun_2(50)')
cProfile.run('fun_2(500)')
cProfile.run('fun_2(5000)')
'''
         30 function calls in 0.000 seconds

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       19    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        6    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}


         340 function calls in 0.001 seconds

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 dz_2.py:41(fun_2)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
      284    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       51    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}


         4588 function calls in 0.007 seconds

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
        1    0.005    0.005    0.006    0.006 dz_2.py:41(fun_2)
        1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
     4082    0.001    0.000    0.001    0.000 {built-in method builtins.len}
      501    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}


         58626 function calls in 0.076 seconds

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.076    0.076 <string>:1(<module>)
        1    0.061    0.061    0.075    0.075 dz_2.py:41(fun_2)
        1    0.005    0.005    0.005    0.005 dz_2.py:43(<listcomp>)
        1    0.000    0.000    0.076    0.076 {built-in method builtins.exec}
    53620    0.008    0.000    0.008    0.000 {built-in method builtins.len}
     5001    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}

'''

