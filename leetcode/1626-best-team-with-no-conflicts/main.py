"""
    1st: dynamic programming (recursion + hashtable)
    - group the input as a list of objects, sort the objects in a reverse order to ensure that the older players are in the front
    e.g. scores = [4,5,6,5], ages = [2,1,2,1]
    players [(2, 6), (2, 4), (1, 5), (1, 5)]
    - then we do recursion to select the same age/young players who have the score <= player[i] has
    - we can cache the result by doing the recursion from the bottom

    Time    O(NlogN + N^2) for every (index, limit) pair, it is visited once
    Space   O(N^2)
    3544 ms, faster than 9.52%
"""
class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        n = len(scores)
        players = []
        for i in range(n):
            players.append((ages[i], scores[i]))
        players.sort(reverse=True)
        return self.dfs(players, 0, sys.maxsize, {})
        
    def dfs(self, players, start, limit, ht):
        if start == len(players):
            return 0
        key = (start, limit)
        if key in ht:
            return ht[key]
        maxScore = 0
        for i in range(start, len(players)):
            age, score = players[i]
            if score <= limit:
                temp = self.dfs(players, i+1, score, ht) + score
                maxScore = max(maxScore, temp)
        ht[key] = maxScore
        return ht[key]
    

"""
    2nd: dynamic programming (2D array)
    - longest increasing subsequence

    Time    O(NlogN + N^2)
    Space   O(N)
    1408 ms, faster than 82.14%
"""
class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        n = len(scores)
        players = []
        for i in range(n):
            players.append((ages[i], scores[i]))
        players.sort()
        
        maxScores = n * [0]
        for i in range(n):
            age, score = players[i]
            maxScore = 0
            for j in range(i):
                if players[j][1] <= score:
                        maxScore = max(maxScore, maxScores[j])
            maxScores[i] = maxScore + score
        return max(maxScores)
        
        