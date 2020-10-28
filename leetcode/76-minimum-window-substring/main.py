import sys
"""
    Questions to ask:
    - lower/upper case?
    - duplicate characters in t?
    - any space?
"""

"""
    1st approach: hashtable
    - move forward the fast pointer until the window contains "satisfies" the target
    - if the window satisfies the target, keep moving the slow pointer to find the minimum window

    e.g. string = azjskfzs, target = az

    first satisfying window
    azjskfzs
    L  R

    move slow(left) pointer to find the minimum
    azjskfzs
     L R

    now the window can not satisfy the target, gonna move the fast(right) poiner next
    azjskfzs
      LR
    
    nice, we see a satisfying window but its length is larger than the intermediate result
    azjskfzs
      L   R
    
    another satisfying window but its length is larger than the intermediate result
    azjskfzs
       L  R
    
    cannot satisfy, move fast pointer next
    azjskfzs
        L R
    
    satisfy now, move the slow pointer next
    azjskfzs
        L  R

    great, this window is satisfying and with shorter length than the intermediate result
    azjskfzs
          LR

    ref:
    - https://www.youtube.com/watch?v=eS6PZLjoaq8

    Time    O(N^2 x 128) at most 128 characters in hashtable if we consider ascii code only
    Space   O(N)
    644 ms, faster than 6.97%
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n = len(s)
        targetHt = Counter(t)
        ht = Counter()
        j = 0
        res = None
        for i in range(n):
            c = s[i]
            ht[c] += 1
            while self.containTarget(ht, targetHt):
                if res == None or i - j + 1 < len(res):
                    res = s[j:i+1]
                last = s[j]
                ht[last] -= 1
                j += 1
        
        if res == None:
            return ''
        return res
    
    def containTarget(self, ht, target):
        for key in target:
            if key not in ht:
                return False
            if ht[key] < target[key]:
                return False
        return True


# print(Solution().checkSameStructure([0, 1, 2], [0, 1, 2]))
print(Solution().minWindow("ABC", "ABC"))
print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("ADOBECODEBANC", "ABCB"))
print(Solution().minWindow("ADOBECODEBANCBABB", "ABC"))
print(Solution().minWindow("ADOBBECCOBDEBANC", "ABC"))

print("-----")

from collections import Counter

"""
    same as 1st approach but use indices
    , so we dont use string slice which we can optimize the time complexity

    Time    O(N x 128) at most 128 characters in hashtable if we consider ascii code only
    Space   O(N)
    644 ms, faster than 6.97%
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        targetHt = Counter(t)
        ht = Counter()
        j = 0
        L, R = 0, n+1
        for i in range(n):
            c = s[i]
            ht[c] += 1
            while self.containTarget(ht, targetHt):
                if i - j + 1 < R - L + 1:
                    L = j
                    R = i + 1
                last = s[j]
                ht[last] -= 1
                j += 1
        
        if R == n+1:
            return ''
        return s[L:R]
    
    def containTarget(self, ht, target):
        for key in target:
            if key not in ht:
                return False
            if ht[key] < target[key]:
                return False
        return True