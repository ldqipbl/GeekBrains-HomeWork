'''
    Определение количества различных подстрок с использованием хэш-функции. 
    Пусть дана строка S длиной N, состоящая только из маленьких латинских букв. 
    Требуется найти количество различных подстрок в этой строке.

    Пример работы функции:

    func("papa")    6
    func("sova")    9
'''
import hashlib


def func(user_text):
    text = list(set(user_text))

    for idx_1 in range(len(user_text)):
        lit = user_text[idx_1]

        for idx_2 in range(idx_1 + 1, len(user_text)):
            lit += user_text[idx_2]

            if lit not in text and lit != user_text:
                text.append(lit)


    text = [hashlib.sha512(el.encode('utf-8)')).hexdigest() for el in text]

    print(user_text)
    print(len(text))

func("sova")
func("papa")
