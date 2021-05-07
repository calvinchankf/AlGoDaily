"""
    1st: greedy? math?
    
    case1: n=5, k=4
    we can build the result = [1, 5, 2, 4, 3] in a zig-zag way

    case2: n=8, k=4
    we can build the part of the result = [1, 5, 2, 4, 3] in a zig-zag way
    and then put the remaining numbers with a diff of 1 [6, 7, 8]
    then the result will be [1, 5, 2, 4, 3, 6, 7, 8]

    Time    O(N)
    Space   O(N) the result
    40 ms, faster than 96.55%
"""


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = []
        left, right = 1, k + 1
        for i in range(k+1):
            if i % 2 == 0:
                res.append(left)
                left += 1
            else:
                res.append(right)
                right -= 1
        for i in range(k+1, n):
            res.append(i+1)
        return res
