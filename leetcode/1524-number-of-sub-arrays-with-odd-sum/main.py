"""
    2nd: learned from others

    odd + even = odd
    even + odd = odd
    odd + odd = even
    even + even = even

    For each element in the array:
    - if current prefix sum is even, res += the number of odd prefix sum
    - if current prefix sum is odd, res += the number of even prefix sum

    e.g. [1,2,2]
    
    [*, 2, 2] 
        ^ we increment our result by the number of odds
    
    [*, 2, 2] 
           ^ we increment our result by the number of odds again
    
    Same logic applies to [x,y,x,2,2] if x+y+x is odd. Also, vice versa.

    Time    O(N)
    Space   O(1)
    1356 ms, faster than 60.00%
"""


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        total = 0  # prefix sum
        odd = 0
        even = 1  # the current prefix sum is 0, which is even
        res = 0
        for i in range(len(arr)):
            total = (total + arr[i]) % 2
            if total % 2 == 0:
                res += odd
                even += 1
            else:
                res += even
                odd += 1
        return res % (10**9+7)
