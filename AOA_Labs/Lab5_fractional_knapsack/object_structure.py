class Item:

    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
        self.ratio_profit_by_weight = profit / weight

    def getWeight(self):
        return self.weight

    def getProfit(self):
        return self.profit

    def getProfitByWeight(self):
        return self.ratio_profit_by_weight
