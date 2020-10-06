import sys
"""
    Questions to ask:
    - lower/upper case?
    - duplicate characters in t?
    - any space?
"""

"""
    Time    O(nk)
    Space   O(n)
    456 ms beats 6.27%
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        indexes = []
        minimum = s
        targetStructure = {}
        for c in t:
            if c in targetStructure:
                targetStructure[c] += 1
            else:
                targetStructure[c] = 1
        curStructure = {}
        for key in targetStructure:
            curStructure[key] = 0

        for i in range(len(s)):
            c = s[i]
            if c in targetStructure:
                indexes.append(i)
                curStructure[c] += 1
                # check recursively
                while self.checkSameStructure(targetStructure, curStructure):
                    end = indexes[-1]
                    start = indexes[0]
                    length = end-start+1
                    if length < len(minimum):
                        minimum = s[start:end+1]
                    popped = indexes.pop(0)
                    curStructure[s[popped]] -= 1
        if len(minimum) == len(s):
            cur = {}
            for key in targetStructure:
                cur[key] = 0
            for i in range(len(s)):
                c = s[i]
                if c in targetStructure:
                    cur[c] += 1
            if self.checkSameStructure(targetStructure, cur):
                return s
            else:
                return ""
        return minimum

    def checkSameStructure(self, a, b):
        for key in a:
            if key not in b:
                return False
            elif a[key] > b[key]:
                return False
        return True


print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("ADOBECODEBANC", "ABCB"))
print(Solution().minWindow("ADOBECODEBANCBABB", "ABC"))
print(Solution().minWindow("ADOBBECCOBDEBANC", "ABC"))
print(Solution().minWindow("ADOBECODEBANC", "ABc"))

print("-----")

"""
    2nd approach: hashtable
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

    Time    O(128n) 128 ascii-characters
    Space   O(n)
    1516 ms, faster than 5.06%
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        targetHt = self.constructHt(t)

        res = s
        curHt = {}
        cur = ''
        j = 0
        for i in range(len(s)):
            c = s[i]
            cur += c

            if c in curHt:
                curHt[c] += 1
            else:
                curHt[c] = 1

            while self.ifAContainB(curHt, targetHt):

                if len(cur) < len(res):
                    res = cur

                last = s[j]
                j += 1

                cur = cur[1:]
                curHt[last] -= 1
                if curHt[last] == 0:
                    del curHt[last]

        if self.ifAContainB(self.constructHt(res), targetHt):
            return res
        return ""

    def constructHt(self, s):
        ht = {}
        for c in s:
            if c in ht:
                ht[c] += 1
            else:
                ht[c] = 1
        return ht

    def ifAContainB(self, a, b):
        for key in b:
            if key not in a:
                return False
            if a[key] < b[key]:
                return False
        return True


# print(Solution().checkSameStructure([0, 1, 2], [0, 1, 2]))
print(Solution().minWindow("ABC", "ABC"))
print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("ADOBECODEBANC", "ABCB"))
print(Solution().minWindow("ADOBECODEBANCBABB", "ABC"))
print(Solution().minWindow("ADOBBECCOBDEBANC", "ABC"))
