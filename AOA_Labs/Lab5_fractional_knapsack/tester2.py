from object_structure import Item

# import copy
#
# list1 = [10, 20, 30, 40]


# list2 = list1
# list2.append(50)
# print(list1)
# print(list2)
#
# list3 = copy.deepcopy(list1)
# list3.append(60)
# print(list1)
# print(list3)

sort_by = 'weight'
list1 = [Item(1, 2), Item(3, 4), Item(5, 6)]
print(getattr(list1[0], sort_by))
setattr(list1[0], sort_by, 10)
print(getattr(list1[0], sort_by))
