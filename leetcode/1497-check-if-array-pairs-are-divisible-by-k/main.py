from typing import List
from collections import defaultdict

"""
    1st: math + hashtable
    - similar to lc1
    
    e.g. arr = [3, 6, 3, 4, 4, 1] k = 7
    
    at idx = 0
    3%7 = 3, so we put 3 in a hashtable and wait for its counterpart
    {
        3: 1
    }

    at idx = 1
    6%7 = 6, so we put 6 in a hashtable and wait for its counterpart
    {
        3: 1,
        6: 1,
    }

    at idx = 2
    3%7 = 6, so we put 3 in a hashtable and wait for its counterpart
    {
        3: 2,
        6: 1,
    }

    at idx = 3
    4%7 = 4, since 7 - 4 = 3 and 3 is in hashtable, we decrement "3"
    {
        3: 1,
        6: 1,
    }

    at idx = 4
    4%7 = 4, since 7 - 4 = 3 and 3 is still in hashtable, we decrement "3" and remove it becos its count = 0
    {
        6: 1,
    }

    at idx = 5
    1%7 = 1, since 7 - 1 = 6 and 6 is in hashtable, we decrement "6" and remove it becos its count = 0
    {}

    Finally, the size of the hashtable = 0, it means all the numbers can be paired up

    Time    O(N)
    Space   O(N)
    784 ms, faster than 33.33% 
"""


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        ht = defaultdict(int)
        for x in arr:
            cur = x % k
            remain = (k - cur) % k
            if remain in ht:
                ht[remain] -= 1
                if ht[remain] == 0:
                    del ht[remain]
            else:
                ht[cur] += 1
        return len(ht) == 0
