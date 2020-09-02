from collections import deque
import bisect

"""
    1st approach: brute force
    
    Time  O(n^2)
    Space O(k)
    TLE
"""


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) < k or len(nums) == 0 or k <= 0:
            return []
        res = []
        window = []
        temp = 0
        for i in range(k):
            window.append(nums[i])
        temp = self.findMax(window)
        res.append(temp)
        for i in range(k, len(nums)):
            window = window[1:]
            window.append(nums[i])
            temp = self.findMax(window)
            res.append(temp)
        return res

    def findMax(self, nums):
        res = nums[0]
        for num in nums:
            res = max(num, res)
        return res


"""
    2nd approach: binary search
    - use binary search to maintain a sorted list(window) all the array to the end
    - each window maximum is the last item in each window 

    Time  O(nlogk) -> O(nk)
    Space O(k)
    180 ms, faster than 42.16%
"""


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) < k or len(nums) == 0 or k <= 0:
            return []
        res = []
        window = []

        for i in range(len(nums)):

            # remove left most item starting from k+1 th
            if i >= k:
                # O(logk) to remove the left most item with binary search
                targetToRemove = nums[i-k]
                idxToRemove = bisect.bisect_left(window, targetToRemove)
                window.pop(idxToRemove)

            # O(logk) to add the current item to a correct place in the window
            idxToAdd = bisect.bisect_left(window, nums[i])
            window.insert(idxToAdd, nums[i])

            # append result starting from k th
            if i+1 >= k:
                # last item in the window is the max
                res.append(window[-1])
        return res


"""
    3rd: deque(double-ended queue) <- suggested approach

    - the idea is monotonic queue: when you push an element, a monotonic queue pop all the items smaller than that 
    e.g. [1,3,-1,-3,5,3,6,7]

                                window          max
    [1] 3 -1 -3 5 3 6 7         [1]             n/a
    [1 3] -1 -3 5 3 6 7         [3]             n/a
    [1 3 -1] -3 5 3 6 7         [3, -1]         3
    1 [3 -1 -3] 5 3 6 7         [3,-1,-3]       3
    1 3 [-1 -3 5] 3 6 7         [5]             5
    1 3 -1 [-3 5 3] 6 7         [5,3]           5
    1 3 -1 -3 [5 3 6] 7         [6]             6
    1 3 -1 -3 5 [3 6 7]         [7]             7


    Time    O(2N)
    Space   O(N)
"""


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        def clean_deque(i):
            # remove indexes of elements not in sliding window
            # since we push item one by one, the first one is guaranteed to be the one to remove if len(window) > k
            if len(deq) > 0 and deq[0] == i - k:
                deq.popleft()
            # remove from deq indexes of all elements
            # which are smaller than current element nums[i]
            while len(deq) > 0 and nums[i] > nums[deq[-1]]:
                deq.pop()

        # init deque and output
        deq = deque()
        output = []
        # build output
        for i in range(n):  # for i in range(k, n):
            clean_deque(i)
            deq.append(i)

            if i+1 >= k:
                output.append(nums[deq[0]])
        return output
