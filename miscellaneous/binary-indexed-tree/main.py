"""
    Binary Indexed Tree(BIT)
    - is the optimal way for mutable range query

    ref:
    - query:    https://www.youtube.com/watch?v=RgITNht_f4Q
    - update:   https://www.youtube.com/watch?v=B-BkW9ZpKKM

    Time    O(logN)
    Space   O(N)
"""


class BinaryIndexedTree(object):

    def __init__(self, n):
        self.fenwickTree = (n+1) * [0]

    def update(self, i, val):
        """
        new i = i + least significant bit(i)
        e.g. start from 5
        5     00101
        6     00110 (becos 00101 + 00001)
        8     01000 (becos 00110 + 00010)
        16    10000 (becos 01000 + 01000)
        """
        k = i + 1
        while k < len(self.fenwickTree):
            self.fenwickTree[k] += val
            k += k & -k

    def getSum(self, i):
        """
        flip the least significant bit 1 by 1 to the left until 0
        e.g. start from 14
        14    1110
        12    1100 (1110 - 0010)
        8     1000 (1100 - 0100)
        0     0000 (1000 - 1000)
        """
        s = 0
        k = i + 1
        while k > 0:
            s += self.fenwickTree[k]
            k -= k & -k
        return s

    def getRangeSum(self, i, j):
        return self.getSum(j) - self.getSum(i-1)


# a = [0,0,0,0,0]
bitree = BinaryIndexedTree(5)

# a = [1,0,0,0,0]
bitree.update(0, 1)
print(bitree.getSum(4))             # 1

# a = [1,3,0,0,0]
bitree.update(1, 3)
print(bitree.getSum(4))             # 4

# a = [1,3,5,0,0]
bitree.update(2, 5)
print(bitree.getSum(4))             # 9

# a = [1,3,5,7,0]
bitree.update(3, 7)
print(bitree.getSum(4))             # 16

# a = [1,3,5,7,9]
bitree.update(4, 9)
print(bitree.getSum(4))             # 25

# a = [1,4,5,7,9]
bitree.update(1, 1)
print(bitree.getSum(4))             # 26
print(bitree.getRangeSum(1, 2))     # 9

# a = [1,4,0,7,9]
bitree.update(2, -6)
print(bitree.getSum(4))             # 20
print(bitree.getRangeSum(1, 2))     # 3
