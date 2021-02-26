"""
    1st approach: hashset
    - 2sum concept
    - but since we only count the unique pairs, we use a hashset
    - remove mirrored key to return the result

    e.g. nums = [1, 1, 1, 2, 1], k = 1
    set = {
        (1,2),
        (2,1),
    }
    remove the (2,1) from result

    Time    O(N)
    Space   O(N)
    124 ms, faster than 45.14% 
"""


from collections import Counter


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        seen = set()
        res = set()
        for i in range(len(nums)):
            num = nums[i]
            up = num + k
            down = num - k
            if up in seen:
                res.add((num, up))
            if down in seen:
                res.add((down, num))
            seen.add(num)
        return len(res)


a = [3, 1, 4, 1, 5]
b = 2
print(Solution().findPairs(a, b))

a = [1, 2, 3, 4, 5]
b = 1
print(Solution().findPairs(a, b))

a = [1, 3, 1, 5, 4]
b = 0
print(Solution().findPairs(a, b))

a = [1, 3, 1, 1, 5, 4]
b = 0
print(Solution().findPairs(a, b))

a = [1, 3, 1, 1, 5, 4, 4, 4, 4]
b = 0
print(Solution().findPairs(a, b))

a = [1, 2, 3, 4, 5]
b = -1
print(Solution().findPairs(a, b))

a = [1, 1, 1, 2, 1]
b = 1
print(Solution().findPairs(a, b))

print("-----")

"""
    2nd approach: sort + hashtable

    Time    O(NlogN)
    Space   O(N)
    60 ms, faster than 85.40%
"""


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        seen = set()
        res = set()
        for x in nums:
            if x - k in seen:
                res.add((x-k, x))
            seen.add(x)
        return len(res)


a = [3, 1, 4, 1, 5]
b = 2
print(Solution().findPairs(a, b))

a = [1, 2, 3, 4, 5]
b = 1
print(Solution().findPairs(a, b))

a = [1, 3, 1, 5, 4]
b = 0
print(Solution().findPairs(a, b))

a = [1, 3, 1, 1, 5, 4]
b = 0
print(Solution().findPairs(a, b))

a = [1, 3, 1, 1, 5, 4, 4, 4, 4]
b = 0
print(Solution().findPairs(a, b))

a = [1, 2, 3, 4, 5]
b = -1
print(Solution().findPairs(a, b))

a = [1, 1, 1, 2, 1]
b = 1
print(Solution().findPairs(a, b))
