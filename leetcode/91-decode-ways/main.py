class Solution(object):

    def __init__(self):
        self.res = []

    def numDecodings(self, s):
        """
        1st approach: brute force
        1. go through all the paths
        2. for each path, when it comes to an end, put the history into an array
        3. the length of the array is the result

        Time Limit Exceeded
        """
        self.helper(s, "")
        return len(self.res)

    def helper(self, s, history):
        if len(s) == 0:
            self.res.append(history)
            return
        a = int(s[0])
        if a > 0:
            self.helper(s[1:], history+s[0]+",")
        b = int(s[:2])
        if a > 0 and b > 9 and b < 27:
            self.helper(s[2:], history+s[:2]+",")


print(Solution().numDecodings("0"))
print(Solution().numDecodings("10"))
print(Solution().numDecodings("12"))
print(Solution().numDecodings("102"))
print(Solution().numDecodings("226"))
print(Solution().numDecodings("1212"))
# print(Solution().numDecodings("9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"))
print("-----")


class Solution(object):

    def __init__(self):
        self.seen = {}

    def numDecodings(self, s):
        """
        2nd approach: brute force with memorization
        1. go through all the paths
        2. for each path, when it comes to an end return 1
        3. memorize the substrings and their "ways" to avoid duplicate calculations
        3. the result is the sum of recursion

        Time    O(n) the length of the string, we use map to avoid duplicate substring
        Space   O(h) the height of recursion
        36 ms, faster than 26.40%
        """
        if s in self.seen:
            return self.seen[s]
        if len(s) == 0:
            return 1
        left = 0
        right = 0
        a = int(s[0])
        if a > 0:
            left = self.numDecodings(s[1:])
        b = int(s[:2])
        if a > 0 and b > 9 and b < 27:
            right = self.numDecodings(s[2:])
        self.seen[s] = left + right
        return left + right


print(Solution().numDecodings("0"))
print(Solution().numDecodings("10"))
print(Solution().numDecodings("12"))
print(Solution().numDecodings("102"))
print(Solution().numDecodings("226"))
print(Solution().numDecodings("1212"))
print(Solution().numDecodings(
    "9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"))
print("-----")


class Solution(object):

    def __init__(self):
        self.seen = {}

    def numDecodings(self, s):
        """
        2nd approach: brute force with memorization
        1. go through all the paths
        2. for each path, when it comes to an end return 1
        3. memorize the substrings and their "ways" to avoid duplicate calculations
        3. the result is the sum of recursion

        Time    O(n) the length of the string, we use map to avoid duplicate substring
        Space   O(h) the height of recursion
        36 ms, faster than 26.40%
        """
        if s in self.seen:
            return self.seen[s]
        if len(s) == 0:
            return 1
        total = 0
        a = int(s[0])
        if a > 0:
            total += self.numDecodings(s[1:])
        b = int(s[:2])
        if a > 0 and b > 9 and b < 27:
            total += self.numDecodings(s[2:])
        self.seen[s] = total
        return total


print(Solution().numDecodings("0"))
print(Solution().numDecodings("10"))
print(Solution().numDecodings("12"))
print(Solution().numDecodings("102"))
print(Solution().numDecodings("226"))
print(Solution().numDecodings("1212"))
print(Solution().numDecodings(
    "9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"))
print("-----")


class Solution:
    def numDecodings(self, s: str) -> int:
        return self.f(s, 0, {})

    def f(self, s, fromIdx, ht):
        if fromIdx == len(s):
            return 1
        if fromIdx + 1 == len(s):
            if int(s[fromIdx]) == 0:
                return 0
            return 1
        else:
            if fromIdx in ht:
                return ht[fromIdx]

            a = s[fromIdx]
            b = s[fromIdx+1]
            c = int(a + b)

            if int(a) == 0:
                return 0

            ways1, ways2 = 0, 0

            if c <= 26:
                ways1 = self.f(s, fromIdx + 1, ht)
                ways2 = self.f(s, fromIdx + 2, ht)
            else:
                ways1 = self.f(s, fromIdx + 1, ht)

            ht[fromIdx] = ways1 + ways2
            return ht[fromIdx]


print(Solution().numDecodings("0"))
print(Solution().numDecodings("10"))
print(Solution().numDecodings("12"))
print(Solution().numDecodings("102"))
print(Solution().numDecodings("226"))
print(Solution().numDecodings("1212"))
print(Solution().numDecodings(
    "9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"))
print("-----")
