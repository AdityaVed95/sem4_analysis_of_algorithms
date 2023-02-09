import random
import time

print("Enter size of Array")
size_of_list = int(input())

list1 = []

i = 0
while i < size_of_list:
    list1.append(random.randint(0, 1000))
    i += 1

print("The input list is :")
print(list1)
count = 0

start = time.time()
for index in range(size_of_list - 1):
    minimum_index = index  # minimum_index
    # is the index at which the number is minimum (in the unsorted array)

    for j in range(index + 1, size_of_list):
        count += 1
        if list1[j] < list1[minimum_index]:
            minimum_index = j

    # swap list1[index] and list1[minimum_index]
    if minimum_index != index:
        temp = list1[index]
        list1[index] = list1[minimum_index]
        list1[minimum_index] = temp
    # above 3 lines can be replaced by the below line
    # (list1[index], list1[minimum_index]) = (list1[minimum_index], list1[index])

    print("The list after ", index, " pass is ", list1)

end = time.time()

print("number of comparisons : ", count)
print("Time takes is : ", end - start)
# print("sorted list is : ")
# print(list1)
