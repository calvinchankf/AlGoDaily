"""
    1st approach: sort

    corner cases:
    - empty array
    - duplicate numbers

    Time    O(nlogn)
    Space   O(n)
    32 ms, faster than 94.31%
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        cur = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                continue
            if nums[i-1]+1 == nums[i]:
                cur += 1
                res = max(res, cur)
            else:
                cur = 1
        return res


s = Solution()

a = [100, 4, 200, 1, 3, 2]
print(s.longestConsecutive(a))

a = [100, 4, 200, 1, 3, 2, 7, 8, 6, 9, 10]
print(s.longestConsecutive(a))

a = [100, 4, 200, 1, 3, 2, 5, 7, 8, 6, 9]
print(s.longestConsecutive(a))

print("-----")

"""
    2nd approach: union find
    Time    O(nlogn)
    Space   O(n)
    100 ms, faster than 9.12%
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hs = set(nums)
        uf = UnionFind(hs)
        for num in nums:
            left = uf.find(num-1)
            right = uf.find(num+1)
            if left != None:
                uf.union(num, left)
            if right != None:
                uf.union(num, right)
        longest = 0
        for key in uf.caps:
            longest = max(longest, uf.caps[key])
        return longest


class UnionFind(object):
    def __init__(self, vertices):
        self.count = len(vertices)
        self.ids = {}
        self.caps = {}
        for vertex in vertices:
            self.ids[vertex] = vertex
            self.caps[vertex] = 1

    def find(self, key):
        # loop to find to ultimate root
        if key not in self.ids:
            return None
        cur = key
        while cur != self.ids[cur]:
            cur = self.ids[cur]
        return cur

    def union(self, p, q):
        if p not in self.ids or q not in self.ids:
            return
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        # attach to the larger tree
        if self.caps[pId] < self.caps[qId]:
            self.ids[pId] = qId
            self.caps[qId] += self.caps[pId]
        else:
            self.ids[qId] = pId
            self.caps[pId] += self.caps[qId]
        self.count -= 1


s = Solution()

a = [100, 4, 200, 1, 3, 2]
print(s.longestConsecutive(a))

a = [100, 4, 200, 1, 3, 2, 7, 8, 6, 9, 10]
print(s.longestConsecutive(a))

a = [100, 4, 200, 1, 3, 2, 5, 7, 8, 6, 9]
print(s.longestConsecutive(a))

print("-----")

"""
    2nd: hashtable
    - similar to lc5, expand to the left, expand to the right
    - use a hashtable to avoid redundant calculation
    - similar to algoexpert: largest range

    Time    O(N)
    Space   O(N)
    32 ms, faster than 99.43%
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        hs = set(nums)
        res = 0
        for i in range(len(nums)):
            x = nums[i]
            # avoid redundancy
            if x in seen:
                continue
            # explore on the left
            left = x
            while left - 1 in hs:
                left -= 1
                seen.add(left)
            # explore on the right
            right = x
            while right + 1 in hs:
                right += 1
                seen.add(right)
            res = max(res, right - left + 1)
        return res


s = Solution()

a = [100, 4, 200, 1, 3, 2]
print(s.longestConsecutive(a))

a = [100, 4, 200, 1, 3, 2, 7, 8, 6, 9, 10]
print(s.longestConsecutive(a))

a = [100, 4, 200, 1, 3, 2, 5, 7, 8, 6, 9]
print(s.longestConsecutive(a))
