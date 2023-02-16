from typing import Tuple
import random
import time


#  here we use type annotations to specify the return type of the find_max_min function:
def find_min_max(list_search: list, low: int, high: int) -> Tuple[int, int]:
    """
    Finds the maximum and minimum elements in the given array/list using
    divide and conquer approach

    low is the least index of the list
    high is the max index of the list

    """

    # Base case: If array has only one element
    if low == high:
        return list_search[low], list_search[low]  # returns tuple

    # If array has 2 elements :
    elif low == high - 1:
        if list_search[low] > list_search[high]:
            return list_search[high], list_search[low]

        else:
            return list_search[low], list_search[high]  # correct

    # If array has more than 2 elements :

    else:
        mid = (low + high) // 2
        left_min_number, left_max_number = find_min_max(list_search, low, mid)
        right_min_number, right_max_number = find_min_max(list_search, mid + 1, high)

        min_of_right_and_left_both = 0
        max_of_right_and_left_both = 0

        if left_min_number < right_min_number:
            min_of_right_and_left_both = left_min_number
        else:
            min_of_right_and_left_both = right_min_number

        if left_max_number > right_max_number:
            max_of_right_and_left_both = left_max_number
        else:
            max_of_right_and_left_both = right_max_number

        return min_of_right_and_left_both, max_of_right_and_left_both


def find_min_max_using_basic_approach(list_search: list) -> Tuple[int, int]:
    min_no = list_search[0]
    max_no = list_search[0]
    for number in list_search:
        if number > max_no:
            max_no = number
        elif number < min_no:
            min_no = number

    return min_no, max_no


def main():
    print("Enter size of list : ")
    size_of_list = int(input())
    list1 = []
    i = 0
    while i < size_of_list:
        list1.append(random.randint(0, 1000000000000))
        i += 1

    # print(list1)
    start = time.time()
    min_no_of_list, max_no_of_list = find_min_max(list1, 0, len(list1) - 1)
    end = time.time()
    print("Using Recursive using Divide and Conquer Approach : ")
    print("Minimum number is : ", min_no_of_list, " and Maximum number is : ", max_no_of_list)
    print("Time taken for finding max and min no of list using divide conquer using recursion is : ", (end - start))

    print("Now using Basic Approach without divide and conquer")
    start = time.time()
    min_no, max_no = find_min_max_using_basic_approach(list1)
    end = time.time()
    print("Minimum number is : ", min_no, " and Maximum number is : ", max_no)
    print("Time taken for finding max and min no of list using basic approach is : ", (end - start))


if __name__ == "__main__":
    main()
