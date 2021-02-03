"""
    1st: greedy
    - come up the target character one by one from the left
    e.g. 

    source = xyz, target = xzyxz

    xz | y | xz
     1   2   3

    1. iterate xyz, remove xz from xzyxz
    2. iterate xyz, remove y from yxz
    3. iterate xyz, remove xz from xz
    4. the target is now an empty string

    Time    O(ST)
    Space   O(T)
    52 ms, faster than 52.00%
"""


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        count = 0
        remain = target
        while True:
            i = 0
            for c in source:
                if i < len(remain) and c == remain[i]:
                    i += 1
            if i == 0:
                return -1
            count += 1
            remain = remain[i:]
            if len(remain) == 0:
                break
        return count
