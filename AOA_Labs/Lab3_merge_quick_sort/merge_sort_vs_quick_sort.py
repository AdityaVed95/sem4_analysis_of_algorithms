import copy
import random
import time


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on left and right halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted left and right halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def quick_sort(arr, low, high):
    if low < high:
        # Partition the array around a pivot
        pivot_index = partition(arr, low, high)

        # Recursively sort the two subarrays
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def create_list(size_of_list: int) -> list:
    list1 = []
    i = 0
    while i < size_of_list:
        list1.append(random.randint(0, 10000))
        i += 1

    return list1


if __name__ == "__main__":
    print("Enter the size of the array")
    size = int(input())
    listInput = create_list(size)
    listInputCopy = copy.deepcopy(listInput)

    start_quick = time.time()
    quick_sort(listInputCopy, 0, len(listInputCopy) - 1)
    end_quick = time.time()

    start_merge = time.time()
    merge_sort(listInput)
    end_merge = time.time()

    print("Time for Merge Sort is : ", (end_merge - start_merge), " seconds")
    print("Time for Quick Sort is : ", (end_quick - start_quick), " seconds")
