def binary_search(values, value, is_sorted=True):
    if not is_sorted:
        array = sorted(values)
    else:
        array = values
    index = len(array) // 2
    while array:
        if array[index] == value:
            return index
        elif index == 0:
            break
        # middle is greater, go left
        elif array[index] > value:
            array = array[:index]
            print(array)
        else:
            array = array[index:]
            print(array)
        index = len(array) // 2
    return -1


l = [1, 2, 4, 5, 6]
print(binary_search(l, 1))
