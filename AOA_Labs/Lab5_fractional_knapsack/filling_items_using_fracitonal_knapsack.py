def fill_items_into_the_bag(no_of_items: int, capacity: float, items_sorted: list):
    amount_filled = 0
    counter = 0
    selection_made = [0] * no_of_items

    while counter < no_of_items:
        if amount_filled >= capacity:
            break

        if items_sorted[counter].getWeight() <= (capacity - amount_filled):
            amount_filled = amount_filled + items_sorted[counter].getWeight()
            selection_made[counter] = 1
            counter += 1

        else:
            amount_remaining = capacity - amount_filled
            fraction = amount_remaining / items_sorted[counter].getWeight()
            selection_made[counter] = fraction
            counter += 1
            amount_filled = capacity

    for i in range(no_of_items):
        print("profit of item  : ", items_sorted[i].getProfit())
        print("weight of item  : ", items_sorted[i].getWeight())
        print("amount selected : ", selection_made[i])
        print("===============")

    total_profit = 0
    for i in range(no_of_items):
        total_profit = total_profit + selection_made[i] * items_sorted[i].getProfit()

    print("total profit using this approach :  = ", total_profit)
