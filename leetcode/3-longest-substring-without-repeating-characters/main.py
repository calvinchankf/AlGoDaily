from collections import Counter
"""
    2nd approach: sliding window + hashtable
    - similar to lc3, 159, 340, 904
	- in each iteration, if we meet a 2-occurence character
        - we move the slow pointer to the left
        - and increment the count of the character on the index where slow pointer points to
        - continue to move the slow pointer until the current character's count becomes 1

	Time	O(2n)
	Space	O(n)
    60 ms, faster than 52.92%
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        j = 0
        ht = Counter()
        res = 0
        for i in range(len(s)):
            cur = s[i]
            ht[cur] += 1
            while ht[cur] > 1:
                left = s[j]
                j += 1
                ht[left] -= 1
                if ht[left] == 0:
                    del ht[left]
            res = max(res, i - j + 1)
        return res


a = "abcabcbb"
print(Solution().lengthOfLongestSubstring(a))

a = "bbbbb"
print(Solution().lengthOfLongestSubstring(a))

a = "pwwkew"
print(Solution().lengthOfLongestSubstring(a))

a = "abcdef"
print(Solution().lengthOfLongestSubstring(a))

a = "abcbdef"
print(Solution().lengthOfLongestSubstring(a))

a = "abcbdee"
print(Solution().lengthOfLongestSubstring(a))

a = "abb"
print(Solution().lengthOfLongestSubstring(a))

a = "ab"
print(Solution().lengthOfLongestSubstring(a))

a = "a"
print(Solution().lengthOfLongestSubstring(a))

print("-----")

"""
    followup: print that substring

    Time	O(2n)
	Space	O(n)
    64 ms, faster than 46.35%
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ht = {}
        slow = 0
        res = ""
        for i in range(len(s)):
            c = s[i]
            # count with hashtable
            if c not in ht:
                ht[c] = 1
            else:
                ht[c] += 1
            # remove the character from the left if count > 1
            while ht[c] > 1:
                last = s[slow]
                ht[last] -= 1
                if ht[last] == 0:
                    del ht[last]
                slow += 1
            # update the result if necessary
            temp = s[slow:i+1]
            if len(temp) > len(res):
                res = temp
        return res


a = "abcabcbb"
print(Solution().lengthOfLongestSubstring(a))

a = "bbbbb"
print(Solution().lengthOfLongestSubstring(a))

a = "pwwkew"
print(Solution().lengthOfLongestSubstring(a))

a = "abcdef"
print(Solution().lengthOfLongestSubstring(a))

a = "abcbdef"
print(Solution().lengthOfLongestSubstring(a))

a = "abcbdee"
print(Solution().lengthOfLongestSubstring(a))

a = "abb"
print(Solution().lengthOfLongestSubstring(a))

a = "ab"
print(Solution().lengthOfLongestSubstring(a))

a = "a"
print(Solution().lengthOfLongestSubstring(a))
