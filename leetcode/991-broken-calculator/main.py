"""
    1st: brute force BFS
    e.g. X=1024, Y=1
    it takes 1023 steps, the tree will be of height 1023...

    Time    O(2^N)
    Space   O(2^N)
    TLE
"""


class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        q = [(X, 0)]
        while len(q) > 0:
            num, steps = q.pop(0)
            if num == Y:
                return steps
            if num <= 0 or num > 10**9:
                continue
            q.append((X*2, steps+1))
            q.append((X-1, steps+1))
        return -1


"""
    2nd: math, work backwards greedily, learned from others
    - when current > target, we either /2 to reach to the target(if its an even) OR +1 to reach to the target(if its an odd)
    - after the above, we only do +1 from the current to the target

    ref:
    - https://leetcode.com/problems/broken-calculator/solution/
    - https://leetcode.com/problems/broken-calculator/discuss/234484/JavaC%2B%2BPython-Change-Y-to-X-in-1-Line

    Time    O(logN)
    Space   O(1)
    16 ms, faster than 73.33%
"""


class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        steps = 0
        while Y > X:
            if Y % 2 == 0:
                Y //= 2
            else:
                Y += 1
            steps += 1
        return steps + X - Y
