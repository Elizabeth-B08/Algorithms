# Bubble Sort
array1 = [1, 3, 4, 7, 5, 10, 9, 8, 6]
array2 = [1, 6, 4, 7, 5, 10, 9, 8, 5]
def bubble_sort(array1):
    n = len(array1)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if array1[j] > array1[j + 1]:
                array1[j], array1[j + 1] = array1[j + 1], array1[j]
                swapped = True
        if not swapped:
            break
    return array1

# Merge Sort
def merge_sort(array2):
    if len(array2) <= 1:
        return array2

    mid = len(array2) // 2
    left = merge_sort(array2[:mid])
    right = merge_sort(array2[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

