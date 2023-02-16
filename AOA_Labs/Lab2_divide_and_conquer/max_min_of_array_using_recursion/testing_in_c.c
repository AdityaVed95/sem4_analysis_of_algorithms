#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct {
    int min;
    int max;
} MinMax;

MinMax findMinMax(int arr[], int low, int high) {
    MinMax result, left, right;

    // Base case: If array has only one element
    if (low == high) {
        result.min = arr[low];
        result.max = arr[low];
        return result;
    }

    // If array has 2 elements:
    else if (low == high - 1) {
        if (arr[low] > arr[high]) {
            result.min = arr[high];
            result.max = arr[low];
        }
        else {
            result.min = arr[low];
            result.max = arr[high];
        }
        return result;
    }

    // If array has more than 2 elements:
    else {
        int mid = (low + high) / 2;
        left = findMinMax(arr, low, mid);
        right = findMinMax(arr, mid + 1, high);

        if (left.min < right.min) {
            result.min = left.min;
        }
        else {
            result.min = right.min;
        }

        if (left.max > right.max) {
            result.max = left.max;
        }
        else {
            result.max = right.max;
        }

        return result;
    }
}

MinMax findMinMaxBasic(int arr[], int size) {
    MinMax result;
    result.min = arr[0];
    result.max = arr[0];

    for (int i = 1; i < size; i++) {
        if (arr[i] < result.min) {
            result.min = arr[i];
        }
        else if (arr[i] > result.max) {
            result.max = arr[i];
        }
    }

    return result;
}

int main() {
    int size_of_list;
    printf("Enter size of list: ");
    scanf("%d", &size_of_list);

    int list1[size_of_list];
    srand(time(NULL));
    for (int i = 0; i < size_of_list; i++) {
        list1[i] = rand() % 1000000000;
    }

    MinMax min_max_list, min_max_basic;
    double start, end;

    start = (double)clock() / CLOCKS_PER_SEC;
    min_max_list = findMinMax(list1, 0, size_of_list - 1);
    end = (double)clock() / CLOCKS_PER_SEC;

    printf("Using Recursive using Divide and Conquer Approach:\n");
    printf("Minimum number is: %d and Maximum number is: %d\n", min_max_list.min, min_max_list.max);
    printf("Time taken for finding max and min no of list using divide conquer using recursion is: %f\n", end - start);

    start = (double)clock() / CLOCKS_PER_SEC;
    min_max_basic = findMinMaxBasic(list1, size_of_list);
    end = (double)clock() / CLOCKS_PER_SEC;

    printf("Now using Basic Approach without divide and conquer:\n");
    printf("Minimum number is: %d and Maximum number is: %d\n", min_max_basic.min, min_max_basic.max);
    printf("Time taken for finding max and min no of list using basic approach is: %f\n", end - start);

    return 0;
}
