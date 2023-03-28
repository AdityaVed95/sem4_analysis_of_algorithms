import merge_sort_on_list_of_object
import optimise_order
from object_structure import Item
from filling_items_using_fracitonal_knapsack import fill_items_into_the_bag
import copy

print("Enter the number of input items ")
no_of_items = int(input())

list_of_items = []

for i in range(no_of_items):
    print("Enter the profit of ", (i + 1), "th element")
    p = int(input())
    print("Enter the weight of ", (i + 1), "th element")
    w = int(input())
    list_of_items.append(Item(p, w))

print("Enter the total weight capacity of Big Bag :")
capacity = int(input())

# creating deep copies of the original list
items_sort_based_on_weight = copy.deepcopy(list_of_items)
items_sort_based_on_profit = copy.deepcopy(list_of_items)
items_sort_based_on_ratio_profit_by_weight = copy.deepcopy(list_of_items)

# sorting each list based on their parameter(profit or weight or profit/weight) and
# their order(asc or des)

merge_sort_on_list_of_object.merge_sort(items_sort_based_on_profit, 0, no_of_items - 1, 'profit', 'descending')
merge_sort_on_list_of_object.merge_sort(items_sort_based_on_weight, 0, no_of_items - 1, 'weight', 'ascending')
merge_sort_on_list_of_object.merge_sort(items_sort_based_on_ratio_profit_by_weight, 0, no_of_items - 1,
                                        'ratio_profit_by_weight', 'descending')

print("\n¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥\n")

# print("optimise_items_sorted_by_profit : ")
optimise_order.optimise_items_sorted_by_profit(no_of_items, items_sort_based_on_profit)

# print("optimise_items_sorted_by_weight")
optimise_order.optimise_items_sorted_by_weight(no_of_items, items_sort_based_on_weight)

# print("Note : The order of putting items in the bag is the order in which they are displayed")
# print("So the item displayed 1st is put in the bag 1st\n")

# filling of maximum profit first :
print("Approach 1 : taking maximum profit elements : ")
fill_items_into_the_bag(no_of_items, capacity, items_sort_based_on_profit)

print("\n¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥\n")

# filling of minimum weight first :
print("Approach 2 : taking minimum weight elements : ")
fill_items_into_the_bag(no_of_items, capacity, items_sort_based_on_weight)

print("\n¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥\n")

# filling of maximum profit/weight first :
print("Approach 3 : taking maximum profit by weight elements : ")
fill_items_into_the_bag(no_of_items, capacity, items_sort_based_on_ratio_profit_by_weight)
