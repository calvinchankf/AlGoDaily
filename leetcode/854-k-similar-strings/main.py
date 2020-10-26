"""
    1st: brute force

    9 / 54 test cases passed.
    LTE
"""


class Solution(object):
    def kSimilarity(self, A, B):
        n = len(A)
        ht = {}
        ht[A] = True
        q = [(A, 0)]
        while len(q) > 0:
            s, steps = q.pop(0)
            if s == B:
                return steps
            for i in range(n):
                for j in range(i+1, n):
                    temp = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                    if temp in ht:
                        continue
                    ht[temp] = True
                    q.append((temp, steps+1))
        return -1


s = Solution()

a = "ab"
b = "ba"
print(s.kSimilarity(a, b))

a = "abc"
b = "bca"
print(s.kSimilarity(a, b))

a = "abac"
b = "baca"
print(s.kSimilarity(a, b))

a = "aabc"
b = "abca"
print(s.kSimilarity(a, b))

a = "aab"
b = "baa"
print(s.kSimilarity(a, b))

a = "calvin"
b = "vlcnai"
print(s.kSimilarity(a, b))

# a = "calvinchan"
# b = "vlcnaichan"
# print(s.kSimilarity(a, b))

# a = "abccaacceecdeea"
# b = "bcaacceeccdeaae"
# print(s.kSimilarity(a, b))

print("----")


"""
    2nd: optimized BFS
    - similar to lc854
    - in BFS, we dont need to generate all permuation of swap(i,j) in every step
    - we can instead target the leftmost character one by one to makes S more simliar to target string B
        so that we can reduce the time complexity

    Time    must be less than O(2^N) because we are reducing the diffence one character by one character
    Space   O(N)
    524 ms, faster than 35.91%
"""


class Solution(object):
    def kSimilarity(self, A, B):
        ht = {}
        ht[A] = True
        q = [(A, 0)]
        while len(q) > 0:
            s, steps = q.pop(0)  # s: temporary string along the way we do BFS
            if s == B:
                return steps
            for cand in self.getCandidates(s, B):
                if cand in ht:
                    continue
                ht[cand] = True
                q.append((cand, steps+1))
        return -1

    def getCandidates(self, s, B):
        # ignore the common prefix
        i = 0
        candidates = []
        while s[i] == B[i]:
            i += 1
        # starting from S[i+1] (because S and B have the common prefix from index 0 to i)
        # for every charactor of S[j] which matches B[i], swap the charactors at i and j in S
        # so that we are making S more simliar to target string B by one character(the leftmost character)
        for j in range(i+1, len(s)):
            if s[j] == B[i]:
                temp = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                candidates.append(temp)
        return candidates


s = Solution()

a = "ab"
b = "ba"
print(s.kSimilarity(a, b))

a = "abc"
b = "bca"
print(s.kSimilarity(a, b))

a = "abac"
b = "baca"
print(s.kSimilarity(a, b))

a = "aabc"
b = "abca"
print(s.kSimilarity(a, b))

a = "aab"
b = "baa"
print(s.kSimilarity(a, b))

a = "calvin"
b = "vlcnai"
print(s.kSimilarity(a, b))

a = "calvinchan"
b = "vlcnaichan"
print(s.kSimilarity(a, b))

a = "abccaacceecdeea"
b = "bcaacceeccdeaae"
print(s.kSimilarity(a, b))
