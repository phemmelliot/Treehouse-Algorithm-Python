"""
This recursive binary search is slower because of the slice operation.
It also has the disadvantage of not returning the index where the item is found
"""


def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] > target:
                return recursive_binary_search(list[:midpoint-1], target)
            else:
                return recursive_binary_search(list[midpoint+1:], target)


"""
This recursive binary search is faster.
It also has the advantage of returning the index and having a big O of (log n + 1)
"""


def better_recursive_binary_search(list, target, start=0, end=None):
    if end is None:
        end = len(list) - 1
    if start > end:
        return -1

    mid = (start + end)//2

    if list[mid] == target:
        return mid
    else:
        if list[mid] > target:
            return better_recursive_binary_search(list, target, start, mid-1)
        else:
            return better_recursive_binary_search(list, target, mid+1, end)


def verify(res):
    print('Target Found: ', res)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 1)
verify(result)


def verify_better(index):
    if index is not None:
        print('The target was found at index: {}'.format(index))
    else:
        print('The target was not found in the list')


result = better_recursive_binary_search(numbers, 12)
verify_better(result)

result = better_recursive_binary_search(numbers, 6)
verify_better(result)
