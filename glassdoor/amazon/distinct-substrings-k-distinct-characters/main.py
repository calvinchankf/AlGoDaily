from collections import Counter

"""
    https://leetcode.com/discuss/interview-question/370112

    Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

    --------------------------------------------------------------------------------
    Example 1:

    Input: s = "abcabc", k = 3
    Output: ["abc", "bca", "cab"]
    --------------------------------------------------------------------------------
    Example 2:

    Input: s = "abacab", k = 3
    Output: ["bac", "cab"]
    --------------------------------------------------------------------------------
    Example 3:

    Input: s = "awaglknagawunagwkwagl", k = 4
    Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
    Explanation: 
    Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl" 
    "wagl" is repeated twice, but is included in the output once.
    --------------------------------------------------------------------------------
    
    Constraints:
    - The input string consists of only lowercase English letters [a-z]
    - 0 <= k <= 26
"""


class Solution(object):
    def distinctSubstrings(self, s, k):
        res = set()
        window = Counter()
        for i in range(len(s)):
            c = s[i]
            window[c] += 1

            if i >= k:
                left = s[i-k]
                window[left] -= 1
                if window[left] == 0:
                    del window[left]

            if len(window) == k:
                sub = s[i-k+1: i+1]
                res.add(sub)
        return res


s = Solution()

a = "abcabc"
b = 3
print(s.distinctSubstrings(a, b))

a = "abacab"
b = 3
print(s.distinctSubstrings(a, b))

a = "awaglknagawunagwkwagl"
b = 4
print(s.distinctSubstrings(a, b))

print("-----")


class Solution(object):
    def distinctSubstrings(self, s, k):
        """
            variation:
            https://www.geeksforgeeks.org/count-number-of-substrings-with-exactly-k-distinct-characters/

            1. find all the substrings and check if each of them has only k distinct charactors using a hashtable
            2. use a set to avoid duplicate substrings

            Time    O(n^2)
            Space   O(n)
        """
        res = set()
        for i in range(len(s)):
            distinct_count = 0
            m = {}
            for j in range(i, len(s)):
                c = s[j]
                if c not in m:
                    m[c] = 1
                    distinct_count += 1
                else:
                    m[c] += 1
                if distinct_count == k:  # i am not sure if dict.keys() is O(n)
                    res.add(s[i: j+1])

        return res, len(res)


print(Solution().distinctSubstrings('abc', 2))
print(Solution().distinctSubstrings('aba', 2))
print(Solution().distinctSubstrings('aa', 1))
print(Solution().distinctSubstrings('abcdabc', 3))
print(Solution().distinctSubstrings('abcbaa', 3))
