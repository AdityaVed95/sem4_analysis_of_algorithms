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

    # for j in range(low, high):

    j = low
    while j < high:

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

        j += 1

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Test case
arrInput = [10, 7, 8, 9, 1, 5, 10, 15]
print("Input array:", arrInput)
quick_sort(arrInput, 0, len(arrInput) - 1)
print("Sorted array:", arrInput)
