from typing import List

"""
    1st: sort

    Time    O(N MlogM) N: number of l & r, M: average length of subarray
    Space   O(N)
    176 ms, faster than 83.33%
"""
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(l)
        res = n * [True]
        for i in range(n):
            left = l[i]
            right = r[i]
            sub = nums[left: right+1]
            sub.sort()
            diff = sub[1] - sub[0]
            for j in range(2, len(sub)):
                if sub[j] - sub[j-1] != diff:
                    res[i] = False
                    break
        return res
    
s = Solution()

a = [4,6,5,9,3,7]
b = [0,0,2]
c = [2,3,5]
print(s.checkArithmeticSubarrays(a, b, c))

a = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
b = [0,1,6,4,8,7]
c = [4,4,9,7,9,10]
print(s.checkArithmeticSubarrays(a, b, c))