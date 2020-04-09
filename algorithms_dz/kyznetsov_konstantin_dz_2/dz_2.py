'''
    Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно. 
    Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
'''

def fun(start, stop, step, text_str = ''):
    if 0 < step < 11:
        lit = chr(start)
        text_str += f'|{lit} = {start}|'
        step -= 1
        start += 1
        fun(start, stop, step, text_str)

    elif start <= stop:
        print(text_str)
        fun(start, stop, 10, text_str = '')


fun(32, 127, 10)


'''
    остаток не выводил т.к. в задании выводить по 10
'''
