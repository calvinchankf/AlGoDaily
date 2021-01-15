"""
    greedy? previous lexicographical permutation algorithm?

    - similar to lc3, 556, 1053

    idea:
    - find the pivot and the successor
    - pivot is the first number that doesnt follow the non-decreasing order from the back
    - successor is the left most index of the closest number <= pivot

    [1, 9, 9, 4, 6, 7, 7, 10]
           ^
         pivot
                    ^
                first smaller(successor)
    
    - swap the pivot and successor

    ref:
    - https://www.youtube.com/watch?v=qwFSeqYH6jc

    Time    O(N)
    Space   O(1)
    236 ms, faster than 25.39% 
"""


class Solution:
    def prevPermOpt1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # find the first non-decreasing number
        i = n - 1
        while i - 1 >= 0 and nums[i-1] <= nums[i]:
            i -= 1
        if i == 0:
            return nums
        pivot = i - 1
        # find the successor, successor is the first number just smaller than the pivot
        firstSmaller = i
        for j in range(i, n):
            if nums[j] < nums[pivot] and nums[j] > nums[firstSmaller]:
                firstSmaller = j
        # swap the numbers at pivot and the successor
        nums[pivot], nums[firstSmaller] = nums[firstSmaller], nums[pivot]
        return nums
