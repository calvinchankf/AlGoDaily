from typing import List


"""
    1st: array
    - multiply string of m by k to see if the substring = target

    Time    O(NM)
    Space   O(N)
    32 ms, faster than 100.00% 
"""


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        total = m * k
        for i in range(len(arr)):
            window = arr[i:i+total]
            sub = window[:m]
            temp = sub * k
            if tuple(temp) == tuple(window):
                return True
        return False


s = Solution()

a = [1, 2, 4, 4, 4, 4]
b = 1
c = 3
print(s.containsPattern(a, b, c))

a = [1, 2, 1, 2, 1, 1, 1, 3]
b = 2
c = 2
print(s.containsPattern(a, b, c))

a = [1, 2, 1, 2, 1, 3]
b = 2
c = 3
print(s.containsPattern(a, b, c))

a = [1, 2, 3, 1, 2]
b = 2
c = 2
print(s.containsPattern(a, b, c))

a = [2, 2, 2, 2]
b = 2
c = 3
print(s.containsPattern(a, b, c))
