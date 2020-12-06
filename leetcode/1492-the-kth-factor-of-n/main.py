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
        root = int(n**0.5)
        fronts, backs = [], []
        for i in range(1, root + 1):
            remain = n // i
            if i * remain != n:
                continue
            if i == remain:
                fronts.append(i)
            else:
                fronts.append(i)
                backs.append(remain)
        factors = fronts + backs[::-1]
        if k-1 < 0 or k-1 == len(factors):
            return -1
        return factors[k-1]
