from heapq import heappop, heappush
from collections import defaultdict

"""
    1st: hashtable + minheap

    Time of join()      O(C)
    Time of leave()     O(C)
    Time of request()   O(NlogN) N = average number of chunks per user
    Space               O(F+U)
    840 ms, faster than 100.00%
"""


class FileSharing:

    def __init__(self, m: int):
        self.users = defaultdict(set)
        self.files = defaultdict(set)
        self.leaves = []

    def join(self, ownedChunks: List[int]) -> int:
        userId = len(self.users) + 1
        if len(self.leaves) > 0:
            userId = heappop(self.leaves)
        self.users[userId] = set(ownedChunks)
        for c in ownedChunks:
            self.files[c].add(userId)
        return userId

    def leave(self, userID: int) -> None:
        if userID not in self.users:
            return
        for c in self.users[userID]:
            self.files[c].remove(userID)
        self.users[userID] = set()
        heappush(self.leaves, userID)

    def request(self, userID: int, chunkID: int) -> List[int]:
        arr = list(self.files[chunkID])
        arr.sort()
        self.users[userID].add(chunkID)
        self.files[chunkID].add(userID)
        return arr
