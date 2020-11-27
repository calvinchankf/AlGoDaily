"""
    1st: BFS + hashtable
    - for every point, there are 2 possibilities, forward and backward, we put them in a hashset to avoid redundant calculations

    Time    O(2N)
    Space   O(2N)
    116 ms, faster than 100.00%
"""


class Solution(object):
    def minimumJumps(self, forbidden, a, b, x):
        """
        :type forbidden: List[int]
        :type a: int
        :type b: int
        :type x: int
        :rtype: int
        """
        forbiddenSet = set(forbidden)
        seen = set()
        q = [(0, 0, False)]
        while len(q) > 0:
            node, steps, isPrevBack = q.pop(0)
            if node == x:
                return steps
            if node in forbiddenSet:
                continue
            key = (node, isPrevBack)
            if key in seen:
                continue
            seen.add(key)
            if node + a <= 6000:  # 2000 + a + b <= 6000
                q.append((node + a, steps + 1, False))
            if node - b >= 0 and isPrevBack == False:
                q.append((node - b, steps + 1, True))
        return -1


s = Solution()

a = [14, 4, 18, 1, 15]
b = 3
c = 15
d = 9
print(s.minimumJumps(a, b, c, d))

a = [8, 3, 16, 6, 12, 20]
b = 15
c = 13
d = 11
print(s.minimumJumps(a, b, c, d))

a = [1, 6, 2, 14, 5, 17, 4]
b = 16
c = 9
d = 7
print(s.minimumJumps(a, b, c, d))

a = [162, 118, 178, 152, 167, 100, 40, 74, 199, 186, 26, 73, 200, 127, 30, 124, 193, 84, 184, 36, 103, 149, 153, 9, 54, 154,
     133, 95, 45, 198, 79, 157, 64, 122, 59, 71, 48, 177, 82, 35, 14, 176, 16, 108, 111, 6, 168, 31, 134, 164, 136, 72, 98]
b = 29
c = 98
d = 80
print(s.minimumJumps(a, b, c, d))
