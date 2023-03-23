# since the same array is getting modified in the program :
# return statement is not used in the program
# the temp array is used in merge function and then is
# destroyed within that function itself
# the temp array is used to hold the sorted part
# this was not needed in merge_sort_recursive.py since we had
# 2 separate arrays that is left half and right half, thus we
# could directly change the original array but here since the
# left and right sorted half are within the array itself , we
# need to use temp array and then copy the elements from temp
# array to main array

# refer to this program from exam point of view :
# this is made from the point of view of C lang where we don't
# have standard fxns as in python like the len() function
def merge(arr: list, low: int, mid: int, high: int):
    i = low
    j = mid + 1
    k = low

    temp = [0] * 100
    # create a temp array of very big length say 100 : ( this is wrong
    # length : high-low+1) containing zeros inside it
    # C equivalent : int temp[100];

    while i <= mid and j <= high:
        # use below commented line instead of  : if arr[i] <= arr[j]:
        # if arr[i] >= arr[j]:
        # inorder to sort in descending order
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1

        else:
            temp[k] = arr[j]
            j += 1
            k += 1

    # Copy the remaining elements of first half, if there are any *1
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    # Copy the remaining elements of 2nd half, if there are any *2
    while j <= high:
        temp[k] = arr[j]
        j += 1
        k += 1

    # either *1 or *2 is executed, both can never get executed in the same run
    # Copy the temp array to original array
    k = low
    while k <= high:
        arr[k] = temp[k]
        k += 1

    # C equivalent :
    # for (int k = low;k <= high;k++)
    # {
    #     arr[k] = temp[k];
    # }


def merge_sort(arr: list, low: int, high: int):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)


# Test case
arrInput = [12, 11, 13, 5, 6, 7]
print("Input array:", arrInput)
merge_sort(arrInput, 0, len(arrInput) - 1)
print("Sorted array:", arrInput)
