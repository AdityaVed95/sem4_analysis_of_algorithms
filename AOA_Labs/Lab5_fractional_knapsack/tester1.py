from object_structure import Item
from merge_sort_on_list_of_object import merge, merge_sort

list1 = [Item(10, 20), Item(3, 4), Item(50, 6)]
merge_sort(list1, 0, len(list1) - 1, 'weight')

for i in range(3):
    print(list1[i].weight)
for i in range(3):
    print(list1[i].profit)
