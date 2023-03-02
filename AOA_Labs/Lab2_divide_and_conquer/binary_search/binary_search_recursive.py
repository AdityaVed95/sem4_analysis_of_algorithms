import random


def binary_search_using_recursive_approach(list1: list, key: int, imin: int, imax: int) -> int:
    imid = 0

    # doubt : if the above line is not there then too the program works
    # it should not have worked since imid is declared inside the else
    # block and is the local variable of the else block



    if imax < imin:
        return -1

    else:
        imid = (imin + imax) // 2

    if list1[imid] < key:
        return binary_search_using_recursive_approach(list1, key, imid + 1, imax)

    elif list1[imid] > key:
        return binary_search_using_recursive_approach(list1, key, imin, imid - 1)

    else:
        return imid


def create_list(size_of_list_to_create: int) -> list:
    list1 = []
    i = 0
    while i < size_of_list_to_create:
        list1.append(random.randint(0, 1000))
        i += 1

    return list1


def sort_list(list1: list) -> list:
    for i in range(0, len(list1)):
        least_index = i
        for j in range(i, len(list1)):
            if list1[j] < list1[least_index]:
                list1[j], list1[least_index] = list1[least_index], list1[j]

    return list1


if __name__ == "__main__":
    print("Binary Search using Recursive approach")
    print("Producing an array of random numbers ....... ")
    print("Enter size of Array")
    size_of_list = int(input())
    list_random = create_list(size_of_list)
    list_sorted = sort_list(list_random)
    print("The array generated is : ", list_sorted)
    print("Enter the number to be searched in the array ")
    key = int(input())

    ans = binary_search_using_recursive_approach(list_sorted, key, 0, len(list_sorted) - 1)
    if ans == -1:
        print("Given Element not found in Array !!!")
    else:
        print("Given Element found at : ", ans, " position in the array")
