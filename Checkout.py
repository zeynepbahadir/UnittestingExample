class Checkout():
    class Discount:
        def __init__(self, numOfItems, price):
            self.numOfItems = numOfItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}
    
    def addItemPrice(self, item, price):
        self.prices[item] = price
    
    def addItem(self, item):
        if item not in self.prices:
            raise Exception("Bad item")
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def CalculateTotal(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.CalculateItemTotal(item, cnt)
        return total
    
    def addDiscount(self, item, numOfItems, price):
        discount = self.Discount(numOfItems, price)
        self.discounts[item] = discount

    def CalculateItemTotal(self, item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.numOfItems:
                numOfDiscounts = cnt/discount.numOfItems
                total += numOfDiscounts * discount.price
                remaining = cnt % discount.numOfItems
                total += remaining * self.prices[item]
            else: 
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt
        return total