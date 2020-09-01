"""
    1st approach: recursion
    - lets say we have num = 3, the combinations are (0,3), (1,2), (2,1), (3,0), the form is (k, num-k)
    - we need to explore all the possibilities of binary represenation with k digit by using recusion
        e.g. k=2
        possibilities = [[1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 0, 1], [0, 0, 1, 1]]
    - after we explore the hours combo and minutes combo, stringify and combine them all together
    
    Time    O(n2^n) -> O(12*60) each digit has 2 options(stay at 0 or change to 1), iteration to explore possibilities in each recursion
    Space   O(2^n) the depth of recursion tree
    20 ms, faster than 83.69%
"""


class Solution(object):
    def readBinaryWatch(self, num):
        res = []
        for k in range(num+1):
            combos = self.explore(k, num-k)
            res += combos
        return res

    def explore(self, a, b):

        hours = []
        minutes = []

        def exploreHours(k, cands, fromIdx):
            if k == 0:
                h = self.transformBinary2Int(cands)
                if h < 12:
                    hours.append(str(h))
            else:
                for i in range(fromIdx, len(cands)):
                    if cands[i] == 0:
                        clone = cands[:]
                        clone[i] = 1
                        exploreHours(k-1, clone, i+1)

        def exploreMinutes(k, cands, fromIdx):
            if k == 0:
                m = self.transformBinary2Int(cands)
                if m < 60:
                    minutes.append(str(m) if m > 9 else '0'+str(m))
            else:
                for i in range(fromIdx, len(cands)):
                    if cands[i] == 0:
                        clone = cands[:]
                        clone[i] = 1
                        exploreMinutes(k-1, clone, i+1)

        exploreHours(a, [0, 0, 0, 0], 0)
        exploreMinutes(b, [0, 0, 0, 0, 0, 0], 0)

        combos = []
        for h in hours:
            for m in minutes:
                combos.append(h+':'+m)
        return combos

    def transformBinary2Int(self, arr):
        num = 0
        for i in range(len(arr)):
            num += arr[i] * (2**i)
        return num


s = Solution()
print(s.readBinaryWatch(1))
print(s.readBinaryWatch(2))

print("-----")

"""
    2nd: think in another way
    - there there 23:59 possibilities, 
        if a binary representation of a timeslot in which the total number of '1' from hour and minute == num, then this is on of the result
"""


class Solution(object):
    def readBinaryWatch(self, num):
        res = []
        for h in range(12):
            for m in range(60):
                b = bin(h) + bin(m)
                if b.count('1') == num:
                    res.append('%d:%02d' % (h, m))
        return res
