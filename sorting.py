import math

def _find_index_min(lst, start):
    i_min = start
    for i in range(start + 1, len(lst)):
        if lst[i] < lst[i_min]:
            i_min = i
    return i_min

def _swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

def selection_sort(lst):
    for i in range(len(lst)):
        i_min = _find_index_min(lst, i)
        _swap(lst, i, i_min)

def insertion_sort(lst):
    for i in range(1, len(lst)):
        cur = lst[i]
        j = i
        while j > 0 and lst[j - 1] > cur:
            lst[j] = lst[j - 1]
            j = j - 1
        lst[j] = cur

def bubble_sort(lst):
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                _swap(lst, j, j + 1)

def _merge(lst1, lst2):
    lst_merged = []
    i1 = 0
    i2 = 0
    while i1 < len(lst1) and i2 < len(lst2):
        if lst1[i1] < lst2[i2]:
            lst_merged.append(lst1[i1])
            i1 = i1 + 1
        else:
            lst_merged.append(lst2[i2])
            i2 = i2 + 1
    while i1 < len(lst1):
        lst_merged.append(lst1[i1])
        i1 = i1 + 1
    while i2 < len(lst2):
        lst_merged.append(lst2[i2])
        i2 = i2 + 1
    return lst_merged

def merge_sort(lst):
    if(len(lst) == 0 or len(lst) == 1):
        return lst
    else:
        lst1 = merge_sort(lst[:len(lst)//2])
        lst2 = merge_sort(lst[len(lst)//2:])
        return _merge(lst1,lst2)

def _partition(lst, start, end):
    pivot = lst[end]
    to_swap = start
    for i in range(start, end):
        if lst[i] < pivot:
            _swap(lst, i, to_swap)
            to_swap = to_swap + 1
    _swap(lst, to_swap, end)
    return to_swap

def _quick_sort(lst, i, j):
    if j > i:
        to_swap = _partition(lst, i, j)
        _quick_sort(lst, i, to_swap - 1)
        _quick_sort(lst, to_swap + 1, j)

def quick_sort(lst):
    _quick_sort(lst, 0, len(lst) - 1)

def _select(lst, k, start, stop):
   pivot_index = _partition(lst, start, stop)
   while pivot_index != k - 1:
    if pivot_index > k - 1:
        stop = pivot_index - 1
        pivot_index = _partition(lst, start, stop) 
    else:
        start = pivot_index + 1
        pivot_index = _partition(lst, start, stop)
   return lst[k - 1]

def select(lst, k):
    return _select(lst, k, 0, len(lst) - 1)

def counting_sort(lst, k):
    length = len(lst)
    b_lst = [0 for i in range(length)]
    c_lst = [0 for i in range(k+1)]
    for i in range(length):
        c_lst[lst[i]] = c_lst[lst[i]] + 1
    for i in range(k):
        c_lst[i+1] += c_lst[i]
    for i in range(length - 1, -1, -1):
        c_lst[lst[i]] -= 1
        b_lst[c_lst[lst[i]]] = lst[i]
    for i in range(length):
        lst[i] = b_lst[i]

def _counting_sort(lst, exp):
    n = len(lst)
    base = 10
    count = [0 for i in range(base)]
    output = [0 for i in range(n)]
    for i in range(n):
        index = (lst[i] // exp) % base
        count[index] += 1
    for i in range(base - 1):
        count[i + 1] += count[i]
    for i in range(n - 1, -1, -1):
        index = (lst[i] // exp) % base
        count[index] -= 1
        output[count[index]] = lst[i]
    for i in range(n):
        lst[i] = output[i]

def radix_sort(lst):
    max_element = max(lst)
    base = 10
    exp = 1
    while max_element // exp > 0:
        _counting_sort(lst, exp)
        exp *= base

def bucket_sort(lst, k):
    buckets = [[] for i in range(k)]
    M = max(lst) + 1
    for i in range(len(lst)):
        buckets[math.floor((k * lst[i]) / M)].append(lst[i])
    for i in range(k):
        quick_sort(buckets[i])
    output = []
    for i in range(k):
        output = output + buckets[i]
    for i in range(len(lst)):
        lst[i] = output[i]