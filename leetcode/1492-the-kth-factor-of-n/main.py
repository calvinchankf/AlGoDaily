from math import sqrt

"""
    1st: math + sort

    Time    O(k + klogk ) k = sqrt(N)
    Space   O(2 * sqrt(N))
    36 ms, faster than 25.00%
"""


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        root = int(sqrt(n))
        factors = []
        for i in range(1, root + 1):
            partner = n // i
            if i * partner == n:
                factors.append(i)
                if i != partner:
                    factors.append(partner)
        factors.sort()
        if k < 1 or k > len(factors):
            return - 1
        return factors[k-1]


"""
    1st: math

    Time    O(k) k = sqrt(N)
    Space   O(2 * sqrt(N))
    28 ms, faster than 75.00%
"""


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        root = int(sqrt(n))
        fronts, backs = [], []
        for i in range(1, root + 1):
            partner = n // i
            if i * partner == n:
                fronts.append(i)
                if i != partner:
                    backs.append(partner)
        factors = fronts + backs[::-1]
        if k < 1 or k > len(factors):
            return - 1
        return factors[k-1]
