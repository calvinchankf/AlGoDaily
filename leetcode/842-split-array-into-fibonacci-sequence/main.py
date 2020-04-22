from typing import List

"""
    1st: recursion
    - similar to lc306
    - generate pairs to get started
    - use recursion to try all the possibilities

    Time    O(N^2 + N!)
    136 ms, faster than 30.20%
"""


class Solution:
    def splitIntoFibonacci(self, s: str) -> List[int]:
        for i in range(1, len(s)-1):

            raw_a = s[:i]
            a = int(raw_a)
            if (len(raw_a) > 1 and raw_a[0] == '0') or a > 2**31-1:
                continue

            for j in range(i+1, len(s)):

                raw_b = s[i:j]
                b = int(raw_b)
                if len(raw_b) > 1 and raw_b[0] == '0' or b > 2**31-1:
                    continue

                temp = self.dfs(a, b, s[j:])
                if temp != None:
                    return [a, b] + temp
        return []

    def dfs(self, a: int, b: int, s: str) -> List[int]:
        if len(s) == 0:
            # print('dfs', a, b)
            return []
        res = None
        for i in range(len(s)):

            temp = s[:i+1]
            num = int(temp)
            if len(temp) > 1 and temp[0] == '0' or num > 2**31-1:
                continue

            if a + b == num:
                suffix = self.dfs(b, num, s[i+1:])
                if suffix != None:
                    res = [num] + suffix
        return res


s = Solution()

a = '123456579'
print(s.splitIntoFibonacci(a))

a = "11235813"
print(s.splitIntoFibonacci(a))

a = "112358130"
print(s.splitIntoFibonacci(a))

a = "0123"
print(s.splitIntoFibonacci(a))

a = "1101111"
print(s.splitIntoFibonacci(a))

a = "112358"
print(s.splitIntoFibonacci(a))

a = "0112358"
print(s.splitIntoFibonacci(a))

a = "199100199"
print(s.splitIntoFibonacci(a))

a = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
print(s.splitIntoFibonacci(a))
