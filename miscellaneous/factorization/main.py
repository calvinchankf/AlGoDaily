from math import sqrt, ceil

"""
    factorization

    Time    O(sqrt(N))
    Space   O(sqrt(N)) <- the result array
"""


def getFactors(n):
    root = int(ceil(sqrt(n)))
    res = set()
    for i in range(1, root+1):
        if n % i == 0:
            res.add(i)
            res.add(n//i)

    return res


print(getFactors(500))
