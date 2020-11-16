"""
    0th: binary search + 2 pointers

    Time of add()   O(N)
    Time of find()  O(N)
    Space           O(N)
    688 ms, faster than 12.52%
"""


from collections import *


class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        i = self.__upperBsearch(self.nums, number)
        self.nums.insert(i, number)

    def __upperBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        left = 0
        right = len(self.nums) - 1
        while left < right:
            total = self.nums[left] + self.nums[right]
            if total < value:
                left += 1
            elif total > value:
                right -= 1
            else:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)


"""
    2nd: hashtable

    Time of add()   O(1)
    Time of find()  O(N)
    Space           O(N)
    336 ms, faster than 69.16%
"""


class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ht = Counter()

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.ht[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.ht:
            remain = value - num
            if remain in self.ht:
                if num != remain:
                    return True
                elif self.ht[num] > 1:
                    return True
        return False
