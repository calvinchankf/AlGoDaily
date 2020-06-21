import time
"""
    1st: brute force recursion + hashtable

    Time    O(4^N)
    Space   O(4^N)
    LTE
"""


class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        start_time = time.time()
        if len(nums) == 0:
            return False
        total = sum(nums)
        L = total // 4
        if L * 4 != total:
            return False
        nums.sort()
        self.ht = {}
        result = self.dfs(nums, L, L, L, L)
        print(round(time.time() - start_time, 5), 'sec')
        return result

    def dfs(self, nums, ra, rb, rc, rd):
        if len(nums) == 0:
            return ra == rb == rc == rd == 0
        if ra < 0 or rb < 0 or rc < 0 or rd < 0:
            return False
        key = (len(nums), ra, rb, rc, rd)
        if key in self.ht:
            return self.ht[key]
        first = nums[0]
        remain = nums[1:]
        result = self.dfs(remain, ra - first, rb, rc, rd) or \
            self.dfs(remain, ra, rb - first, rc, rd) or \
            self.dfs(remain, ra, rb, rc - first, rd) or \
            self.dfs(remain, ra, rb, rc, rd - first)
        self.ht[key] = result
        return result


s = Solution()

a = [1, 1, 2, 2, 2]
print(s.makesquare(a))

a = [3, 3, 3, 3, 4]
print(s.makesquare(a))

a = [13, 1, 1, 1]
print(s.makesquare(a))

a = 16 * [1]
print(s.makesquare(a))

# LTE: 22 / 174 test cases passed.
a = [3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
print(s.makesquare(a))

# LTE: 53 / 174 test cases passed.
a = [20, 13, 19, 19, 4, 15, 10, 5, 5, 15, 14, 11, 3, 20, 11]
print(s.makesquare(a))

# LTE: 129 / 174 test cases passed.
a = [5969561, 8742425, 2513572, 3352059, 9084275, 2194427, 1017540,
     2324577, 6810719, 8936380, 7868365, 2755770, 9954463, 9912280, 4713511]
# print(s.makesquare(a))

print("-----")

"""
    2nd approach: backtracking + hashtable
    - but 2 choices at a time for each number
    - exactly the same as lc698

    Time    O(N 2^N)
    Space   O(2^N)
    1100 ms, faster than 61.36%
"""


class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        start_time = time.time()
        if len(nums) == 0:
            return False
        total = sum(nums)
        L = total // 4
        if L * 4 != total:
            return False

        used = len(nums) * [False]
        result = self.dfs(nums, L, 0, 4, 0, used)
        print(round(time.time() - start_time, 5), 'sec')
        return result

    def dfs(self, nums, target, curSum, k, start, used):
        if k == 1:
            return True
        if curSum == target:
            return self.dfs(nums, target, 0, k-1, 0, used)
        for i in range(start, len(nums)):
            if used[i] == False:
                used[i] = True
                if self.dfs(nums, target, curSum+nums[i], k, i+1, used):
                    return True
                used[i] = False
        return False


s = Solution()

a = [1, 1, 2, 2, 2]
print(s.makesquare(a))

a = [3, 3, 3, 3, 4]
print(s.makesquare(a))

a = [13, 1, 1, 1]
print(s.makesquare(a))

a = 16 * [1]
print(s.makesquare(a))

# LTE: 22 / 174 test cases passed.
a = [3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
print(s.makesquare(a))

# LTE: 53 / 174 test cases passed.
a = [20, 13, 19, 19, 4, 15, 10, 5, 5, 15, 14, 11, 3, 20, 11]
print(s.makesquare(a))

# LTE: 129 / 174 test cases passed.
a = [5969561, 8742425, 2513572, 3352059, 9084275, 2194427, 1017540,
     2324577, 6810719, 8936380, 7868365, 2755770, 9954463, 9912280, 4713511]
print(s.makesquare(a))
