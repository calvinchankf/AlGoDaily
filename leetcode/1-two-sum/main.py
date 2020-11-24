"""
    questions to ask:
    - return the indices or the values? indices
    - should i give u back one pair or all paris? one <- res = [] if yes
    - will there be any duplicates? no <- save indices/count if yes
    - use once? yes
"""

"""
    1st approach: hashtable

    Time  O(n)
    Space O(n)
    40 ms, faster than 66.68%
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ht = {}
        for i in range(len(nums)):
            x = nums[i]
            remain = target - x
            if remain in ht:
                return [ht[remain], i]
            ht[x] = i
        return []


"""
    2nd approach: sort + 2 pointers

    Time    O(nlogn)
    Space   O(n)
    40 ms, faster than 73.58%
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr = []
        for i in range(len(nums)):
            arr.append([nums[i], i])  # [num, index]
        arr = sorted(arr, key=lambda x: x[0])
        left = 0
        right = len(arr) - 1
        while left < right:
            temp = arr[left][0] + arr[right][0]
            if temp == target:
                return [arr[left][1], arr[right][1]]
                # if all pairs and use once
                # left += 1
                # right -= 1
            elif temp < target:
                left += 1
            else:
                right -= 1


"""
    3rd approach: sort + binary search

    Time    O(nlogn)
    Space   O(n)
    44 ms, faster than 62.57%
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr = []
        for i in range(len(nums)):
            arr.append([nums[i], i])  # [num, index]
        arr = sorted(arr, key=lambda x: x[0])
        # iterate through the array and binary search the partner in remaining array
        for i in range(len(arr)-1):
            remain = target - arr[i][0]
            j = self.bsearch(arr, i+1, remain)
            if j > -1:
                return [arr[i][1], arr[j][1]]

    def bsearch(self, nums, start, target):
        left = start
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if target < nums[mid][0]:
                right = mid - 1
            elif target > nums[mid][0]:
                left = mid + 1
            else:
                return mid
        return -1


"""
    followup1:
    - what if here might be no solution or more than one solution
    - no duplicates, still

    1st approach: hashtable

    e.g.
     0  1  2  3  4   5  6   7  8  9
    [5, 2, 3, 6, 7, 12, 4, 15, 8, 1]

    target = 8, pairs = (1,3), (0,2),
    target = 100, pairs = empty
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ht = {}
        res = []
        for i in range(len(nums)):
            num = nums[i]
            remain = target - num
            if remain in ht:
                res.append((ht[remain], i))
            else:
                ht[num] = i
        return res


print(Solution().twoSum([5, 2, 3, 6, 7, 12, 4, 15, 8, 1], 8))
print(Solution().twoSum([5, 2, 3, 6, 7, 12, 4, 15, 8, 1], 100))
print("-----")

"""
    followup2: every number can be used once, print the indices

    e.g.1
     0  1  2  3  4  5  6
    [5, 2, 5, 2, 2, 3, 4] 7
    _____  ____     ____

    result  = [[0, 1], [2, 3], [5, 6]]

    e.g.2
     0  1  2  3  4  5  6
    [5, 5, 2, 2, 2, 3, 4] 7
    _____  ____     ____

    result  = [[1, 2], [0, 3], [5, 6]]
    Note that [[0, 2], [1, 3], [5, 6]] is also correct
"""


class Solution(object):
    def twoSum(self, nums, target):
        res = []
        ht = {}
        for i in range(len(nums)):
            x = nums[i]
            remain = target - x
            if remain in ht:
                j = ht[remain].pop()
                res.append([j, i])
                if len(ht[remain]) == 0:
                    del ht[remain]
            else:
                if x not in ht:
                    ht[x] = []
                ht[x].append(i)
        return res


s = Solution()

a = [5, 2, 5, 2, 2, 3, 4]
b = 7
print(s.twoSum(a, b))

a = [5, 5, 2, 2, 2, 3, 4]
b = 7
print(s.twoSum(a, b))
