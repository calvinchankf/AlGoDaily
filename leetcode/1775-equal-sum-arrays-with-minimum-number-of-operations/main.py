"""
    1st: sort
    - hinted from others
    - in the larger array, every number can only be decreased down to 1
    - in the smaller array, every number can only be increased up to 6
    - sort the diffs until the target_diff <= 0
    - if larger array with all ones > smaller array with all 6s, return -1

    ref:
    - https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/discuss/1085859/Python-O(nlogn)-(faster-than-100.00)-with-explanation

    Time    O(NlogN)
    Space   O(N)
    1248 ms, faster than 100.00%
"""
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        A, B = sum(nums1), sum(nums2)
        
        larger = nums1
        smaller = nums2
        if B > A:
            larger = nums2
            smaller = nums1
        elif A == B:
            return 0
        
        gains_in_larger = [x-1 for x in larger]
        gains_in_smaller = [6-x for x in smaller]
        gains = gains_in_larger + gains_in_smaller
        gains.sort(reverse = True)
        
        count = 0
        target_diff = abs(A - B)
        
        for i in range(len(gains)):
            target_diff -= gains[i]
            count += 1
            if target_diff <= 0:
                return count
        return -1