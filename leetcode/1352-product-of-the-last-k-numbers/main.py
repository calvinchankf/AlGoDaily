"""
    1st: prefix sum
    - corner case: zero
        - we need to store the position of the last zero
        - so that if the k go backend beyond the last zero, we can just return 0 as a result

    Time    O(1)
    Space   O(N)
    312 ms, faster than 57.68%
"""


class ProductOfNumbers(object):

    def __init__(self):
        self.lastZeroIdx = -1
        self.products = []

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.lastZeroIdx = len(self.products)

        if len(self.products) == 0:
            self.products.append(num)
        else:
            if self.products[-1] == 0:
                self.products.append(num)
            else:
                self.products.append(num * self.products[-1])

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        idx = len(self.products) - k - 1
        if idx < self.lastZeroIdx:
            return 0
        prev = self.products[idx]
        if idx == -1 or prev == 0:
            return self.products[-1]
        return self.products[-1] / prev


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
