from collections import Counter

"""
    1st approach: hashtable + sliding window
    - similar to lc3, 159, 340, 904
    - in each iteration
        1. put the character into the hastable counter
        2. if the number of keys > k, remove the leftmost character in the window as well as increment its count
        3. update the result if the number of keys is <= k

    Time    O(2n) worst case: aaaaaaaaaabc, k=2
    Space   O(n)
    68 ms, faster than 59.78% 
"""


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        j = 0
        ht = Counter()
        res = 0
        for i in range(len(s)):
            cur = s[i]
            ht[cur] += 1
            while len(ht) > k:
                left = s[j]
                j += 1
                ht[left] -= 1
                if ht[left] == 0:
                    del ht[left]
            res = max(res, i-j+1)
        return res


a = "eceba"
b = 2
print(Solution().lengthOfLongestSubstringKDistinct(a, b))

a = "aa"
b = 1
print(Solution().lengthOfLongestSubstringKDistinct(a, b))

a = "a"
b = 1
print(Solution().lengthOfLongestSubstringKDistinct(a, b))

a = "a@b$5!a8alskj234jasdf*()@$&%&#FJAvjjdaurNNMa8ASDF-0321jf?>{}L:fh"
b = 10
print(Solution().lengthOfLongestSubstringKDistinct(a, b))
