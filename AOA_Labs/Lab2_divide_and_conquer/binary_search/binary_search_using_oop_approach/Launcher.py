import time

from binary_search_tester import BinarySearchTester


def printResult(ans: int):
    if ans == -1:
        print("Given Element not found in Array !!!")
    else:
        print("Given Element found at : ", ans, " position in the array")


def main():
    print("Binary Search using Recursive approach")
    print("Producing an array of random numbers ....... ")
    print("Enter size of Array")
    size_of_list = int(input())

    testObject = BinarySearchTester()

    list_random = testObject.create_list(size_of_list)
    list_sorted = testObject.sort_list(list_random)
    print("The array generated is : ", list_sorted)
    print("Enter the number to be searched in the array ")
    key = int(input())

    print("Using Iterative Approach : ")
    start1 = time.time()
    ans1 = testObject.binary_search_using_iterative_approach(list_sorted, key, 0, len(list_sorted) - 1)
    end1 = time.time()
    printResult(ans1)

    print("Using Recursive Approach : ")
    start2 = time.time()
    ans2 = testObject.binary_search_using_recursive_approach(list_sorted, key, 0, len(list_sorted) - 1)
    end2 = time.time()
    printResult(ans2)

    print("Time taken by Iterative approach : ", (end1-start1))
    print("Time taken by Recursive approach : ", (end2-start2))

if __name__ == "__main__":
    main()
