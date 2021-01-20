
import random

"""
    learned from others
    
    ref:
    - https://www.youtube.com/watch?v=783qX31AN08
    - https://www.youtube.com/watch?v=2g9OSRKJuzM

    Time of search(), add(), delete()       O(logN) average -> O(N) worst
    Space                                   O(N)
    320 ms, faster than 56.41%
"""


class Node:
    def __init__(self, val=-1, right=None, down=None):
        self.val = val
        self.right = right
        self.down = down


class Skiplist:
    def __init__(self):
        self.head = Node()  # Dummy head

    def search(self, target: int) -> bool:
        cur = self.head
        while cur:
            # Move to the right in the current level
            while cur.right and cur.right.val < target:
                cur = cur.right
            if cur.right and cur.right.val == target:
                return True
            # Move to the the next level
            cur = cur.down
        return False

    def add(self, num: int) -> None:
        nodes = []
        cur = self.head
        while cur:
            # Move to the right in the current level
            while cur.right and cur.right.val < num:
                cur = cur.right
            nodes.append(cur)
            # Move to the next level
            cur = cur.down

        shouldInsert = True
        bottomNode = None
        while len(nodes) > 0 and shouldInsert:
            node = nodes.pop()
            node.right = Node(num, node.right, bottomNode)
            bottomNode = node.right
            shouldInsert = (random.getrandbits(1) == 0)

        # Create a new level with a dummy head
        if shouldInsert:
            self.head = Node(-1, None, self.head)

    def erase(self, num: int) -> bool:
        cur = self.head
        found = False
        while cur:
            # Move to the right in the current level
            while cur.right and cur.right.val < num:
                cur = cur.right
            # Find the target node
            if cur.right and cur.right.val == num:
                # Delete by skipping
                cur.right = cur.right.right
                found = True
            # Move to the next level
            cur = cur.down
        return found
