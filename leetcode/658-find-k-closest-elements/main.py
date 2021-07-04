"""
    1st: nearest binary search

    Time        O(logN + K)
    Space       O(K)
    308 ms, faster than 61.39%
"""
import heapq


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        centerIdx = self.bSearchNearest(arr, x)
        left, right = centerIdx, centerIdx
        k -= 1
        while k > 0:
            if left-1 >= 0 and right+1 < n:
                if abs(arr[left-1] - x) < abs(arr[right+1] - x):
                    left -= 1
                elif abs(arr[left-1] - x) > abs(arr[right+1] - x):
                    right += 1
                else:
                    left -= 1
            elif left-1 < 0:
                right += 1
            elif right+1 == n:
                left -= 1
            k -= 1
        return arr[left:right+1]

    def bSearchNearest(self, nums, target):
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            mid = (left + right)//2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        # bounds checking
        if right < 0:
            return 0
        if left > n-1:
            return n-1
        # compare
        if abs(target - nums[right]) <= abs(target - nums[left]):
            return right
        return left


"""
    2nd: heap

    Time    O(NlogN + KlogK)
    Space   O(N)
    400 ms, faster than 20.44%
"""


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pq = []
        for num in arr:
            diff = abs(num - x)
            heapq.heappush(pq, (diff, num))
        res = []
        while len(res) < k:
            diff, num = heapq.heappop(pq)
            res.append(num)
        return sorted(res)
