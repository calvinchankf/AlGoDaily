from collections import defaultdict
"""
    1st: binary search
    - sort the array
    - upper bound binary search to look for the earliest idx pointing to the legit age(target = 0.5 * ages[i] + 7)
    - lower bound binary search to look for the earlieest idx pointing to the same age with target

    Time    O(3 * NlogN)
    Space   O(1)
    1012 ms, faster than 5.01%
"""


class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        res = 0
        ages = sorted(ages)
        for i in range(len(ages)):
            target = 0.5 * ages[i] + 7
            legitAgeEarliestIdx = self.upperBsearch(ages, i, target)
            # different legit ages
            res += i - legitAgeEarliestIdx
            # same age
            sameAgeEarliestIdx = self.lowerBsearch(
                ages, legitAgeEarliestIdx, i, ages[i]
            )
            res += i - sameAgeEarliestIdx
        return res

    def upperBsearch(self, nums, idx, target):
        left = 0
        right = idx
        while left < right:
            mid = (left + right)//2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left

    def lowerBsearch(self, nums, left, right, target):
        while left < right:
            mid = (left + right)//2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()

a = [16, 16]  # 2
print(s.numFriendRequests(a))

a = [16, 17, 18]  # 2
print(s.numFriendRequests(a))

a = [20, 30, 100, 110, 120]  # 3
print(s.numFriendRequests(a))

a = [24, 69, 8, 85, 85]  # 4
print(s.numFriendRequests(a))

print("-----")

"""
    2nd: hashtable
    - 1 <= ages.length <= 20000 and 1 <= ages[i] <= 120 means that there are a lot of people having the same ages
    - for each age a != b if b is legit, we will make count[a] * count[b] requests
    - for each age a == b, count[a] * (count[b] - 1) requests (exclude self)

    Time    O(n^2) but n <= 120
    Space   O(n)
    320 ms, faster than 53.58%
"""


class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        res = 0
        counts = defaultdict(int)
        for age in ages:
            counts[age] += 1
        for a in counts:
            for b in counts:
                if self.aCanRequestB(a, b):
                    if a == b:
                        res += counts[a] * (counts[b] - 1)
                    else:
                        res += counts[a] * counts[b]
        return res

    def aCanRequestB(self, a, b):
        if b > a:
            return False
        if b <= 0.5 * a + 7:
            return False
        return True


s = Solution()

a = [16, 16]  # 2
print(s.numFriendRequests(a))

a = [16, 17, 18]  # 2
print(s.numFriendRequests(a))

a = [20, 30, 100, 110, 120]  # 3
print(s.numFriendRequests(a))

a = [24, 69, 8, 85, 85]  # 4
print(s.numFriendRequests(a))
