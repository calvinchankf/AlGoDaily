"""
  questions to ask:
  - will word1 == word2?
  - will either word1, word2 be in the list always? 
"""

"""
    naive solution: brute force O(n^2)
"""


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int

        1st approach: 2pointers

        Time    O(n)
        Space   O(n)
        52 ms, faster than 27.57%
        """
        p1 = -1
        p2 = -1
        res = len(words)
        for i in range(len(words)):
            word = words[i]
            if word == word1:
                p1 = i
            if word == word2:
                p2 = i
            if p1 != -1 and p2 != -1:
                res = min(res, abs(p1-p2))
        return res


a = ["practice", "makes", "perfect", "coding", "makes"]
b = "makes"
c = "coding"
print(Solution().shortestDistance(a, b, c))

print("-----")


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        1st approach: binary search the nearest target index

        Time    O(mlogn) m: word1, n: word2
        Space   O(m+n)
        12 ms, faster than 7.14%
        """
        A, B = [], []
        for i in range(len(words)):
            w = words[i]
            if w == word1:
                A.append(i)
            elif w == word2:
                B.append(i)
        res = 2**32
        for x in A:
            j = self.bsearch(B, x)
            y = B[j]
            res = min(res, abs(x-y))
        return res

    def bsearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        if right < 0:
            return 0
        if left > len(nums)-1:
            return len(nums)-1
        if abs(nums[left] - target) < abs(nums[right] - target):
            return left
        return right
