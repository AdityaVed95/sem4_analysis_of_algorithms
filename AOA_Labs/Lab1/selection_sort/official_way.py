list1 = [64, 25, 12, 22, 11]

for i in range(0, len(list1)):
    least_index = i
    for j in range(i, len(list1)):
        if list1[j] < list1[least_index]:
            list1[j], list1[least_index] = list1[least_index], list1[j]

print(list1)

# for i in range(5):
#     print(i)


# for i in range(0, len(list1)):
#     least_index = i
#     for j in range(i, len(list1)):
#         if list1[j] < list1[least_index]:
#             least_index = j
#
#         list1[j], list1[least_index] = list1[least_index], list1[j]

