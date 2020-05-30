"""
    1st: sort
    - convert the strings to numbers and sort the numbers
    - see if either one of them can break another string

    e.g.1
    s1 = "abc" , s2 = "xya"
    a1 = [0, 1, 2]
          |  ^  ^
    a2 = [0,24,25]
    from the above, a2 > a1, therefore s2 can break s1

    e.g.2
    s1 = "abe" , s2 = "acd"
    a1 = [0, 1, 4]
          |  ^  v
    a2 = [0, 2, 3]
    from the above, neither one of them can break one another

    Time    O(NlogN)
    Space   O(N)
    516 ms, faster than 25.00%
"""


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        n = len(s1)
        arr1, arr2 = [], []
        for i in range(n):
            arr1.append(ord(s1[i]) - ord('a'))
            arr2.append(ord(s2[i]) - ord('a'))
        arr1.sort()
        arr2.sort()
        aLarger, bLarger = True, True
        for i in range(n):
            if arr1[i] < arr2[i]:
                aLarger = False
            elif arr1[i] > arr2[i]:
                bLarger = False
        return aLarger or bLarger


"""
    2nd: hashtable
    - check if count of all characters in s1 is >= s2

    Time    O(N)
    Space   O(N)
    68 ms, faster than 100.00%
"""


class Solution:
    def checkIfFormerLarger(self, d1, d2):
        diff = 0
        for c in 'abcdefghijklmnopqrstuvwxyz':
            diff += d1[c] - d2[c]
            if diff < 0:
                return False
        return True

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        ht1 = collections.Counter(s1)
        ht2 = collections.Counter(s2)
        return self.checkIfFormerLarger(ht1, ht2) | self.checkIfFormerLarger(ht2, ht1)
