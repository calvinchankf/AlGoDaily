from sys import maxsize
from typing import List
from collections import OrderedDict, Counter

"""
    1st: hashtable

    Time    O(N^2)
    Space   O(N)
    LTE
"""


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        seen = set()
        res = []
        for i in range(len(rains)):
            x = rains[i]
            if x > 0:
                if x in seen:
                    return []
                seen.add(x)
                res.append(-1)
            else:
                found = False
                for j in range(i+1, len(rains)):
                    y = rains[j]
                    if y in seen:
                        res.append(y)
                        seen.remove(y)
                        found = True
                        break
                if found == False:
                    res.append(1)
        return res


s = Solution()

# a = [1, 2, 3, 4]
# print(s.avoidFlood(a))

# a = [1, 2, 0, 0, 2, 1]
# print(s.avoidFlood(a))

# a = [1, 2, 0, 1, 2]
# print(s.avoidFlood(a))

# a = [69, 0, 0, 0, 69]
# print(s.avoidFlood(a))

# a = [10, 20, 20]
# print(s.avoidFlood(a))

# a = [1, 0, 2, 0]
# print(s.avoidFlood(a))

# a = [1, 2, 0, 2, 3, 0, 1]
# print(s.avoidFlood(a))

# a = [1, 0, 2, 3, 0, 1, 2]
# print(s.avoidFlood(a))

# a = [3, 5, 4, 0, 1, 0, 1, 5, 2, 8, 9]
# print(s.avoidFlood(a))

# a = [0, 1, 1]
# print(s.avoidFlood(a))

# a = [97, 0, 98, 99, 0, 97, 98]
# print(s.avoidFlood(a))

print("-----")

"""
    2nd: hashtable

    Time    O(N * K) K depends on the number of distinct numbers
    Space   O(N)
    74 / 78 test cases passed
"""


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ht = {}
        for i in range(len(rains)):
            x = rains[i]
            if x == 0:
                continue
            if x in ht:
                ht[x].append(i)
            else:
                ht[x] = [i]

        seen = set()
        res = []
        for i in range(len(rains)):
            x = rains[i]
            if x > 0:
                if x in seen:
                    return []
                seen.add(x)
                ht[x].pop(0)
                if len(ht[x]) == 0:
                    del ht[x]
                res.append(-1)
            else:
                target = maxsize
                for key in ht:
                    if key in seen:
                        target = min(target, ht[key][0])

                if target != maxsize:
                    res.append(rains[target])
                    seen.remove(rains[target])
                else:
                    res.append(1)
        return res


s = Solution()

a = [1, 2, 3, 4]
print(s.avoidFlood(a))

a = [1, 2, 0, 0, 2, 1]
print(s.avoidFlood(a))

a = [1, 2, 0, 1, 2]
print(s.avoidFlood(a))

a = [69, 0, 0, 0, 69]
print(s.avoidFlood(a))

a = [10, 20, 20]
print(s.avoidFlood(a))

a = [1, 0, 2, 0]
print(s.avoidFlood(a))

a = [1, 2, 0, 2, 3, 0, 1]
print(s.avoidFlood(a))

a = [1, 0, 2, 3, 0, 1, 2]
print(s.avoidFlood(a))

a = [3, 5, 4, 0, 1, 0, 1, 5, 2, 8, 9]
print(s.avoidFlood(a))

a = [0, 1, 1]
print(s.avoidFlood(a))

a = [97, 0, 98, 99, 0, 97, 98]
print(s.avoidFlood(a))

print("-----")

"""
    3rd: hashtable + binary search
    - when we see a zero, dont dry any lake yet. Please put it in candidates first
    - because afterward when we see a seen number, we can use the zeors from candicates to dry a lake
    - since it is possible that there are duplicate numbers between zeros, we should use binary search to find which zeros to use for drying

    e.g. [97, 0, 98, 99, 0, 97, 98]
    idx   0   1   2   3  4   5   6

    After idx = 4
    hashtable of (num: idx) = {
        97: 0,
        98: 2,
        99: 3,
    }
    zeros = [1,4]
    res = [-1, 1, -1, -1, 1, x, x]

    At idx = 5, 
    - we binary search 0 in [1,4] thus get the first zero, use it to update our result
    - and zeros.pop(0)
    - and update hashtable[97] to 5
    hashtable of (num: idx) = {
        97: 5,
        98: 2,
        98: 3,
    }
    zeros = [4]
    res = [-1, 97, -1, -1, 1, -1, x]

    At idx = 6, 
    - we binary search 0 in [4] thus get the first zero, use it to update our result
    - and zeros.pop(0)
    - and update hashtable[99] to 6
    hashtable of (num: idx) = {
        97: 5,
        98: 2,
        99: 6,
    }
    zeros = []
    res = [-1, 97, -1, -1, 98, -1, -1]


    Time    O(NlogN) -> O(N * K) binary search takes O(logN) but arr.pop(k) takes O(K)
    Space   O(N)
    1400 ms, faster than 35.21%
"""


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = []
        ht = {}
        zeros = []
        for i in range(len(rains)):
            x = rains[i]
            if x == 0:
                zeros.append(i)
                res.append(1)
            else:
                res.append(-1)
                if x in ht:
                    idx = self.bsearch(zeros, ht[x])
                    if 0 <= idx < len(zeros):
                        res[zeros[idx]] = x
                        zeros.pop(idx)
                    else:
                        return []
                ht[x] = i
        return res

    def bsearch(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        # to find number that >= target
        return left


s = Solution()

a = [1, 2, 3, 4]
print(s.avoidFlood(a))

a = [1, 2, 0, 0, 2, 1]
print(s.avoidFlood(a))

a = [1, 2, 0, 1, 2]
print(s.avoidFlood(a))

a = [69, 0, 0, 0, 69]
print(s.avoidFlood(a))

a = [10, 20, 20]
print(s.avoidFlood(a))

a = [1, 0, 2, 0]
print(s.avoidFlood(a))

a = [1, 2, 0, 2, 3, 0, 1]
print(s.avoidFlood(a))

a = [1, 0, 2, 3, 0, 1, 2]
print(s.avoidFlood(a))

a = [3, 5, 4, 0, 1, 0, 1, 5, 2, 8, 9]
print(s.avoidFlood(a))

a = [0, 1, 1]
print(s.avoidFlood(a))

a = [97, 0, 98, 99, 0, 97, 98]
print(s.avoidFlood(a))

"""
[-1, -1, -1, -1]
[-1, -1, 2, 1, -1, -1]
[]
[-1, 69, 1, 1, -1]
[]
[-1, 1, -1, 1]
[-1, -1, 2, -1, -1, 1, -1]
[-1, 1, -1, -1, 2, -1, -1]
[-1, -1, -1, 5, -1, 1, -1, -1, -1, -1, -1]
[]
[-1, 97, -1, -1, 98, -1, -1]
"""
