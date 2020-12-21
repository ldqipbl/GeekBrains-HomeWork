"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet


arg_1, arg_2 = 'yandex.ru', 'youtube.com'


def check_ping(sait):
    args = ['ping', sait]
    ya_ping = subprocess.Popen(args, stdout=subprocess.PIPE)


    for time, el in enumerate(ya_ping.stdout):
        if time > 20:
            break
        else:
            result = chardet.detect(el)
            print(result)
            el = el.decode(result['encoding']).encode('utf-8')
            print(el.decode('utf-8'))


check_ping(arg_1)
check_ping(arg_2)
