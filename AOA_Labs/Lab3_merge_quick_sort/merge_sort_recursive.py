# refer to this program from conceptual understanding point of view
# not from exam point of view

def merge(arr: list, left_half: list, right_half: list):
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


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on left and right halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted left and right halves
        merge(arr, left_half, right_half)

        # either call the above "merge" fxn or execute below commented code
        # i = j = k = 0
        # while i < len(left_half) and j < len(right_half):
        #     if left_half[i] < right_half[j]:
        #         arr[k] = left_half[i]
        #         i += 1
        #     else:
        #         arr[k] = right_half[j]
        #         j += 1
        #     k += 1
        #
        # while i < len(left_half):
        #     arr[k] = left_half[i]
        #     i += 1
        #     k += 1
        #
        # while j < len(right_half):
        #     arr[k] = right_half[j]
        #     j += 1
        #     k += 1


# Test case
arrInput = [12, 11, 13, 5, 6, 7]
print("Input array:", arrInput)
merge_sort(arrInput)
print("Sorted array:", arrInput)
