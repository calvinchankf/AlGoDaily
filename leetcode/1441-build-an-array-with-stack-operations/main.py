"""
    1st: math

    Time    O(N)
    Space   O(N) <- result
    32 ms, faster than 91.18%
"""


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        i = 0
        while i < len(target):
            diff = None
            if i == 0:
                diff = target[i]
            else:
                diff = target[i] - target[i-1]
            if diff > 1:
                res += (diff - 1) * ['Push', 'Pop']
                res += ['Push']
            else:
                res += ['Push']
            i += 1
        return res
