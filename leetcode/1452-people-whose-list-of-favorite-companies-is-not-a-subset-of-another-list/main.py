"""
    1st: brute force + hashtable
    - save the favoriteCompanies as a hashtable for every person
    - for every person, find out his favoriteCompanies in a subset of another's favoriteCompanies

    Time    O(ABC)
    Space   O(A)
    1008 ms, faster than 100.00%
"""


class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        hts = []
        for i in range(len(favoriteCompanies)):
            comps = favoriteCompanies[i]
            hts.append(set(comps))
        res = []
        for i in range(len(favoriteCompanies)):
            comps = favoriteCompanies[i]
            found_ = False
            for j in range(len(hts)):
                if i == j:
                    continue
                ht = hts[j]
                found = True
                for comp in comps:
                    if comp not in ht:
                        found = False
                found_ = found_ or found

            if not found_:
                res.append(i)
        return res
