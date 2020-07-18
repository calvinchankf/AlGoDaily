from typing import List
from collections import *

"""
    1st: hashtables
    - 2 hashtables
    - one hashtable stores the (unique key: next number) as (key: value)
    - one hastable stores the result

    Time    O(N) -> O(N^2)
    Space   O(N)
    460 ms, faster than 60.84%
"""


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ht = {}
        res = OrderedDict()
        for name in names:
            if name not in ht and name not in res:
                ht[name] = 1
                res[name] = True
            elif name not in ht:
                ht[name] = 1
                key = name + '(' + str(ht[name]) + ')'
                while key in res:
                    ht[name] += 1
                    key = name + '(' + str(ht[name]) + ')'
                res[key] = True
            elif name not in res:
                key = name + '(' + str(ht[name]) + ')'
                res[key] = True
            else:
                key = name + '(' + str(ht[name]) + ')'
                while key in res:
                    ht[name] += 1
                    key = name + '(' + str(ht[name]) + ')'
                res[key] = True
        return list(res)


s = Solution()

a = ["pes", "fifa", "gta", "pes(2019)"]
print(s.getFolderNames(a))

a = ["gta", "gta(1)", "gta", "avalon"]
print(s.getFolderNames(a))

a = ["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]
print(s.getFolderNames(a))

a = ["wano", "wano", "wano", "wano"]
print(s.getFolderNames(a))

a = ["kaido", "kaido(1)", "kaido", "kaido(1)"]
print(s.getFolderNames(a))

a = ["pes", "fifa", "gta", "gta", "abc",
     "abc(2)", "abc", "abc(1)", "abc", "abc(1)"]
print(s.getFolderNames(a))

# 21th
a = ["r(1)", "r", "r(2)(1)", "r", "r", "r", "r",
     "r(1)", "r", "r", "r(2)", "r(2)(1)", "r"]
print(s.getFolderNames(a))

print("-----")

"""
    2nd: optimize the 1st

    Time    O(N) -> O(N^2)
    Space   O(N)
    436 ms, faster than 68.01%
"""


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ht = {}
        res = OrderedDict()
        for name in names:

            if name not in ht:
                ht[name] = 1

            if name not in res:
                res[name] = True
                continue

            key = name + '(' + str(ht[name]) + ')'
            while key in res:
                ht[name] += 1
                key = name + '(' + str(ht[name]) + ')'
            res[key] = True

        return list(res)


s = Solution()

a = ["pes", "fifa", "gta", "pes(2019)"]
print(s.getFolderNames(a))

a = ["gta", "gta(1)", "gta", "avalon"]
print(s.getFolderNames(a))

a = ["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]
print(s.getFolderNames(a))

a = ["wano", "wano", "wano", "wano"]
print(s.getFolderNames(a))

a = ["kaido", "kaido(1)", "kaido", "kaido(1)"]
print(s.getFolderNames(a))

a = ["pes", "fifa", "gta", "gta", "abc",
     "abc(2)", "abc", "abc(1)", "abc", "abc(1)"]
print(s.getFolderNames(a))

# 21th
a = ["r(1)", "r", "r(2)(1)", "r", "r", "r", "r",
     "r(1)", "r", "r", "r(2)", "r(2)(1)", "r"]
print(s.getFolderNames(a))

"""
['pes', 'fifa', 'gta', 'pes(2019)']
['gta', 'gta(1)', 'gta(2)', 'avalon']
['onepiece', 'onepiece(1)', 'onepiece(2)', 'onepiece(3)', 'onepiece(4)']
['wano', 'wano(1)', 'wano(2)', 'wano(3)']
['kaido', 'kaido(1)', 'kaido(2)', 'kaido(1)(1)']
['pes', 'fifa', 'gta', 'gta(1)', 'abc', 'abc(2)', 'abc(1)', 'abc(1)(1)', 'abc(3)', 'abc(1)(2)']
["r(1)","r","r(2)(1)","r(2)","r(3)","r(4)","r(5)","r(1)(1)","r(6)","r(7)","r(2)(2)","r(2)(1)(1)","r(8)"]
"""
