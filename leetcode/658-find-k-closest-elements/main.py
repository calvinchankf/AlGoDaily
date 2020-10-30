"""
    1st: binary search

    Time        O(logN + K + KlogK)
    Space       O(K)
    308 ms, faster than 61.39%
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = self.bsearch(arr, x)
        res = [arr[idx]]
        i = idx - 1
        j = idx + 1
        while i >= 0 and j < len(arr) and len(res) < k:
            if abs(arr[i] - x) <= abs(arr[j] - x):
                res.append(arr[i])
                i -= 1
            else:
                res.append(arr[j])
                j += 1
        while i == -1 and len(res) < k:
            res.append(arr[j])
            j += 1
        while j == len(arr) and len(res) < k:
            res.append(arr[i])
            i -= 1
        return sorted(res)
    
    def bsearch(self, arr, target):
        n = len(arr)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if target == arr[mid]:
                return mid
            elif target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        if right < 0:
            return 0
        if left > n - 1:
            return n-1
        # compare
        if abs(target-arr[left]) < abs(target-arr[right]):
            return left
        return right


import heapq

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