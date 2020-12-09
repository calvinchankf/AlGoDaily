"""
    1st: brute force
    - 2 and 5 cannot come up with any number that ends with '1'
    - loop every possibility of num = 10 * num + 1

    Time    O(?)
    Space   O(1)
    1980 ms, faster than 26.71%
"""


class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        num = 1
        count = 1
        while num % K != 0:
            num = 10*num + 1
            count += 1
        return count


"""
    2nd: optimized
    - same logic as 1st
    - but we do num = (10*num + 1) % K to avoid integer overflow
    - Since there are K numbers (from 0 to K-1), the Time Complexity is O(K)

    Time    O(K)
    Space   O(1)
    1980 ms, faster than 26.71%
"""


class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        num = 1
        count = 1
        while num % K != 0:
            num = (10*num + 1) % K
            count += 1
        return count
