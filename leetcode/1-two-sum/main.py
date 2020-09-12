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
            num = nums[i]
            remain = target - num
            if remain in ht:
                return [i, ht[remain]]
            ht[num] = i
        return [-1, -1]


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
    followup:
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
    2nd approach: binary search

    e.g.
     0  1  2  3  4   5  6   7  8  9
    [5, 2, 3, 6, 7, 12, 4, 15, 8, 1]

    target = 8, pairs = (1,3), (0,2), (5, 9)
    target = 100, pairs = empty
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
        res = []
        for i in range(len(arr)-1):
            remain = target - arr[i][0]
            j = self.bsearch(arr, i+1, remain)
            if j > -1:
                res.append([arr[i][1], arr[j][1]])
        return res

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


print(Solution().twoSum([5, 2, 3, 6, 7, 12, 4, 15, 8, 1], 8))
print(Solution().twoSum([5, 2, 3, 6, 7, 12, 4, 15, 8, 1], 100))
print("-----")


"""
    followup2:
    - there are duplicates
    - just give me the count

    e.g.
     0  1  2  3  4  5  6  7  8  9, 10, 11
    [5, 2, 3, 6, 7, 2, 4, 5, 8, 6, 4, 4]

    5: [0, 7]
    2: [1, 5]
    3: [2]
    6: [3,9]
    7: [4]
    4: [6, 10, 11]
    8: [8]
    target = 8, pairs(idx) = (0,2), (7,2), (1,3), (1,9), (5,3), (5,9), (6,10), (6,11), (10,11) total = 9
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ht = {}
        count = 0
        for i in range(len(nums)):
            num = nums[i]
            # cal the remain
            remain = target - num
            if remain in ht:
                count += len(ht[remain])
            # put into the hashtable
            if num not in ht:
                ht[num] = [i]
            else:
                ht[num].append(i)
        return count


print(Solution().twoSum([5, 2, 3, 6, 7, 2, 4, 5, 8, 6, 4, 4], 8))
print(Solution().twoSum([5, 2, 3, 6, 7, 2, 4, 5, 8, 6], 100))
print("-----")

"""
    or store the count
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ht = {}
        count = 0
        for i in range(len(nums)):
            num = nums[i]
            # cal the remain
            remain = target - num
            if remain in ht:
                count += ht[remain]
            # put into the hashtable
            if num not in ht:
                ht[num] = 1
            else:
                ht[num] += 1
        return count


print(Solution().twoSum([5, 2, 3, 6, 7, 2, 4, 5, 8, 6, 4, 4], 8))
print(Solution().twoSum([5, 2, 3, 6, 7, 2, 4, 5, 8, 6], 100))
print("--yo--")

"""
    followup3:
    - 2 arrays instead of one array
    - no duplicate on each array
    - all pairs(indices)

    e.g.
    a = [5, 3, 9, 8, 7, 11]
    b = [3, 6, 0, 1, 2, 12]
    target = 9

    result = [(nums1 index, nums2 index), ....]
    = (1, 1), (2, 2), (3, 3), (4, 4)

    Time    O(nlogn)
    Space   O(n)
"""


class Solution(object):

    def twoSum(self, nums1, nums2, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr = []
        for i in range(len(nums2)):
            arr.append([nums2[i], i])  # [num, index]
        arr = sorted(arr, key=lambda x: x[0])

        res = []
        for i in range(len(nums1)):
            remain = target - nums1[i]
            idx = self.bsearch(arr, remain)
            if idx > -1:
                res.append([i, arr[idx][1]])
        return res

    def bsearch(self, nums, target):
        left = 0
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


a = [5, 3, 9, 8, 7, 11]
b = [3, 6, 0, 1, 2, 12]
print(Solution().twoSum(a, b, 9))
