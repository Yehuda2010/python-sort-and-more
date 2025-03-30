def binary_search(lst, element):
    low = 0
    high = len(lst) - 1
    while high >= low:
        mid = (low + high) // 2
        if lst[mid] == element:
            return mid
        elif lst[mid] > element:
            high = mid - 1
        else:
            low = mid + 1
    return -1
