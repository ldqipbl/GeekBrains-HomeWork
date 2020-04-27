'''
    Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). 
    Выведите на экран исходный и отсортированный массивы.
'''

from random import uniform as rand


array = [rand(0, 50) for el in range(10)]


def merge(left_ls, right_ls):
    sort_lst = []
    left_idx, right_idx = 0, 0
    left_len, right_len = len(left_ls), len(right_ls)

    for _ in range(left_len + right_len):
        if left_idx < left_len and right_idx < right_len:
            if left_ls[left_idx] <= right_ls[right_idx]:
                sort_lst.append(left_ls[left_idx])
                left_idx += 1

            else:
                sort_lst.append(right_ls[right_idx])                
                right_idx += 1

        elif left_idx == left_len:
            sort_lst.append(right_ls[right_idx])
            right_idx += 1

        elif right_idx == right_len:
            sort_lst.append(left_ls[left_idx])
            left_idx += 1

    return sort_lst


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_ls = merge_sort(nums[:mid])
    right_ls = merge_sort(nums[mid:])

    return merge(left_ls, right_ls)

print(f'{array} исходный массив \n{merge_sort(array)} отсортированный массив')
