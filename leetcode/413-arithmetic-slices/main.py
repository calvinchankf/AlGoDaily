"""
    1st: math

    e.g. [1, 2, 3, 4, 5, 7, 9, 11]
    diff =  [1, 1, 1, 1, 2, 2, 2]

    for [1, 2, 3, 4, 5], we can come up with 4(3)/2 = 6
    for [5, 7, 9, 11], we can come up with 3(2)/2 = 3
    result = 6 + 3 = 9

    Time    O(N)
    Space   O(N)
    28 ms, beats 97.75%
"""


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        n = len(A)
        diffs = []
        for i in range(1, n):
            diffs.append(A[i] - A[i-1])
        res = 0
        cur = diffs[0]
        count = 1
        for i in range(1, len(diffs)):
            if diffs[i] == cur:
                count += 1
            else:
                if count >= 2:
                    res += self.cal(count)
                cur = diffs[i]
                count = 1
        if count >= 2:
            res += self.cal(count)
        return res

    def cal(self, n):
        return n * (n-1) // 2
