
from collections import *

"""
    1st: 2 pointers
    - similar to lc3, 76
    
    e.g. abcabc

     L
    abcabc
      R
    Soon after we moved our L pointer (to the point that the window doesnt contain all 3 chars), we add L to our result.
    In this case, res += 1, it means we add 'abc' to the result

      L
    abcabc
       R
    res += 2, it means we add 'abca', 'bca' to the result

       L
    abcabc
        R
    res += 3, it means we add 'abcab', 'bcab', 'cab' to the result

        L
    abcabc
         R
    res += 4, it means we add 'abcabc', 'bcabc', 'cabc', 'abc' to the result

    Time    O(N)
    Space   O(N)
    320 ms, faster than 32.63%
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        j = 0
        res = 0
        counter = Counter()
        for i in range(len(s)):
            counter[s[i]] += 1
            while len(counter) == 3:
                left = s[j]
                counter[left] -= 1
                if counter[left] == 0:
                    del counter[left]
                j += 1
            res += j    # crux
        return res
