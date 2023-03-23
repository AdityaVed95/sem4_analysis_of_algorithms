# this is how we initially started :
# the below approach/program is incorrect

from Lab3_merge_quick_sort import merge_sort_acc_to_algo

print("Enter the number of input items ")
no_of_items = int(input())
weight_of_items = []
profit_of_items = []

for i in range(no_of_items):
    print("Enter the weight of ", (i + 1), "th element")
    weight_of_items.append(int(input()))
    print("Enter the profit of ", (i + 1), "th element")
    profit_of_items.append(int(input()))

print("Enter the total weight capacity of Big Bag :")
capacity = int(input())

profit_by_weight_of_items = []

for i in range(no_of_items):
    profit_by_weight_of_items.append(profit_of_items[i] / weight_of_items[i])

print(profit_by_weight_of_items)

merge_sort_acc_to_algo.merge_sort(profit_by_weight_of_items, 0, no_of_items - 1)

# now the profit_by_weight_of_items list has been sorted using
# merge sort , this steps takes O( n * log(n) ) time complexity

weight_filled_in_bag = 0
counter = 0

while True:

    if weight_filled_in_bag >= capacity:
        break
