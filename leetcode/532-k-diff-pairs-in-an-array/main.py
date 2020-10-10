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

    Time    O(n)
    Space   O(n)
    124 ms, faster than 45.14% 
"""


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
                res.add((up, num))
            if down in seen:
                res.add((down, num))
            seen.add(num)
        final = set()
        for left, right in res:
            if k == 0 or (right, left) not in final:
                final.add((left, right))
        return len(final)


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
    2nd approach: simply the 1st approach of using hashtable
    - count the occurence of each number
    - there are 2 cases:
        - if k > 0, and if key + k in hashtalbe, increment the count
        - if k == 0, and if m[key] > 1, increment the count

    e.g.1
    nums = [1, 1, 1, 2, 1], k = 1
    counter = {
        1: 4,
        2: 1
    }
    1+k=2, 2 is in the hashtbale so increment the count

    e.g.2
    nums = [1, 1, 1, 2, 1], k = 0
    counter = {
        1: 4,
        2: 1
    }
    k == 0, ones appear more than once in the hashtbale so increment the count

    Time    O(n)
    Space   O(n)
    104 ms, faster than 73.71% 
"""


class Solution(object):
    def findPairs(self, nums, k):
        m = {}
        for num in nums:
            if num not in m:
                m[num] = 1
            else:
                m[num] += 1
        res = 0
        for key in m:
            if (k > 0 and key + k in m) or (k == 0 and m[key] > 1):
                res += 1
        return res


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

from collections import Counter

"""
    3rd: remove the paired number from the hashtable

    Time    O(NlogN + logN)
    Space   O(N)
    88 ms, faster than 97.98% 
"""
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        ht = Counter(nums)
        res = set()
        for x in nums:
            if x + k in ht:
                if x == x + k:
                    if ht[x] > 1:
                        res.add((x, x))
                        ht[x + k] -= 1
                elif ht[x + k] > 0:
                    res.add((x, x+k))
                    ht[x + k] -= 1
        return len(res)