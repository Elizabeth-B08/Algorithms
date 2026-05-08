"""
Sorting Algorithms Performance Comparison
Based on the report by Elizabeth Balogun

This program:
1. Implements Bubble Sort and Merge Sort without built-in sorting
2. Generates random datasets
3. Tests performance on different dataset sizes
4. Runs each algorithm 5 times
5. Calculates average execution times
6. Displays results in a table
"""

import random
import time


# -----------------------------
# Bubble Sort
# -----------------------------
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):

            # Compare adjacent elements
            if arr[j] > arr[j + 1]:

                # Swap if in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Stop early if already sorted
        if not swapped:
            break

    return arr


# -----------------------------
# Merge Sort
# -----------------------------
def merge_sort(arr):

    # Base case
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursive sorting
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):

    result = []
    i = 0
    j = 0

    # Compare elements and merge
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# -----------------------------
# Performance Testing Function
# -----------------------------
def test_algorithm(algorithm, data, trials=5):

    total_time = 0

    for _ in range(trials):

        # Copy data so original dataset is unchanged
        test_data = data.copy()

        start_time = time.perf_counter()

        algorithm(test_data)

        end_time = time.perf_counter()

        total_time += (end_time - start_time)

    # Return average execution time
    return total_time / trials