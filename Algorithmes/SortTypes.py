import random
import matplotlib.pyplot as plt
from math import floor


def plot(array):
    width = 3 / len(array)
    labels = [str(i) for i in array]

    plt.bar(labels, array, width)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("List Sorting")

    plt.show()


updated = 0


def new_plot(array):
    global updated
    updated += 1
    width = 1 - 5 / len(array)
    labels = [str(i) for i in array]

    plt.clf()
    plt.bar(labels, array, width)
    # plt.ion()
    # plt.plot(array)
    plt.text(0.9, 0.03, f"calls: {updated}", transform=plt.gca().transAxes)
    plt.draw()
    plt.pause(0.001)


def insertion_sort(values):
    sl = list()
    for i in values[:]:
        index = 0
        # reach the end or find greater value
        while index < len(sl) and sl[index] < i:
            index += 1
        sl.insert(index, i)
        values.remove(i)
        new_plot(sl + values)
    return sl


def selection_sort(values):
    sl = list()
    x = len(values)
    for i in range(x):
        item = min(values)
        sl.append(item)
        values.remove(item)
        new_plot(sl + values)
    return sl


def merge_sort(values):
    if len(values) > 1:
        m = len(values) // 2
        left = values[:m]
        right = values[m:]
        left = merge_sort(left)
        right = merge_sort(right)

        values = []

        while left and right:
            if left[0] < right[0]:
                values.append(left.pop(0))
            else:
                values.append(right.pop(0))
            # new_plot(left + right + values)

        for i in left:
            values.append(i)
        for i in right:
            values.append(i)

    new_plot(values)
    return values


""" Wrapper for quicksort """


def quick_sort(values):
    quicksort(values, 0, len(values) - 1)
    return values


""" 
Sorts in place
The entire array is sorted by quicksort(A, 0, length(A) - 1).
"""


def quicksort(array, start, end):
    new_plot(array)
    if start >= end:
        return

    p = partition(array, start, end)
    quicksort(array, start, p - 1)
    quicksort(array, p + 1, end)


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    # swap the values
    array[start], array[high] = array[high], array[start]

    return high


def pigeonhole_sort(values):
    lst = [(value, value) for value in values]
    pigeonholesort(lst)
    return [value for key, value in lst]


def pigeonholesort(lst) -> None:
    """Sort list of (key, value) pairs by key."""
    base = min(key for key, value in lst)
    size = max(key for key, value in lst) - base + 1

    pigeonholes = [[] for _ in range(size)]

    for key, value in lst:
        i = key - base
        pigeonhole = pigeonholes[i]
        pigeonhole.append((key, value))

    i = 0
    for pigeonhole in pigeonholes:
        for element in pigeonhole:
            lst[i] = element
            new_plot([key for key, value in lst])
            i += 1


def counting_sort(values, k=None, key=int):
    if k == None:
        k = max(values)
    count = [0 for i in range(k + 1)]
    for x in values:
        count[key(x)] += 1

    total = 0
    for i in range(k + 1):
        count[i], total = total, count[i] + total

    output = [0 for i in range(len(values))]
    for x in values:
        output[count[key(x)]] = x
        count[key(x)] += 1
        new_plot(output)

    return output


def _sort(values):
    sl = list()
    for i in values:
        new_plot(sl + values)
    return sl


l = list(range(-50, 50))
random.shuffle(l)
new_plot(quick_sort(l))
plt.pause(3)
