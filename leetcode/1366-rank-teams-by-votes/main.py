"""
    idea: sort by the frequencies of rank for each team, order by lexico

    e.g.1
    ["ABC","ACB","ABC","ACB","ACB"]

    ranks = {
        #   1  2  3 <- ranking
        #   -------
        A: [5, 0, 0],
        B: [0, 2, 3],
        C: [0, 3, 2]
    }

    A appears 5 times as rank1, so it is ranked #1
    C appears 3 times as rank2 whereas B appears 2 times as rank2

    e.g.2
    ["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"]

    ranks = {
        A: [2, 2, 2], 
        B: [2, 2, 2],
        C: [2, 2, 2]
    }
    All appear twice, so rank them by IDs lexicographically
"""


class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        teamsCount = len(votes[0])
        ranks = {}
        for v in votes:
            for i in range(len(v)):
                team = v[i]
                if team not in ranks:
                    ranks[team] = teamsCount * [0]
                ranks[team][i] += 1

        keys = ranks.keys()

        def cmptr(a, b):
            A = ranks[a]
            B = ranks[b]
            for i in range(teamsCount):
                if A[i] != B[i]:
                    return B[i] - A[i]  # descending
            if a < b:  # lexico
                return -1
            return 1
        keys.sort(cmp=cmptr)

        return ''.join(keys)


s = Solution()

a = ["ABC", "ACB", "ABC", "ACB", "ACB"]
print(s.rankTeams(a))

a = ["WXYZ", "XYZW"]
print(s.rankTeams(a))

a = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
print(s.rankTeams(a))

a = ["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"]
print(s.rankTeams(a))

a = ["M", "M", "M", "M"]
print(s.rankTeams(a))
