from object_structure import Item


def merge(list_of_items: list, low: int, mid: int, high: int, sort_by: str, sort_order: str):
    i = low
    j = mid + 1
    k = low

    temp = [Item(-1, -1)] * 100

    while i <= mid and j <= high:

        if sort_order == 'descending':
            if getattr(list_of_items[i], sort_by) >= getattr(list_of_items[j], sort_by):
                # setattr(temp[k], sort_by, getattr(list_of_items[i], sort_by))
                temp[k] = list_of_items[i]
                i += 1
                k += 1

            else:
                temp[k] = list_of_items[j]
                j += 1
                k += 1

        elif sort_order == 'ascending':
            if getattr(list_of_items[i], sort_by) <= getattr(list_of_items[j], sort_by):
                # setattr(temp[k], sort_by, getattr(list_of_items[i], sort_by))
                temp[k] = list_of_items[i]
                i += 1
                k += 1

            else:
                temp[k] = list_of_items[j]
                j += 1
                k += 1

    # Copy the remaining elements of first half, if there are any *1
    while i <= mid:
        temp[k] = list_of_items[i]
        i += 1
        k += 1
    # Copy the remaining elements of 2nd half, if there are any *2
    while j <= high:
        temp[k] = list_of_items[j]
        j += 1
        k += 1

    # either *1 or *2 is executed, both can never get executed in the same run
    # Copy the temp array to original array
    k = low
    while k <= high:
        # setattr(list_of_items[k], sort_by, getattr(temp[k], sort_by))
        list_of_items[k] = temp[k]
        k += 1

    # C equivalent :
    # for (int k = low;k <= high;k++)
    # {
    #     arr[k] = temp[k];
    # }


def merge_sort(list_of_items: list, low: int, high: int, sort_by: str, sort_order: str):
    if low < high:
        mid = (low + high) // 2
        merge_sort(list_of_items, low, mid, sort_by, sort_order)
        merge_sort(list_of_items, mid + 1, high, sort_by, sort_order)
        merge(list_of_items, low, mid, high, sort_by, sort_order)
