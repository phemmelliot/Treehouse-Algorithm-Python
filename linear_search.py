def linear_search(list, target):
    """
    Returns the index position if found and none if not found
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print('The target was found at index: {}'.format(index))
    else:
        print('The target was not found in the list')


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

searchResult = linear_search(numbers, 3)

verify(searchResult)

