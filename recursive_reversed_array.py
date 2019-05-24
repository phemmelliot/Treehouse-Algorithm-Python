def recursive_reverse(array, last_index, first_index):
    current_first = array[first_index]
    current_last = array[last_index]
    array[first_index] = current_last
    array[last_index] = current_first
    if last_index == first_index or first_index > last_index:
        return array
    return recursive_reverse(array, last_index-1, first_index+1)


list_array = [1, 2, 3, 4, 5, 6, 7]
reversed_array = recursive_reverse(list_array, 6, 0)
print(reversed_array)