"""
    1st approach: permutation

    Time    O(4!)
    Space   O(4!)
    28 ms, faster than 30.08%
"""


class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        self.times = []
        self.permute(A, "")
        res = None
        for time in self.times:
            hour = time[:2]
            minute = time[2:]
            if int(hour) < 24 and int(minute) < 60:
                if res == None or hour+minute > res:
                    res = hour+minute
        if res == None:
            return ""
        return res[:2] + ':' + res[2:]

    def permute(self, cands, chosen):
        if len(cands) == 0:
            self.times.append(chosen)
        for i in range(len(cands)):
            cand = cands[i]
            self.permute(cands[:i]+cands[i+1:], chosen+str(cand))


"""
    2nd: try all timeslots

    Time    O(24*60*60) = (86,400)
    Space   O(1)
    200 ms, faster than 5.04%
"""


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ht = 10 * [0]
        for a in A:
            ht[a] += 1

        for i in range(23, -1, -1):
            for j in range(59, -1, -1):
                temp = 10 * [0]
                temp[i//10] += 1
                temp[i % 10] += 1
                temp[j//10] += 1
                temp[j % 10] += 1

                allMatch = True
                for k in range(10):
                    if temp[k] != ht[k]:
                        allMatch = False
                if allMatch:
                    return "%02d:%02d" % (i, j)

        return ''
