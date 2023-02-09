unsorted_list = [64, 25, 12, 22, 11]
sorted_list = []

for i in range(0, len(unsorted_list)):
    # find the smallest element in unsorted list and put it to the left most side of the unsorted list

    # for number in unsorted_list:
    #     if number < unsorted_list[0]:
    #         number, unsorted_list[0] = unsorted_list[0], number  # swap the no and 1st element of unsorted list

    for j in range(1, len(unsorted_list)):
        if unsorted_list[j] < unsorted_list[0]:
            unsorted_list[j], unsorted_list[0] = unsorted_list[0], unsorted_list[j]

    shortest_num_of_unsorted_list = unsorted_list.pop(0)
    sorted_list.append(shortest_num_of_unsorted_list)

print(sorted_list)
