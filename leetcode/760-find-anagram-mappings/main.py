from collections import defaultdict

"""
    1st: hashtable

	Time		O(N)
	Space		O(N)
	36 ms, faster than 49.57%
"""
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        ht = defaultdict(list)
        for i in range(len(B)):
            num = B[i]
            ht[num].append(i)
        res = []
        for num in A:
            top = ht[num].pop()
            res.append(top)
        return res