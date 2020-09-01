"""
1st: dynamic programming
- bottom up recursion + hashtable
- generate all the possibilities by recursion
- cache the array of temporary result of number on each layer, ie. (num, N) to avoid redundant calculation

Time    O(N^2) -> O(2^N)
Space   O(N^2) -> O(2^N)
40 ms, faster than 71.91%
"""


class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.ht = {}
        res = set()
        start = 1
        for i in range(start, 10):
            temp = self.dfs(N, K, i)
            for x in temp:
                res.add(int(x))
        return list(res)

    def dfs(self, N, K, num):
        if num < 0 or num > 9:
            return []
        if N == 1:
            return [str(num)]

        # comment these 2 lines u will get: 64 ms, faster than 12.36%
        if (num, N) in self.ht:
            return self.ht[(num, N)]

        left = self.dfs(N-1, K, num-K)
        right = self.dfs(N-1, K, num+K)

        res = []
        for x in left:
            res.append(str(num) + x)
        for y in right:
            res.append(str(num) + y)
        self.ht[(num, N)] = res
        return res


s = Solution()
a = 3
b = 7
print(s.numsSameConsecDiff(a, b))

a = 2
b = 1
print(s.numsSameConsecDiff(a, b))

a = 4
b = 2
print(s.numsSameConsecDiff(a, b))

a = 1
b = 0
print(s.numsSameConsecDiff(a, b))

a = 3
b = 0
print(s.numsSameConsecDiff(a, b))


print("-----")

"""
    2nd: brute force iteration, learned from others

    ref:
    - https://leetcode.com/problems/numbers-with-same-consecutive-differences/discuss/211183/JavaC%2B%2BPython-Iterative-Solution

    Time    O(2^N)
    Space   O(2^N)
    28 ms, faster than 100.00%
"""


class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        cur = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for _ in range(2, N+1):
            cur2 = []
            for x in cur:
                # get the last digit
                y = x % 10
                # add new digit by y-K, y+K
                if x > 0 and y + K < 10:
                    cur2.append(x * 10 + y + K)
                if x > 0 and K > 0 and y - K >= 0:
                    cur2.append(x * 10 + y - K)
            cur = cur2
        return cur
