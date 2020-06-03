"""
    1st: sort
    - pop the minimum tokens to get score
    - pop the maximum tokens to get power
    - since tokens can be used once, we must pass through the max score along the way

    Buy the cheapests and sell the most expensives

    Time    O(NlogN)
    Space   O(N)
    52 ms, faster than 81.25% 
"""


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        res = 0
        score = 0
        arr = sorted(tokens)
        while len(arr) > 0:
            if arr[0] <= P:
                score += 1
                P -= arr.pop(0)
            else:
                score -= 1
                P += arr.pop()
            res = max(res, score)
        return res
