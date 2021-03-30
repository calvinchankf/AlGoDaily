"""
    1st: 2pointers + math
    - similar to lc15
    
    need to consider 3 cases
    
    case0: [1, 2, 2, 2, 2, 2]
               ^  ^  ^  ^  *
    there are five 2s in total, we need the combination of picking 2 of 5, which is 4(5)/2 = 10

    case1: [1, 2, 2, x, 2, 2, 2]
               ^  ^     *  *  *
    there are five 2s in total, we need the combination of picking 2 of 5, which is 4(5)/2 = 10

    case2: [1, 2, 2, 3, 5, 5, 5]
               ^  ^     *  *  *
    there are two 2s and three 5s, the combination is 2 * 3 = 6

    Therefore, we can come up with this:
    if _left == _right:
        count = (a + 1) * a // 2
    else:
        count = a * b

    Time    O(N^2)
    Space   O(1)
    5636 ms, faster than 5.27% 
"""


class Solution:
    def threeSumMulti(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:

                    _left, _right = nums[left], nums[right]
                    a, b = 1, 1

                    while left+1 < right and nums[left] == nums[left+1]:
                        a += 1
                        left += 1
                    left += 1

                    while left <= right-1 and nums[right-1] == nums[right]:
                        b += 1
                        right -= 1
                    right -= 1

                    count = 0
                    if _left == _right:
                        count = (a + 1) * a // 2
                    else:
                        count = a * b

                    res += count
                    res %= 10**9 + 7

                elif total < target:
                    left += 1
                else:
                    right -= 1
        return res
