"""
    1st approach: binary search + sliding window
    - let's say the length of a string is 10, we can try to see if there are any duplicate substrings of length 5
    - if yes, we are going to see if there are any duplicate substrings of length (10+5+1)//2 = 8
    - if no, we are going to see if there are any duplicate substrings of length (0+5+1)//2 = 3

    Time    O(nlogn)
    Space   O(n^2)
    10 / 16 test cases passed. Memory Limit Exceeded(MLE)
"""


class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = ""
        left, right = 0, len(S)
        while left < right:
            mid = (left + right + 1)//2
            sub = self.findDupOflength(S, mid)
            if len(sub) > 0:
                left = mid
                res = sub
            else:
                right = mid - 1
        return res

    def findDupOflength(self, S, k):
        window = ""
        seen = set()
        for i in range(len(S)):
            if i >= k:
                window = window[1:]
            window += S[i]
            if len(window) == k:
                if window not in seen:
                    seen.add(window)
                else:
                    return window
        return ""


"""
    2nd approach: binary search + sliding window with Rabin-Karp Rolling Hash
    - same idea as 1st approach, use rolling hash to reduce string storage
    
    rolling hash:
    e.g. banana
    [b,a,n,a,n,a] -> [1, 0, 13, 0, 13, 0]
    
    consider k = 3, from the begining, ban, ana, nan....etc

    step1: ban
                                b    a     n      
    ban => 26 * (26 * (26 * 0 + 1) + 0) + 13 = 689

    step2: ana 
    ana => ban - b + a => 
          ban  -          b + a
    (26 * 689) - 26*26*26*1 + 0 = 338

    step3: nan
    ...


    - just need to understand the rolling hash function, dont need to remember it

    ref:
    - https://leetcode.com/problems/longest-duplicate-substring/discuss/327643/Step-by-step-to-understand-the-binary-search-solution
    - https://leetcode.com/problems/longest-duplicate-substring/discuss/290871/Python-Binary-Search


    Time    O(nlogn)
    Space   O(n)
    1952 ms, faster than 40.53%
"""


class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = ""
        left, right = 0, len(S)
        while left < right:
            mid = (left + right + 1)//2
            sub = self.findDupOflength(S, mid)
            if len(sub) > 0:
                left = mid
                res = sub
            else:
                right = mid - 1
        return res

    def findDupOflength(self, S, k):
        modulus = 2**63-1
        nums = [ord(c) - ord('a') for c in S]
        # compute the hash of string S[:L]
        rollingHash = 0
        for i in range(k):
            rollingHash = (rollingHash * 26 + nums[i]) % modulus
        seen = set([rollingHash])
        # const value to be used often : a**L % modulus
        p = pow(26, k, modulus)
        for i in range(k, len(S)):
            # compute rolling hash in O(1) time
            rollingHash = (rollingHash * 26 +
                           nums[i] - nums[i - k] * p) % modulus
            if rollingHash in seen:
                start = i - k + 1
                return S[start: start + k]
            seen.add(rollingHash)
        return ""
