# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # Find next smallest element
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # Swap values in array.
        a, b = arr[cur_index], arr[smallest_index]
        arr[smallest_index], arr[cur_index] = a, b
    # Sorted
    return arr


# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    while True:
        swapcount = 0
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                a, b = arr[i], arr[i + 1]
                arr[i], arr[i + 1] = b, a
                swapcount += 1
        if swapcount == 0:
            return arr


# STRETCH: implement the Count Sort function below


def count_sort(arr):
    if len(arr) == 0:
        return []
    if min(arr) < 0:
        return "Error, negative numbers not allowed in Count Sort"
    maximum = max(arr)
    count = [0 for _ in range(maximum + 1)]
    for i in arr:
        count[i] += 1
    sum = 0
    for i, c in enumerate(count):
        count[i] = sum
        sum += c
    sorted = [None] * len(arr)
    for i in arr:
        sorted[count[i]] = i
        count[i] += 1
    return sorted
