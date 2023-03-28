import merge_sort_on_list_of_object


# this file is used to optimise the order for approach 1 and approach 2
# in approach we select the max profit element 1st
# in case 2 items with equal profit and different weights
# this file has the optimisation of picking the item with less weight and same profit 1st

# similarly the optimisation of picking up more profit item with the same weight in approach2 is
# an optimisation which I have implemented in this file

def optimise_items_sorted_by_profit(no_of_items, items_sort_based_on_profit):
    i = 0

    while i < no_of_items - 1:

        if items_sort_based_on_profit[i].getProfit() != items_sort_based_on_profit[i + 1].getProfit():
            i += 1
            continue

        else:
            j = i
            while j < no_of_items - 1:
                if items_sort_based_on_profit[j].getProfit() == items_sort_based_on_profit[j + 1].getProfit():
                    j += 1
                    continue
                else:
                    break
            #       sorting range (for sorting by weight) is from i to j
            merge_sort_on_list_of_object.merge_sort(items_sort_based_on_profit, i, j, 'weight', 'ascending')

            i = j + 1

    # for i in range(no_of_items):
    #     print(items_sort_based_on_profit[i].getProfit())
    #     print(items_sort_based_on_profit[i].getWeight())
    #     print("=========")


def optimise_items_sorted_by_weight(no_of_items, items_sort_based_on_weight):
    i = 0

    while i < no_of_items - 1:

        if items_sort_based_on_weight[i].getWeight() != items_sort_based_on_weight[i + 1].getWeight():
            i += 1
            continue

        else:
            j = i
            while j < no_of_items - 1:
                if items_sort_based_on_weight[j].getWeight() == items_sort_based_on_weight[j + 1].getWeight():
                    j += 1
                    continue
                else:
                    break
            #       sorting range (for sorting by weight) is from i to j
            merge_sort_on_list_of_object.merge_sort(items_sort_based_on_weight, i, j, 'profit', 'descending')

            i = j + 1

    # for i in range(no_of_items):
    #     print(items_sort_based_on_weight[i].getProfit())
    #     print(items_sort_based_on_weight[i].getWeight())
    #     print("=========")


# note :
# the usage of below function will actually not make any difference to
# the final profit obtained since we are considering the ratio of profit
# by weight , thus below optimisation function is not called from main.py
def optimise_items_sorted_based_on_ratio_profit_by_weight(no_of_items, items_sort_based_on_ratio_profit_by_weight):
    i = 0

    while i < no_of_items - 1:

        if items_sort_based_on_ratio_profit_by_weight[i].getProfitByWeight() != \
                items_sort_based_on_ratio_profit_by_weight[i + 1].getProfitByWeight():
            i += 1
            continue

        else:
            j = i
            while j < no_of_items - 1:
                if items_sort_based_on_ratio_profit_by_weight[j].getProfitByWeight() == \
                        items_sort_based_on_ratio_profit_by_weight[j + 1].getProfitByWeight():
                    j += 1
                    continue
                else:
                    break
            #       sorting range (for sorting by weight) is from i to j
            merge_sort_on_list_of_object.merge_sort(items_sort_based_on_ratio_profit_by_weight, i, j, 'weight',
                                                    'ascending')

            i = j + 1

    for i in range(no_of_items):
        print(items_sort_based_on_ratio_profit_by_weight[i].getProfit())
        print(items_sort_based_on_ratio_profit_by_weight[i].getWeight())
        print("=========")
