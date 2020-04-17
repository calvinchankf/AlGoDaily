"""
    1st: recursion
    - generate pairs to get started
    - use recursion to try all the possibilities

    Time    O(N^2 + N!)
    36 ms, faster than 6.37%
"""


class Solution:
    def isAdditiveNumber(self, s: str) -> bool:
        for i in range(1, len(s)-1):
            raw_a = s[:i]
            if len(raw_a) > 1 and raw_a[0] == '0':
                continue
            a = int(raw_a)

            for j in range(i+1, len(s)):
                raw_b = s[i:j]
                if len(raw_b) > 1 and raw_b[0] == '0':
                    continue
                b = int(raw_b)

                if self.dfs(a, b, s[j:]):
                    return True
        return False

    def dfs(self, a: int, b: int, s: str) -> bool:
        if len(s) == 0:
            return True
        res = False
        for i in range(len(s)):
            temp = s[:i+1]
            if len(temp) > 1 and temp[0] == '0':
                continue
            num = int(temp)
            if a + b == num:
                res = res or self.dfs(b, num, s[i+1:])
        return res


s = Solution()

a = "112358"
print(s.isAdditiveNumber(a))

a = "199100199"
print(s.isAdditiveNumber(a))

a = "101"
print(s.isAdditiveNumber(a))

a = "100"
print(s.isAdditiveNumber(a))

a = "1001"
print(s.isAdditiveNumber(a))

a = "10010"
print(s.isAdditiveNumber(a))
