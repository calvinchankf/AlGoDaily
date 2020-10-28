from typing import List
from collections import Counter

"""
    1st: sliding window + hashtable
    - similar to lc3, 159, 340, 1248
    - the crux of the problem based on the fact that:
        1. atMostK(nums, K) - atMostK(nums, K-1) = exactlyK(nums, K)
        2. to find the number of subarrays with atMost K, we use res += i - j + 1

    e.g.

    aabab
    1       <- a
     2      <- a, aa
      3     <- b, ab, aab
       4    <- a, ba, aba, aaba
        5   <- b, ab, bab, abab, aabab
    so there total 16 substrings that at most have 2 distinct charactors

    ref:
    https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/235002/One-code-template-to-solve-all-of-these-problems!

    Time    O(N)
    Space   O(N)
    704 ms, faster than 34.71%
"""


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.subarraysWithAtMostKDistinct(A, K) - self.subarraysWithAtMostKDistinct(A, K-1)

    def subarraysWithAtMostKDistinct(self, A, K):
        window = Counter()
        j = 0
        res = 0
        for i in range(len(A)):
            c = A[i]
            window[c] += 1
            while len(window) > K:
                last = A[j]
                window[last] -= 1
                if window[last] == 0:
                    del window[last]
                j += 1
            res += i - j + 1
        return res


"""
    2nd: same as 1st but different Implementation

    ref:
    - https://leetcode.com/problems/subarrays-with-k-different-integers/solution/

    Time    O(N)
    Space   O(N)
    704 ms, faster than 34.71%
"""


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        window1 = Window()
        window2 = Window()
        res = 0
        left1, left2 = 0, 0

        for i in range(len(A)):
            window1.add(A[i])
            window2.add(A[i])
            while window1.size() > K:
                window1.remove(A[left1])
                left1 += 1
            while window2.size() > K-1:
                window2.remove(A[left2])
                left2 += 1
            res += left2 - left1
        return res


class Window:
    def __init__(self):
        self.counter = Counter()

    def add(self, x):
        self.counter[x] += 1

    def remove(self, x):
        self.counter[x] -= 1
        if self.counter[x] == 0:
            del self.counter[x]

    def size(self):
        return len(self.counter)
