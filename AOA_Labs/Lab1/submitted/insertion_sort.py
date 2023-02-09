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
for i in range(1, len(list1)):

    key = list1[i]

    j = i - 1
    while j >= 0 and key < list1[j]:
        count += 1  # counting number of comparisons
        list1[j + 1] = list1[j]
        j -= 1

    list1[j + 1] = key

    print("The list after ", i, " pass is ", list1)
end = time.time()

print("number of comparisons : ", count)
print("Time takes is : ", end - start)
# print("sorted list is : ")
# print(list1)
