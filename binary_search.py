def binary_search(passed_list, target):
    passed_list.sort()
    global keep_searching
    keep_searching = True

    while keep_searching:

        if len(passed_list) == 1:
            middle_index = 0
        else:
            middle_index = round(len(passed_list) / 2)

        if middle_index == 0 & passed_list[middle_index] == target:
            keep_searching = False
            return middle_index

        if middle_index == 0:
            keep_searching = False
            return -1

        if passed_list[middle_index - 1] == target:
            # print('Inside first check')
            keep_searching = False
            return middle_index

        if passed_list[middle_index - 1] > target:
            passed_list = passed_list[:middle_index]
            # print(passed_list)

        if passed_list[middle_index - 1] < target:
            passed_list = passed_list[middle_index:]
            # print(passed_list)


def new_binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None


def verify(index):
    if index is not None:
        print('The target was found at index: {}'.format(index))
    else:
        print('The target was not found in the list')


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

searchResult = new_binary_search(numbers, 1)

verify(searchResult)

# numbers = [1, 2, 3, 4]
# index = binary_search(numbers, 3)
# print(index)