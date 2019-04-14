# -*- coding: utf-8 -*-
"""
@author: wangyunming
@file: k_Big.py
@time: 2019-04-13 16:17
"""


def k_big(lst, k):
    if len(lst) < k:
        return

    min_heap = lst[0:k]
    for i in range(k):
        heap_insert(min_heap, i)

    for x in lst[k:]:
        if x > min_heap[0]:
            min_heap[0] = x
            heapify(min_heap, 0, k)
    return min_heap[0]


def heap_insert(min_heap, index):
    father_index = int((index - 1) / 2)
    while min_heap[index] < min_heap[father_index]:
        min_heap[index], min_heap[father_index] = min_heap[father_index], min_heap[index]
        index = father_index
        father_index = int((index - 1) / 2)


def heapify(lst, index, size):
    left = 2 * index + 1
    while left < size:
        less = [left, left + 1][(left + 1) < size and lst[left] > lst[left + 1]]
        if lst[index] < lst[less]:
            return
        lst[index], lst[less] = lst[less], lst[index]
        index = less
        left = 2 * index + 1


if __name__ == '__main__':
    lst = [9, 2, 4, 1, 5, 3, 7, 6, 8, 0]
    print(k_big(lst, 6))
