from collections import Counter
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

    Time    O(128N) at most 128 characters in hashtable if we consider ascii code only
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


"""
    2nd: hashtable + counting trick

    e.g. string = azjskfzs, target = az

    counter of az = { a: 1, z: 1 }

    azjskfzs
    ^
       ^
    azjs containts az, counter = {
        a: -1,
        z: 0,
        j: -1,
        s: 0
    }

    then we move the left pointer until the counter doesnt satisfy our target

    1.
    azjskfzs
     ^
       ^
    azjs containts az, counter = {
        z: 0,
        j: -1,
        s: 0
    }

    2.
    azjskfzs
      ^
       ^
    azjs containts az, counter = {
        z: 1,
        j: -1,
        s: 0
    }

    Now we move our faster pointer until counter satisfy our target
    azjskfzs
      ^
          ^
    azjs containts az, counter = {
        z: 0,
        s: 0,
        j: -1,
        k: -1,
        f: -1,
    }

    So now, we move our left pointer again to see if we can find out a shorter substring satasify our target
    azjskfzs
        ^
          ^
    azjs containts az, counter = {
        z: 0,
        s: 1,
        k: -1,
        f: -1,
    }

    Now, lets move the fast pointer again
    azjskfzs
        ^
           ^
    azjs containts az, counter = {
        z: 0,
        s: 0,
        k: -1,
        f: -1,
    }

    Then left pointer,
    azjskfzs
          ^
           ^
    azjs containts az, counter = {
        z: 0,
        s: 0,
    }

    At the end, the last two characters is the shortest substring that contains our target !!!

    Time    O(N)
    Space   O(N)
    128 ms, faster than 41.28%
"""


class Solution(object):
    def minWindow(self, s, t):
        ht = Counter(t)
        j = 0
        count = 0
        res = ''
        for i in range(len(s)):
            c = s[i]
            if ht[c] > 0:
                count += 1
            ht[c] -= 1
            while count == len(t):
                if res == '' or i-j+1 < len(res):
                    res = s[j:i+1]
                left = s[j]
                j += 1
                ht[left] += 1
                if ht[left] > 0:
                    count -= 1
        return res
