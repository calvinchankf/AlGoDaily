"""
    1st: hashtable + sort
    - similar to lc347, 692, 1772

    Time    O(M + NlogN) M: responses,  N: keys
    Space   O(N)
    352 ms, faster than 100.00% 
"""


class Solution(object):
    def sortFeatures(self, features, responses):
        counter = {}
        for i in range(len(features)):
            key = features[i]
            counter[key] = [0, i]
        for s in responses:
            words = s.split(' ')
            for w in set(words):
                if w in counter:
                    counter[w][0] += 1
        freqs = []
        for key in counter:
            f, i = counter[key]
            freqs.append((key, f, i))
        freqs.sort(key=lambda x: (-x[1], x[2]))

        return [key for key, f, i in freqs]
