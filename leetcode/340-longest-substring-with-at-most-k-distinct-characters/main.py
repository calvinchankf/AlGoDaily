"""
    1st approach: hashtable + sliding window
    - similar to lc3, 159, 904
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
        res = 0
        left = 0
        ht = {}
        for i in range(len(s)):
            # put the character into the hastable counter
            c = s[i]
            if c not in ht:
                ht[c] = 1
            else:
                ht[c] += 1

            # if the total number of keys of hashtable > k, we
            while len(ht) > k:
                last = s[left]
                ht[last] -= 1
                # dont forget to remove the keys from hashtable if no more count on it
                if ht[last] == 0:
                    del ht[last]
                # move the left pointer to the right by 1 unit
                left += 1
            # update the result if the number of keys is <= k
            res = max(res, i-left+1)

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
