from typing import List

"""
    1st: hashtable
    - use a hashtable to store all { productID: price, productID: price, ....}
    - use an integer to store the n-th, rotate back to zero if its == n, therefore to avoid overflow

    Time of init        O(P)
    Time of getBill     O(P)
    Space               O(Products * Price)
    780 ms, faster than 85.80%
"""


class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.rotatingCount = 0
        self.discount = discount
        self.productPrices = {}
        for i in range(len(products)):
            product = products[i]
            price = prices[i]
            self.productPrices[product] = price

    def getBill(self, products: List[int], amounts: List[int]) -> float:
        x = 0
        for i in range(len(products)):
            product = products[i]
            amount = amounts[i]
            price = self.productPrices[product] * amount
            x += price
        self.rotatingCount += 1
        if self.rotatingCount == self.n:
            self.rotatingCount = 0
            return x - (self.discount * x) / 100
        return x


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
