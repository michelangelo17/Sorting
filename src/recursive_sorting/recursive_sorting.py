# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    i = j = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1
    if i == len(arrA):
        merged_arr.extend(arrB[j:])
    else:
        merged_arr.extend(arrA[i:])
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        return merge(merge_sort(left), merge_sort(right))
    return arr


# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    l, r = start, mid+1
    index = start
    while l < r and index < end and r <= end:
        if arr[l] <= arr[r]:
            l += 1
            index += 1
        else:
            arr.insert(index, arr.pop(r))
            l += 1
            r += 1
            index += 1
    return arr


def merge_sort_in_place(arr, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
